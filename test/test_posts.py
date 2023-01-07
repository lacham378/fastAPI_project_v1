import pytest
from typing import List
from app import schemas


def test_get_all_posts(authorized_client, test_posts):
    res= authorized_client.get("/posts/")
    
    def validate(post):
        return schemas.PostOut(**post)
    posts_map = map(validate, res.json())
    posts_list = list(posts_map)
    
    
    assert len(res.json()) == len(test_posts)
    assert res.status_code == 200
    # assert posts_list[0].Post.id == test_posts[0].id 

# get all posts from unauthenticated user   
def test_unauthorized_user_get_all_posts(client, test_posts):
    res = client.get("/posts/")
    assert res.status_code == 401
    

# get invidual posts from unauthenticated user
def test_unauthorized_user_get_one_post(client, test_posts):
    res = client.get(f"/posts/{test_posts[0].id}")
    assert res.status_code == 401


def test_get_one_post_not_found(authorized_client, test_posts):
    res = authorized_client.get(f"/posts/00378")
    assert res.status_code == 404
    
    
def test_get_one_post(authorized_client, test_posts):
    res = authorized_client.get(f"/posts/{test_posts[0].id}")
    print(res.json())
    post = schemas.PostOut(**res.json())
    print(post)
    assert res.status_code == 200
    assert post.Post.id == test_posts[0].id
    assert post.Post.content == test_posts[0].content
    assert post.Post.title == test_posts[0].title

@pytest.mark.parametrize("title, content, published", [ 
    ("awesome app title", "awesome app content", True),
    ("my favourite app ", "love python content", False),
    ("awesome beaches ", "florida in USA beach", True),
    
])
def test_create_post(authorized_client, test_user, test_posts, title, content, published):
    res = authorized_client.post(
        "/posts/", json={'title': title, 'content':content, 'published': published})
    
    create_post = schemas.Post(**res.json())
    assert res.status_code == 201
    assert create_post.title == title
    assert create_post.content == content
    assert create_post.published == published
    assert create_post.owner_id == test_user['id']
    

def test_create_post_default_published_true(authorized_client, test_user, test_posts):
    res = authorized_client.post(
        "/posts/", json={'title': "fast api", 'content': "its awesome stuff"})
    
    create_post = schemas.Post(**res.json())
    assert res.status_code == 201
    assert create_post.title == "fast api"
    assert create_post.content == "its awesome stuff"
    assert create_post.published == True
    assert create_post.owner_id == test_user['id']

# test unauthenticated user
def test_unauthorized_user_create_post(client, test_user, test_posts):
    res = client.post(
        "/posts/", json={'title': "fast api", 'content': "its awesome stuff"})
    assert res.status_code == 401
    

def test_unauthorized_user_delete_post(client, test_user, test_posts):
    res = client.delete(
        f"/posts/{test_posts[0].id}")
    assert res.status_code == 401
    
    
def test_delete_post_success(authorized_client, test_user, test_posts):
    res = authorized_client.delete(
        f"/posts/{test_posts[0].id}")
    assert res.status_code == 204


def test_delete_post_non_exist(authorized_client, test_user, test_posts):
    res = authorized_client.delete(
        f"/posts/8000000")
    assert res.status_code == 404


def test_delete_other_user_post(authorized_client, test_user, test_posts):
    res = authorized_client.delete(
        f"/posts/{test_posts[3].id}")
    assert res.status_code == 403
    
    
def test_update_post(authorized_client, test_user, test_posts):
    data = {
        "title": "updated title",
        "content": "updated content",
        "id": test_posts[0].id
        
    }
    res = authorized_client.put(f"/posts/{test_posts[0].id}", json=data)
    updated_post = schemas.Post(**res.json())
    assert res.status_code == 200
    assert updated_post.title == data["title"]
    assert updated_post.content == data["content"]
    assert updated_post.id == data["id"]


def test_update_other_user_post(authorized_client, test_user, test_user2, test_posts):
    data = {
        "title": "updated title",
        "content": "updated content",
        "id": test_posts[3].id

    }
    res = authorized_client.put(f"/posts/{test_posts[3].id}", json=data)
    assert res.status_code == 403


def test_unauthorized_user_update_post(client, test_user, test_posts):
    res = client.put(
        f"/posts/{test_posts[0].id}")
    assert res.status_code == 401


def test_update_post_non_exist(authorized_client, test_user, test_posts):
    data = {
        "title": "updated title",
        "content": "updated content",
        "id": test_posts[3].id

    }
    res = authorized_client.put(
        f"/posts/8000000", json=data)
    assert res.status_code == 404
