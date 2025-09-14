from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi_service.app.config.database import get_db
from fastapi_service.app.schemas.post_schema import PostCreate, PostResponse
from fastapi_service.app.services import post_service

router = APIRouter(prefix="/posts", tags=["posts"])


@router.post("/", response_model=PostResponse)
def create_post(post: PostCreate, db: Session = Depends(get_db)):
    return post_service.create_post(db, post)


@router.get("/", response_model=list[PostResponse])
def read_posts(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return post_service.list_posts(db, skip, limit)


@router.get("/{post_id}", response_model=PostResponse)
def read_post(post_id: int, db: Session = Depends(get_db)):
    return post_service.get_post_by_id(db, post_id)


@router.put("/{post_id}", response_model=PostResponse)
def update_post(post_id: int, post: PostCreate, db: Session = Depends(get_db)):
    return post_service.update_post(db, post_id, post)


@router.delete("/{post_id}", response_model=PostResponse)
def delete_post(post_id: int, db: Session = Depends(get_db)):
    return post_service.delete_post(db, post_id)
