from fastapi import FastAPI
from database import engine
import models
from routers import user,post,auth,vote
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins=['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user.router)
app.include_router(post.router)
app.include_router(auth.router)
app.include_router(vote.router)


#uvicorn app.main:app --reload

@app.get("/")
async def root():
    return {"message": "Hello World!!!!,i love this game!!!"}