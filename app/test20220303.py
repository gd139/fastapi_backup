from typing import Optional
from unicodedata import name
from fastapi import FastAPI,Response,status,HTTPException
from fastapi.params import Body
from numpy import delete
from pydantic import BaseModel
from random import randrange
import psycopg2
import psycopg2.extensions
from psycopg2.extras import RealDictCursor
import time

app = FastAPI()

try:
    conn = psycopg2.connect(host='localhost',dbname='fastapi',user='postgres',password='12345678',cursor_factory=RealDictCursor)
    cursor = conn.cursor()
    print("Database connection was succssful!")
    #break
except Exception as error:
    print("Connection to db was failed")
    print("Error: ", error)





#uvicorn app.TEST:app --reload

@app.get("/")
async def root():
    return {"message": "Hello World!!!!,i love this game"}
class Post(BaseModel):
     title: str
     content: str
     published: bool=True


my_posts=[{"title":"title os post 1","content":"content of post 1","id":1},
          {"title":"favorite foods","content":"I love pizze","id":2},
          {"title":"love song","content":"I love home","id":3}]

def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p

def find_index_post(id):
    for i,p in enumerate(my_posts):
        if p['id']==id:
            return i


@app.get("/posts")
def get_posts():
    #return{"data":"hi,good morning"}
    cursor.execute("SELECT * FROM posts")
    posts = cursor.fetchall()
    print(posts)
    return{"data":posts}




#@app.post("/creatposts")
#def creat_posts(playload: dict =Body(...)):
    #print(playload)
    #return{"news message":f"tittle:{playload['tittle']} name:{playload['name']}"} 

@app.post("/posts",status_code = status.HTTP_201_CREATED)
def creat_posts(post:Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0,9999)
    my_posts.append(post_dict)
   # print (post)
    print (post.dict())
    return {"data":post_dict}

@app.get("/posts/latest")
def get_latest_post():
    post = my_posts[len(my_posts)-1]
    return{"detail":post}    

@app.get("/posts/{id}")
def get_post(id:int):#response:Response):
    print(type(id))
    post = find_post(id)
    #return {"post_detail":f"Here is post {id}"}
    print(post)
    if not post:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
            detail=f"post with id: {id} was not found")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return{"message": f"post with id: {id} was not found"}
    return{"post_detail":post}

@app.delete("/posts/{id}", status_code = status.HTTP_204_NO_CONTENT)
def delete_post(id:int):
    index=find_index_post(id)
    if index==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id: {id} was not exist")
    my_posts.pop(index)
    return Response(status_code = status.HTTP_204_NO_CONTENT)
    #return{"message":'post was successfully deleted'}

@app.put("/posts/{id}")
def Update_post(id:int,post:Post):
    index=find_index_post(id)
    if index==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id: {id} was not exist")
    post_dict = post.dict()
    post_dict['id']=id
    my_posts[index]=post_dict
    print(post_dict)
    return{"data":post_dict,"home":my_posts}

