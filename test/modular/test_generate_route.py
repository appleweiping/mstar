from fastapi.testclient import TestClient

from mstar.api_server import entrypoint


def test_generate_rejects_malformed_model_kwargs(monkeypatch):
    monkeypatch.setattr(entrypoint, "api_server", object())

    response = TestClient(entrypoint.app).post(
        "/generate",
        data={"model_kwargs": "{"},
    )

    assert response.status_code == 400
    assert response.json() == {"detail": "model_kwargs must be valid JSON"}
