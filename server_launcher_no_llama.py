#!/usr/bin/env python3
"""
服务器启动脚本 - 禁用LlamaIndex以避免网络问题
"""
import sys

# 添加必要的路径到sys.path
sys.path.insert(0, '/usr/local/lib/python3.11/site-packages')
sys.path.insert(0, '/app/auto-mcp-upload/data/2346')

# 模拟命令行参数，添加 --disable-llama-index
sys.argv = [sys.argv[0]] + sys.argv[1:] + ['--transport', 'stdio']

if __name__ == "__main__":
    import os
    # 设置环境变量禁用 LlamaIndex
    os.environ['DISABLE_LLAMA_INDEX'] = 'true'
    
    # 直接运行服务器
    from persistent_code.mcp_server import PersistentCodeMCP
    
    # 创建并运行服务器，禁用 LlamaIndex
    from persistent_code.config import config as config_instance
    config_instance.set("llama_index", "enabled", False)
    
    server = PersistentCodeMCP(project_name="test", storage_dir=None)
    print("Starting persistent-code MCP server for project 'test' (LlamaIndex disabled)")
    server.run(transport="stdio")