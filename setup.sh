#!/bin/bash

echo "==================================="
echo "Happy Coding - FastAPI Project Setup"
echo "==================================="
echo ""

# 检查Python是否安装
if ! command -v python3 &> /dev/null && ! command -v python &> /dev/null
then
    echo "❌ Python未安装，请先安装Python 3.8+"
    exit 1
fi

echo "✅ Python已安装"

# 创建虚拟环境
if [ ! -d "venv" ]; then
    echo "📦 创建虚拟环境..."
    python3 -m venv venv || python -m venv venv
else
    echo "✅ 虚拟环境已存在"
fi

# 激活虚拟环境
echo "🔧 激活虚拟环境..."
source venv/bin/activate || . venv/Scripts/activate

# 安装依赖
echo "📥 安装依赖..."
pip install --upgrade pip
pip install -r requirements.txt

# 安装开发依赖
read -p "是否安装开发依赖？(y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]
then
    pip install -r requirements-dev.txt
    echo "✅ 开发依赖安装完成"
fi

# 创建.env文件
if [ ! -f ".env" ]; then
    echo "📝 创建.env文件..."
    cp .env.example .env
    echo "✅ .env文件已创建，请根据需要修改配置"
else
    echo "✅ .env文件已存在"
fi

echo ""
echo "==================================="
echo "✅ 项目设置完成！"
echo "==================================="
echo ""
echo "下一步："
echo "1. 修改 .env 文件配置"
echo "2. 运行: uvicorn src.main:app --reload"
echo "3. 访问: http://localhost:8000/docs"
echo ""
