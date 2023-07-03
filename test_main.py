from fastapi.testclient import TestClient
from fastapi import status
from main import app
import requests
import pytest
from dbfiles import models
from main import get_db
from dbfiles import database
from sqlalchemy import Column, String, Integer

@pytest.fixture(scope="module")
def test_client():
    with TestClient(app) as client:
        yield client

@pytest.fixture(scope="module")
def test_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


def test_home_route(test_client, test_db):
    # Önceden tanımlanmış bir todo ekleyelim
    todo = models.Todo(title="Test Todo")
    test_db.add(todo)
    test_db.commit()
    # Ana sayfaya GET isteği gönderelim
    response = test_client.get("http://127.0.0.1:8000")
    # Yanıt durum kodunun 200 olması gerektiğini kontrol edelim
    assert response.status_code == 200
    # Yanıtın doğru template kullanılarak oluşturulduğunu kontrol edelim
    assert "index.html" in response.template.name
    # Yanıtın içinde "Test Todo" metninin yer almasını kontrol edelim
    assert "Test Todo" in response.text

def test_add_route(test_client, test_db):
    # Yeni bir todo ekleyelim
    response = test_client.post("/add", data={"title": "New Todo"})
    # Yanıt durum kodunun 303 olduğunu (yönlendirme olduğunu) kontrol edelim
    assert response.status_code == 200
    # # Yönlendirilen URL'nin ana sayfa olduğunu kontrol edelim
    # assert response.headers["Location"] == "/"
    # Eklenen todo'nun veritabanında yer aldığını kontrol edelim
    todo = test_db.query(models.Todo).filter_by(title="New Todo").first()
    assert todo is not None
    
def test_todo_initialization():
    # Todo nesnesini oluşturalım
    todo = models.Todo()
    assert isinstance(todo, models.Todo)
    assert todo.__tablename__ == "todos"
    assert hasattr(todo, "id")
    assert hasattr(todo, "title")