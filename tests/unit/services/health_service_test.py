def test_health_check_endpoint_returns_healthy(client):
    response = client.get("/health/")
    assert response.status_code == 200
    assert response.json == {"healthy": True}
