from fastapi.testclient import TestClient
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.main import app
from app.config import settings
from app.database import get_db
from app.database import Base
from app.oauth2 import create_access_token
from app import models
from alembic import command


# SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:passwd123@localhost:5432/fastapi_test'
SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.db_username}:{settings.db_password}@{settings.db_hostname}:{settings.db_port}/{settings.db_name}_test'

engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(
    autocommit=False, 
    autoflush=False, 
    bind=engine)


@pytest.fixture
def session():
    print("my session fixture created")
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
       yield db
    finally:
       db.close()


# run the code generator before the test
# command.upgrade("head")
@pytest.fixture
def client(session):
  def override_get_db():
    try:
        yield session
    finally:
      session.close()
  app.dependency_overrides[get_db] = override_get_db
  yield TestClient(app)
  # command.downgrade("base")
  # run the code after test finishes

@pytest.fixture
def client(session):
  def override_get_db():
    try:
        yield session
    finally:
      session.close()
  app.dependency_overrides[get_db] = override_get_db
  yield TestClient(app)
  # command.downgrade("base")
  # run the code after test finishes
  

# create a test_user a fixture to created login user
@pytest.fixture
def test_user2(client):
  user_data = {"email": "lamin@ipdxhub.live",
               "password": "passwd123"}
  res = client.post("/users/", json=user_data)

  assert res.status_code == 201
  # print(res.json())
  new_user = res.json()
  new_user["password"] = user_data["password"]
  return new_user


  
# create a test_user a fixture to created login user
@pytest.fixture
def test_user(client):
  user_data = {"email": "admin@ipdxhub.live",
               "password": "passwd123"}
  res = client.post("/users/", json=user_data)

  assert res.status_code == 201
  # print(res.json())
  new_user = res.json()
  new_user["password"] = user_data["password"]
  return new_user


# create a new user with token
@pytest.fixture
def token(test_user):
    return create_access_token({"user_id": test_user['id']})


# create authenticated user
@pytest.fixture
def authorized_client(client, token):
    client.headers = {**client.headers,
    "Authorization": f"Bearer {token}"
    .format(token=token)
    
    }
    return client


@pytest.fixture
def test_posts(test_user, session, test_user2):
    posts_data = [{
        "title": "first post",
        "content": "first content",
        "owner_id": test_user['id']
    }, {
        "title": "2nd post",
        "content": "2nd content",
        "owner_id": test_user['id']
    }, {
        "title": "3rd post",
        "content": "3rd content",
        "owner_id": test_user['id']
    }, {
        "title": "tyson post",
        "content": "tyson content",
        "owner_id": test_user2['id']
    }]
    
    def create_post_model(post):
        return models.Post(**post)
    
    post_map = map(create_post_model, posts_data)
    posts = list(post_map)
    
    session.add_all(posts)
    # session.add_all(
    #     [models.Post(
    #         title="first title",
    #         content="first content",
    #         owner_id=test_user['id']),
    #      models.Post(
    #          title="2nd title",
    #          content="2nd content",
    #          owner_id=test_user['id']),
    #     models.Post(
    #         title="3rd title",
    #         content="3rd content",
    #         owner_id=test_user['id'])
    # ])
    session.commit()
    posts = session.query(models.Post).all()
    return posts
    




