def test_signup_and_unregister(client):
    activity_name = "Chess Club"
    email = "test@mergington.edu"

    # Signup
    signup_resp = client.post(f"/activities/{activity_name}/signup", params={"email": email})
    assert signup_resp.status_code == 200
    assert signup_resp.json()["message"].startswith("Signed up")

    # Unregister (DELETE to /signup, not /unregister)
    unregister_resp = client.delete(f"/activities/{activity_name}/signup", params={"email": email})
    assert unregister_resp.status_code == 200
    assert unregister_resp.json()["message"].startswith("Unregistered")
