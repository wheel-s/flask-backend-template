

def test_protected_route(client):
    client.post("api/auth/register", json={
        "username":"Blue",
        "email":"Cuzan2002@gmail.com",
        "password":"admin",
        "role":"admin"
    })
   
    login =  client.post("api/auth/login", json={
        "email":"Cuzan2002@gmail.com",
        "password":"admin"
    })
    assert login.status_code == 200
    data = login.get_json()
    token = data.get("access-token")
    token = str(token).strip()
    
    print(f"{token}\n")
    if not token:
        assert False, "token variable is empty, cannot proceed"
    res = client.get('/api/v1/student', headers={"Authoriaztion":f"Bearer {token}"})
    assert res.status_code == 401