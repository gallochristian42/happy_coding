.PHONY: help install install-dev run dev test lint format clean docker-build docker-up docker-down migrate

help: ## 显示帮助信息
	@echo "可用命令:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'

install: ## 安装生产依赖
	pip install --upgrade pip
	pip install -r requirements.txt

install-dev: ## 安装开发依赖
	pip install --upgrade pip
	pip install -r requirements.txt
	pip install -r requirements-dev.txt

run: ## 运行应用（生产模式）
	uvicorn src.main:app --host 0.0.0.0 --port 8000

dev: ## 运行应用（开发模式）
	uvicorn src.main:app --reload --host 0.0.0.0 --port 8000

test: ## 运行测试
	pytest tests/ -v

test-cov: ## 运行测试并生成覆盖率报告
	pytest --cov=src --cov-report=html --cov-report=term tests/

lint: ## 代码检查
	flake8 src/
	pylint src/

format: ## 代码格式化
	black src/ tests/
	isort src/ tests/

clean: ## 清理临时文件
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	rm -rf .pytest_cache
	rm -rf .coverage
	rm -rf htmlcov
	rm -rf dist
	rm -rf build

docker-build: ## 构建Docker镜像
	docker-compose build

docker-up: ## 启动Docker容器
	docker-compose up -d

docker-down: ## 停止Docker容器
	docker-compose down

docker-logs: ## 查看Docker日志
	docker-compose logs -f

migrate-create: ## 创建数据库迁移
	alembic revision --autogenerate -m "$(msg)"

migrate-upgrade: ## 应用数据库迁移
	alembic upgrade head

migrate-downgrade: ## 回滚数据库迁移
	alembic downgrade -1

db-init: ## 初始化数据库
	alembic upgrade head
