from tkinter import S
from jose import JWSError,jwt
from typing import Optional
from datetime import datetime,timedelta
from fastapi import FastAPI,Response,status,HTTPException,Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import schemas,database,models
from sqlalchemy.orm import Session
from config import settings

oauth2_scheme=OAuth2PasswordBearer(tokenUrl='/login')

# to get a SCECRET_KEY string :
#ALGORITHM
# openssl rand -hex 32
SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithms
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes
#SECRET_KEY = "09d25e094faa6ca4488c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
#ALGORITHM = "HS256"
#ACCESS_TOKEN_EXPIRE_MINUTES = 60

def create_access_token(data: dict): 
    to_encode = data.copy()

    expire= datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_access_token(token:str,credentials_exception):
    try:

        playload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        id:str=playload.get("user_id")
        if id is None:
            raise credentials_exception
        token_data=schemas.TokenData(id=id)
    
    except JWSError:
        raise credentials_exception

    return token_data

def get_current_user(token:str=Depends(oauth2_scheme),db:Session=Depends(database.get_db)):
    credentials_exception=HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
             detail=f"cloud not validate this ",headers={"www_AUTH":"Bearer"})
    
    token = verify_access_token(token,credentials_exception)
    user = db.query(models.User).filter(models.User.id == token.id).first()
    return user
    #return verify_access_token(token,credentials_exception)



