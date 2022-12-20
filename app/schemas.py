from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Optional
from pydantic import conint


# client/users (post/requests) 
# sending requests to API endpoint

# postBase() dB-schema: PostBase(BaseModel) 
# create basemodel using inheritance
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True
    
# postBase using inheritance(child) 
# create basemodel from parent class
class PostCreate(PostBase):
    pass


# no password in plain text
# we have ommitted the password field for security reasons
# only the (id), and (email) fields) used here
class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True

# client/users (get/response)
# getting response from API endpoint
# extending postBase schema class which is already defined above
class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut
    
    class Config:
        orm_mode = True
        

# Create a voting post
class PostOut(BaseModel):
    Post: Post
    votes: int

    class Config:
        orm_mode = True
           
# create a new user endpoint
class UserCreate(BaseModel):
    email: EmailStr
    password: str
    

# create a new user login
class UserLogin(BaseModel):
    email: EmailStr
    password: str
    
 
# client/users(access token) model     
class Token(BaseModel):
    access_token: str
    token_type: str

# client/users(token_data) model
class TokenData(BaseModel):
    id: Optional[str] = None
    

class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)
    
    
