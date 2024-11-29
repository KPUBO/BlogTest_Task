from fastapi import APIRouter, Depends

from database.session import Session, get_db
from schemas.post_schema import PostCreate
from services.post_service import PostService

router = APIRouter()


@router.get("/")
def get_posts(db: Session = Depends(get_db)):
    posts = PostService(db)
    return posts.get_all_posts()


@router.get("/{post_id}")
def get_post_by_id(post_id: int, db: Session = Depends(get_db)):
    posts = PostService(db)
    return posts.get_post_by_id(post_id)


@router.post("/")
def create_post(post: PostCreate, db: Session = Depends(get_db)):
    posts = PostService(db)
    return posts.create_post(post)


@router.delete("/{post_id}")
def delete_post(post_id: int, db: Session = Depends(get_db)):
    posts = PostService(db)
    return posts.delete_post(post_id)


@router.put("/{post_id}")
def update_post(post_id: int, post: PostCreate, db: Session = Depends(get_db)):
    posts = PostService(db)
    return posts.update_post(post_id, post)


@router.post("posts/{id}/like")
def like_post(post_id: int, db: Session = Depends(get_db)):
    posts = PostService(db)
    return posts.like_post(post_id)


@router.post("/posts/{id}/unlike")
def unlike_post(post_id: int, db: Session = Depends(get_db)):
    posts = PostService(db)
    return posts.unlike_post(post_id)
