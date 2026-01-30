#!/usr/bin/env python3
import sys
sys.path.insert(0, '/usr/local/lib/python3.11/site-packages')

from setuptools import setup, find_packages
from setuptools.dist import Distribution

# 创建分发对象
dist = Distribution({
    "name": "iflow-mcp_sparshdrolia_persistent-code",
    "version": "0.1.0",
    "description": "An MCP server for maintaining code knowledge across LLM chat sessions",
    "packages": find_packages(),
    "install_requires": [
        "mcp>=1.2.0",
        "llama-index-core>=0.9.0",
        "llama-index>=0.9.0",
        "llama-index-embeddings-huggingface>=0.1.0",
        "transformers>=4.34.0",
        "networkx>=3.1",
        "sentence-transformers>=2.2.0",
        "pydantic>=2.0.0",
        "sqlalchemy>=2.0.0",
        "fastapi>=0.103.0",
        "uvicorn>=0.23.0",
        "python-dotenv>=1.0.0",
    ],
    "entry_points": {
        "console_scripts": [
            "persistent-code=persistent_code.__main__:main",
        ],
    },
    "python_requires": ">=3.10",
})

# 运行构建命令
dist.run_command('sdist')
dist.run_command('bdist_wheel')

print("Build completed successfully!")
print("Distribution files are in the 'dist' directory.")