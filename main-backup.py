from re import U
from turtle import pos
from typing import Optional,List
from unicodedata import name
from fastapi import FastAPI,Response,status,HTTPException,Depends,APIRouter
from fastapi.params import Body
from numpy import delete
from pydantic import BaseModel, BaseSettings, PostgresDsn,BaseSettings
from random import randrange
import psycopg2
import psycopg2.extensions
from psycopg2.extras import RealDictCursor
import time
from database import engine, get_db
from sqlalchemy.orm import Session
import models,schemas,utils
from routers import user,post,auth

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user.router)
app.include_router(post.router)
app.include_router(auth.router)

#
#@app.get("/sqlalchemy")
#def test_post(db: Session = Depends(get_db)):
#      posts=db.query(models.Post).all()
#      return{"data":posts}

   

while True:
    try:
       conn = psycopg2.connect(host='localhost',dbname='fastapi',user='postgres',password='12345678',cursor_factory=RealDictCursor)
       cursor = conn.cursor()
       print("Database connection was succssful!")
       break
    except Exception as error:
       print("Connection to db was failed")
       print("Error: ", error)
       time.sleep(2)


#uvicorn app.main:app --reload

@app.get("/")
async def root():
    return {"message": "Hello World!!!!,i love this game!!!"}



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







#@app.get("/posts",response_model= list[schemas.Post])
#def get_posts(db: Session = Depends(get_db)):
##return{"data":"hi,good morning"}
    ##cursor.execute("""SELECT * FROM posts where id in (1,2,3,4,7,8)""")
    ##posts= cursor.fetchall()
    #posts=db.query(models.Post).all()
    #print(posts)
    #return posts
    ##return{"data":posts}




#@app.post("/creatposts")
#def creat_posts(playload: dict =Body(...)):
    #print(playload)
    #return{"news message":f"tittle:{playload['tittle']} name:{playload['name']}"} 

#@app.post("/posts",status_code = status.HTTP_201_CREATED,response_model=schemas.Post)
#def creat_posts(post:schemas.PostCreat,db: Session = Depends(get_db)):
    ##sor.execute("""INSERT INTO posts(title,content,published) VALUES(%s,%s,%s) returning * """,
    #        (post.title,post.content,post.published))
    ##_post= cursor.fetchone()
    #print(new_post)
    #conn.commit()
    #print(**post.dict())
    #new_posts=models.Post(title=post.title,content=post.content,published=post.published)
    #new_posts=models.Post(**post.dict())
    #db.add(new_posts)
    #db.commit()
    #db.refresh(new_posts)
    #return{"data":new_posts}
    #return new_posts
    

    #post_dict = post.dict()
    # ['id'] = randrange(0,9999)
    #my_posts.append(post_dict)
   # print (post)
    #print (post.dict())
    #return {"data":post_dict}

#@app.get("/posts/latest")
#def get_latest_post():
#    post = my_posts[len(my_posts)-1]
#    return{"detail":post}    




#@app.get("/posts/{id}",response_model=schemas.Post)
#def get_post(id:int,db: Session = Depends(get_db)):#response:Response):
    ##print(type(id))
    ##cursor.execute("""SELECT * FROM posts WHERE id =%s""",(str(id)))
    ##post= cursor.fetchone()
    ##print(post)
    #post=db.query(models.Post).filter(models.Post.id==id).first()
  
    #return{"post_detail":post}

    #post = find_post(id)
    #return {"post_detail":f"Here is post {id}"}

    #return{"post_detail":test_post}
    #if not post:
    #    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
    #        detail=f"post with id: {id} was not found")
        ##response.status_code = status.HTTP_404_NOT_FOUND
        ##return{"message": f"post with id: {id} was not found"}

    ##return{"post_detail":post}
    #return post

#@app.delete("/posts/{id}", status_code = status.HTTP_204_NO_CONTENT)
#def delete_post(id:int,db: Session = Depends(get_db)):
    ##.execute("""DELETE FROM posts WHERE id =%s RETURNING *""" ,(str(id)),)
   # #post = cursor.fetchone()
    ##ommit()
    #post=db.query(models.Post).filter(models.Post.id==id)
    #print(post)
    ##if delet_post==None:
    #if post.first()==None:
    #    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id: {id} was not exist")
    #post.delete(synchronize_session=False)
    #db.commit()
    #return Response(status_code = status.HTTP_204_NO_CONTENT)
    ##return{"message":'post was successfully deleted'}

#@app.put("/posts/{id}",response_model=schemas.Post)
#def Update_post(id:int,update_post:schemas.PostCreat,db:Session = Depends(get_db)):
    ##cursor.execute("""UPDATE posts SET title=%s,content=%s,published=%s WHERE id=%s returning * """,
    ##       (post.title,post.content,post.published,str(id)))
    ##updated_post= cursor.fetchone()
    ##print(updated_post)
    ##conn.commit()
    #post_query=db.query(models.Post).filter(models.Post.id==id)
    #post=post_query.first()
#
    #if post==None:
    #    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id: {id} was not exist")
    
    ##post_query.update({"title":"this update message","content":"i love this game"},synchronize_session=False)
   # post_query.update(update_post.dict(),synchronize_session=False)
   # db.commit()
    ##return{"data":post_query.first()}
    #return post


#@app.post("/users",status_code = status.HTTP_201_CREATED,response_model=schemas.UserOut)
#def creat_users(user:schemas.UserCreat,db: Session = Depends(get_db)):
#    hashed_password=utils.hash(user.password)
#    user.password=hashed_password
#    new_users=models.User(**user.dict())
#    db.add(new_users)
#    db.commit()
#    db.refresh(new_users)
#    return new_users
#
#@app.get('/users/{id}',response_model=schemas.UserOut)
#def get_user(id:int,db: Session = Depends(get_db)):
#    user=db.query(models.User).filter(models.User.id==id).first()
#
#    if not user:
#        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"user with id: {id} was not exist")
#    return user