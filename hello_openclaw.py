#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hello OpenClaw!
一个简单的 Python 脚本，展示 OpenClaw 的能力。
"""

def greet(name: str) -> str:
    """打招呼函数"""
    return f"你好，{name}！欢迎使用 OpenClaw！🦞"

def main():
    """主函数"""
    print("=" * 50)
    print("🦞 OpenClaw 演示脚本")
    print("=" * 50)
    
    # 打招呼
    message = greet("用户")
    print(f"\n{message}\n")
    
    # 展示一些功能
    print("✨ OpenClaw 可以做到：")
    print("  - 📸 截屏并发送到飞书")
    print("  - 🎤 录音并转录文字")
    print("  - 📰 监控博客更新")
    print("  - 🌤️ 查询天气")
    print("  - 📁 管理文件")
    print("  - 💬 多平台聊天（飞书、WhatsApp 等）")
    print("\n" + "=" * 50)
    print("祝你使用愉快！😊")
    print("=" * 50)

if __name__ == "__main__":
    main()
