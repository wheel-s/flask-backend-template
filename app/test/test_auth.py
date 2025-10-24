



def protected(client):
    token = 'aks'
    headers = {"Authorization": f"Bearer {token}"}
    res = client.get('/api/v1/students', headers)

    assert res.status_code ==200
    assert "email" in res.get_json()