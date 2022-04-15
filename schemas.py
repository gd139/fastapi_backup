from ast import Pass
import email
from typing import Optional
from numpy import int0
from pydantic import BaseModel,EmailStr, conint
from datetime import datetime

class UserCreat(BaseModel):
     email:EmailStr
     password:str

     class Config:
        orm_mode = True

class UserOut(BaseModel):
     id:int
     email:EmailStr
     created_at:datetime
     class Config:
        orm_mode = True


class PostBase(BaseModel):
     title: str
     content: str
     published: bool=True
    
class PostCreat(PostBase):
    Pass

class Post(PostBase):  #BaseModel
     id:int
     #: str
     #nt: str
     #shed: bool
     created_at:datetime
     owner_id:int
     owner:UserOut

     class Config:
        orm_mode = True

#class UserCreat(BaseModel):
     #email:EmailStr
     ##password:str
##
#     #class Config:
     #   orm_mode = True
#
#class UserOut(BaseModel):
#     id:int
#     email:EmailStr
#     created_at:datetime
#     class Config:
#        orm_mode = True

class UserLogin(BaseModel):
     email:EmailStr
     password:str
     
     class Config:
        orm_mode = True

class Token(BaseModel):
     access_token:str
     token_type:str

class TokenData(BaseModel):
     id:Optional[str]=None
     class Config:
       orm_mode = True

class Vote(BaseModel):
     post_id:int
     dir:conint(le=1)
