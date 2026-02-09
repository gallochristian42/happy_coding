@echo off
echo ===================================
echo Happy Coding - FastAPI Project Setup
echo ===================================
echo.

REM 检查Python是否安装
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python未安装，请先安装Python 3.8+
    pause
    exit /b 1
)

echo ✅ Python已安装

REM 创建虚拟环境
if not exist "venv" (
    echo 📦 创建虚拟环境...
    python -m venv venv
) else (
    echo ✅ 虚拟环境已存在
)

REM 激活虚拟环境
echo 🔧 激活虚拟环境...
call venv\Scripts\activate.bat

REM 安装依赖
echo 📥 安装依赖...
python -m pip install --upgrade pip
pip install -r requirements.txt

REM 询问是否安装开发依赖
set /p install_dev="是否安装开发依赖？(y/n): "
if /i "%install_dev%"=="y" (
    pip install -r requirements-dev.txt
    echo ✅ 开发依赖安装完成
)

REM 创建.env文件
if not exist ".env" (
    echo 📝 创建.env文件...
    copy .env.example .env
    echo ✅ .env文件已创建，请根据需要修改配置
) else (
    echo ✅ .env文件已存在
)

echo.
echo ===================================
echo ✅ 项目设置完成！
echo ===================================
echo.
echo 下一步：
echo 1. 修改 .env 文件配置
echo 2. 运行: uvicorn src.main:app --reload
echo 3. 访问: http://localhost:8000/docs
echo.
pause
