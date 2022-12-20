
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from .database import Base

# create a new database instance("posts")  
class Post(Base):
    __tablename__ = 'posts'
    
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, server_default='TRUE', nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), 
                        nullable=False, server_default=text('now()'))
    # create foreign key constraints for table (posts)
    owner_id = Column(Integer, ForeignKey(  
        "users.id", ondelete="CASCADE"), nullable=False)
    
    
    # create an relationship between models based on owner_id
    owner = relationship("User")
    
# create user account(authentication)     
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, default=False)
    created_at = Column(TIMESTAMP(timezone=True),
                nullable=False, server_default=text('now()'))
    phone_number = Column(String)


# create a vote table using sqlalchemy class
class Vote(Base):
    __tablename__ = "votes"
    user_id = Column(Integer, ForeignKey(
        "users.id", ondelete="CASCADE"), primary_key=True)
    post_id = post_id = Column(Integer, ForeignKey(
        "posts.id", ondelete="CASCADE"), primary_key=True)
