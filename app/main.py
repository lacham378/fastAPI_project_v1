# from random import randrange
# from typing import Optional, List
# from datetime import datetime
# from fastapi import FastAPI, Response, status, HTTPException, Depends
# from fastapi.params import Body
# from pydantic import BaseModel
# import psycopg2
# from psycopg2.extras import RealDictCursor
# import time
# from sqlalchemy.orm import Session
# from . import models, schemas, utils
# from . database import engine, get_db
from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from . import models
from . database import engine
from .routers import post, user, auth, vote
from .config import settings


print(settings.db_username)

# models.Base.metadata.create_all(bind=engine)
app = FastAPI()

# origins = ["https://www.google.com"]
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


#dB schema create a class base model
# class Post(BaseModel):
#     title: str
#     created_at: datetime = datetime.now()
#     content: str
#     published: bool = True
#     #rating: Optional[int] = None

    
               
# Save a model instances in memory
my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1}, {"title":
"favourite foods", "content": "I like pizza", "id": 2}]


def find_post(id):
    for p in my_posts:
        if p['id'] == id:
            return p
        
def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i
 
        
# define the routers
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


# Get method url:"/"
@app.get("/")
def root():
    return {"message": 
        "IPDXHUB.LIVE FastAPI"
            "Successfully Deployed CI/DC Pipeline on Ubuntu Server"}

# Get a receive method url:"/sqlalchemy"
# @app.get("/sqlalchemy")
# def test_posts(db: Session = Depends(get_db)):
#     posts = db.query(models.Post).all()
#     print(posts)
#     return {"data": posts}




