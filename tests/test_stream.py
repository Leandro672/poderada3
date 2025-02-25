from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_stream_video_available():
    response = client.get("/stream/vid123")
    assert response.status_code == 200
    assert response.json() == {"message": "Reproduzindo o vídeo vid123"}

def test_stream_video_unavailable():
    response = client.get("/stream/vid000")
    assert response.status_code == 404
    assert response.json() == {"detail": "Vídeo não encontrado"}
