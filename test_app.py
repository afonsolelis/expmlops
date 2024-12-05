import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_train_endpoint(client):
    response = client.get('/train')
    assert response.status_code == 200
    data = response.get_json()

    # Verificar as chaves no JSON retornado
    assert "classification_report" in data
    assert "accuracy" in data

    # Verificar se a acurácia é um valor numérico
    assert isinstance(data["accuracy"], float)
    assert 0 <= data["accuracy"] <= 1
