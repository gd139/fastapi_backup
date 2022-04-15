from hashlib import algorithms_available
import secrets
from pydantic import BaseSettings

class Settings(BaseSettings):
    database_hostname:str
    database_port:str
    database_password:str
    database_name:str
    database_username:str
    secret_key:str
    algorithms:str
    access_token_expire_minutes:int

    class Config:
      env_file = ".env"

settings = Settings()

