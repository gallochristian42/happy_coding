"""主程序测试"""

import sys
from pathlib import Path

# 添加src目录到路径
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_root():
    """测试根路径"""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "version" in data


def test_health_check():
    """测试健康检查"""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"


def test_example_endpoint():
    """测试示例端点"""
    response = client.get("/api/v1/example")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
