#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
图像识别演示脚本
使用 OpenCV 进行基础图像识别和处理
功能：边缘检测、颜色识别、物体轮廓检测
"""

import cv2
import numpy as np
from pathlib import Path


def detect_edges(image_path: str, output_path: str) -> dict:
    """
    边缘检测
    
    Args:
        image_path: 输入图片路径
        output_path: 输出图片路径
        
    Returns:
        检测结果字典
    """
    # 读取图片
    image = cv2.imread(image_path)
    if image is None:
        return {"success": False, "error": "无法读取图片"}
    
    # 转换为灰度图
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Canny 边缘检测
    edges = cv2.Canny(gray, 100, 200)
    
    # 保存结果
    cv2.imwrite(output_path, edges)
    
    return {
        "success": True,
        "image_shape": image.shape,
        "edges_detected": np.sum(edges > 0),
        "output_path": output_path
    }


def detect_colors(image_path: str) -> dict:
    """
    颜色识别
    
    Args:
        image_path: 输入图片路径
        
    Returns:
        颜色分析结果
    """
    image = cv2.imread(image_path)
    if image is None:
        return {"success": False, "error": "无法读取图片"}
    
    # 转换为 HSV 色彩空间
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    # 定义颜色范围（BGR 格式）
    colors = {
        "红色": ([0, 70, 50], [10, 255, 255]),
        "绿色": ([40, 70, 50], [80, 255, 255]),
        "蓝色": ([100, 70, 50], [130, 255, 255]),
        "黄色": ([20, 70, 50], [35, 255, 255]),
    }
    
    results = {}
    for color_name, (lower, upper) in colors.items():
        mask = cv2.inRange(hsv, np.array(lower), np.array(upper))
        pixel_count = np.sum(mask > 0)
        percentage = (pixel_count / (image.shape[0] * image.shape[1])) * 100
        results[color_name] = f"{percentage:.2f}%"
    
    return {
        "success": True,
        "color_distribution": results
    }


def detect_contours(image_path: str, output_path: str) -> dict:
    """
    物体轮廓检测
    
    Args:
        image_path: 输入图片路径
        output_path: 输出图片路径
        
    Returns:
        检测结果
    """
    image = cv2.imread(image_path)
    if image is None:
        return {"success": False, "error": "无法读取图片"}
    
    # 转换为灰度图
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # 高斯模糊
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # 阈值处理
    _, thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)
    
    # 查找轮廓
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # 绘制轮廓
    result = image.copy()
    cv2.drawContours(result, contours, -1, (0, 255, 0), 2)
    
    # 保存结果
    cv2.imwrite(output_path, result)
    
    return {
        "success": True,
        "contours_found": len(contours),
        "output_path": output_path
    }


def main():
    """主函数"""
    print("=" * 60)
    print("🖼️  OpenClaw 图像识别演示")
    print("=" * 60)
    
    # 检查示例图片
    sample_image = Path("/Users/tong/.openclaw/workspace/sample.jpg")
    
    if not sample_image.exists():
        print("\n❌ 未找到示例图片")
        print("请提供一张图片进行测试，例如：")
        print("  python3 image_recognition.py your_image.jpg")
        return
    
    print(f"\n📁 使用图片：{sample_image}")
    
    # 1. 边缘检测
    print("\n🔍 1. 边缘检测...")
    edge_result = detect_edges(
        str(sample_image),
        "/Users/tong/.openclaw/workspace/edges_output.jpg"
    )
    if edge_result["success"]:
        print(f"   ✅ 图片尺寸：{edge_result['image_shape']}")
        print(f"   ✅ 边缘像素：{edge_result['edges_detected']}")
        print(f"   ✅ 输出：{edge_result['output_path']}")
    else:
        print(f"   ❌ 失败：{edge_result.get('error')}")
    
    # 2. 颜色识别
    print("\n🎨 2. 颜色识别...")
    color_result = detect_colors(str(sample_image))
    if color_result["success"]:
        print("   📊 颜色分布：")
        for color, percentage in color_result["color_distribution"].items():
            print(f"      {color}: {percentage}")
    else:
        print(f"   ❌ 失败：{color_result.get('error')}")
    
    # 3. 轮廓检测
    print("\n🔲 3. 轮廓检测...")
    contour_result = detect_contours(
        str(sample_image),
        "/Users/tong/.openclaw/workspace/contours_output.jpg"
    )
    if contour_result["success"]:
        print(f"   ✅ 找到轮廓：{contour_result['contours_found']} 个")
        print(f"   ✅ 输出：{contour_result['output_path']}")
    else:
        print(f"   ❌ 失败：{contour_result.get('error')}")
    
    print("\n" + "=" * 60)
    print("✨ 图像处理完成！")
    print("=" * 60)


if __name__ == "__main__":
    main()
