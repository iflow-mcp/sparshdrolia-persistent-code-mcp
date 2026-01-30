#!/usr/bin/env python3
"""
服务器启动脚本 - 修复路径问题
"""
import sys

# 添加必要的路径到sys.path
sys.path.insert(0, '/usr/local/lib/python3.11/site-packages')
sys.path.insert(0, '/app/auto-mcp-upload/data/2346')

if __name__ == "__main__":
    from persistent_code.__main__ import main
    main()