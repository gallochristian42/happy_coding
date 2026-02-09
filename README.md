# Happy Coding

一个标准的FastAPI项目模板

## 项目结构

```
happy_coding/
├── src/                        # 源代码目录
│   ├── api/                    # API路由
│   │   ├── v1/                 # API版本1
│   │   │   ├── endpoints/      # 端点
│   │   │   └── router.py       # 路由汇总
│   │   └── dependencies.py     # API依赖
│   ├── models/                 # 数据库模型
│   │   └── __init__.py
│   ├── schemas/                # Pydantic模型
│   │   └── __init__.py
│   ├── services/               # 业务逻辑
│   │   └── __init__.py
│   ├── config/                 # 配置文件
│   │   ├── settings.py         # 应用配置
│   │   └── database.py         # 数据库配置
│   ├── middleware/             # 中间件
│   │   └── __init__.py
│   ├── utils/                  # 工具函数
│   │   └── __init__.py
│   ├── __init__.py
│   └── main.py                 # 应用入口
├── tests/                      # 测试目录
│   ├── __init__.py
│   └── test_main.py
├── docker/                     # Docker相关文件
│   └── Dockerfile
├── alembic/                    # 数据库迁移
│   └── versions/
├── requirements.txt            # 项目依赖
├── requirements-dev.txt        # 开发依赖
├── docker-compose.yml          # Docker Compose配置
├── alembic.ini                 # Alembic配置
├── .env.example                # 环境变量示例
├── .gitignore                  # Git忽略文件
├── .dockerignore               # Docker忽略文件
└── README.md                   # 项目说明
```

## 安装依赖

```bash
pip install -r requirements.txt
```

## 配置环境变量

复制环境变量示例文件：

```bash
cp .env.example .env
```

根据需要修改 `.env` 文件中的配置。

## 运行项目

### 开发模式

```bash
uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
```

### 生产模式

```bash
uvicorn src.main:app --host 0.0.0.0 --port 8000 --workers 4
```

访问 API 文档：
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 数据库迁移

初始化Alembic：

```bash
alembic init alembic  # 已完成，跳过此步
```

创建新的迁移：

```bash
alembic revision --autogenerate -m "初始化数据库"
```

应用迁移：

```bash
alembic upgrade head
```

回滚迁移：

```bash
alembic downgrade -1
```

## 运行测试

```bash
pytest tests/
```

运行测试并生成覆盖率报告：

```bash
pytest --cov=src tests/
```

## Docker部署

### 构建镜像

```bash
docker build -f docker/Dockerfile -t happy_coding:latest .
```

### 使用Docker Compose

```bash
docker-compose up -d
```

## 开发

安装开发依赖：

```bash
pip install -r requirements-dev.txt
```

代码格式化：

```bash
black src/
isort src/
```

代码检查：

```bash
pylint src/
flake8 src/
```

## 项目特性

- ✅ FastAPI框架
- ✅ SQLAlchemy ORM
- ✅ Alembic数据库迁移
- ✅ Pydantic数据验证
- ✅ JWT认证支持
- ✅ CORS中间件
- ✅ Docker部署
- ✅ 分层架构（API、Service、Model）
- ✅ 环境变量配置
- ✅ 自动API文档

## 开发建议

1. **配置环境变量**：复制 `.env.example` 为 `.env` 并修改配置
2. **数据库模型**：在 `src/models/` 中添加新的数据库模型
3. **API端点**：在 `src/api/v1/endpoints/` 中添加新的API端点
4. **业务逻辑**：在 `src/services/` 中实现业务逻辑
5. **数据验证**：在 `src/schemas/` 中定义Pydantic模型
6. **中间件**：在 `src/middleware/` 中添加自定义中间件

## 常用命令

### 使用Makefile（推荐）

```bash
make help              # 查看所有可用命令
make install-dev       # 安装开发依赖
make dev               # 启动开发服务器
make test              # 运行测试
make test-cov          # 运行测试并生成覆盖率报告
make format            # 代码格式化
make lint              # 代码检查
make migrate-create msg="描述"  # 创建数据库迁移
make migrate-upgrade   # 应用数据库迁移
make docker-up         # 启动Docker
```

### 直接使用命令

```bash
# 启动开发服务器
uvicorn src.main:app --reload
# 或使用启动脚本
python run.py

# 创建数据库迁移
alembic revision --autogenerate -m "描述"

# 应用数据库迁移
alembic upgrade head

# 运行测试
pytest

# 代码格式化
black src/ && isort src/

# Docker构建和运行
docker-compose up --build
```
