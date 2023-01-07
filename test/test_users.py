import pytest
from jose import jwt
from app import schemas
from app.config import settings



# def test_root(client):
#   res = client.get("/")
#   print(res.json().get('message')) 
#   assert res.json().get('message') == "Welcome to IPDXHUB.LIVE FastAPI 2022"
#   assert res.status_code == 200
  
  
def test_create_user(client):
    res = client.post("/users/", json={"email": "user@ipdxhub.live", "password": "passwd123"}
    )
    # print(res.json())
    new_user = schemas.UserOut(**res.json())
    assert res.json().get('email') == "user@ipdxhub.live", res.status_code == 201 
    assert new_user.email == "user@ipdxhub.live"


def test_login_user(test_user, client):
    res = client.post(
        "/login", data={"username": test_user["email"], "password": test_user["password"]})
    # print(res.json())
    login_res = schemas.Token(**res.json())
    payload = jwt.decode(login_res.access_token, settings.secret_key, algorithms=[settings.algorithm])
    id = payload.get("user_id")
    assert id == test_user["id"]
    assert login_res.token_type == "bearer"
    assert res.status_code == 200



@pytest.mark.parametrize("email, password, status_code", [
    ('wrongemail@ipdxhub.live', 'passwd123', 403),
    ('admin@ipdxhub.live', 'wrongpassword', 403),
    ('wrongemail@ipdxhub.live', 'wrongpassword', 403),
    (None, 'passwd123', 422),
    ('admin@ipdxhub.live', None, 422)
  
])
def test_incorrect_login(test_user, client, email, password, status_code):
    res = client.post(
      "/login", data={"username": email, "password": password})
    
    assert res.status_code == status_code
    # assert res.status_code == 403
    # assert res.json().get('detail') == 'Invalid Credentials'
