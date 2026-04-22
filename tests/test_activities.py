def test_get_activities(client):
    response = client.get("/activities")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    # Check for at least one known activity
    assert "Chess Club" in data
    assert "participants" in data["Chess Club"]
