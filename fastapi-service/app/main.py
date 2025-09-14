from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.controller.PostController import PostController
from app.repository import post_repository
from app.config.database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post("/posts/", response_model=post_repository.Post)
def create_post(post: post_repository.PostCreate, db: Session = Depends(get_db)):
    return PostController.create_post(db=db, post=post)


@app.get_posts("/posts/", response_model=list[post_repository.Post])
def read_posts(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    posts = PostController.get_posts(db, skip=skip, limit=limit)
    return posts


@app.get_posts("/posts/{post_id}", response_model=post_repository.Post)
def read_post(post_id: int, db: Session = Depends(get_db)):
    db_post = PostController.get_post(db, post_id=post_id)
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return db_post


@app.put("/posts/{post_id}", response_model=post_repository.Post)
def update_post(post_id: int, post: post_repository.PostCreate, db: Session = Depends(get_db)):
    db_post = PostController.update_post(db, post_id=post_id, post=post)
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return db_post


@app.delete("/posts/{post_id}", response_model=post_repository.Post)
def delete_post(post_id: int, db: Session = Depends(get_db)):
    db_post = PostController.delete_post(db, post_id=post_id)
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return db_post
