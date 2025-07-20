#!/bin/sh
set -e

# 设置 PYTHONPATH
export PYTHONPATH=/app

# 初始化数据库
echo "🚀 Running DB init and seed script..."
python -m app.scripts.init_db

# 启动应用
echo "✅ DB initialized. Starting FastAPI app..."
exec uvicorn app.main:app --host 0.0.0.0 --port 9999 --reload