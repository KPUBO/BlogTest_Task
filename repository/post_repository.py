from datetime import datetime
from typing import List

from fastapi import HTTPException, Depends
from sqlalchemy import select

from database.session import Session, get_db
from models import Post
from schemas.post_schema import PostResponse, PostCreate


class PostRepository:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def get_all_posts(self) -> List[PostResponse]:
        posts_query = select(Post)

        return self.db.execute(posts_query).scalars().all()

    def get_post_by_id(self, post_id: int) -> PostResponse:
        post = self.db.query(Post).filter(Post.id == post_id).first()
        if post is None:
            raise HTTPException(status_code=404, detail="Post not found")
        return post

    def create_post(self, post_data: PostCreate) -> Post:
        new_post = Post(
            title=post_data.title,
            content=post_data.content,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )

        self.db.add(new_post)
        self.db.commit()
        self.db.refresh(new_post)

        return new_post

    def delete_post(self, post_id: int) -> None:
        post = self.get_post_by_id(post_id)
        self.db.delete(post)
        self.db.commit()

    def update_post(self, post_id: int, post_data: PostCreate) -> Post:
        post = self.get_post_by_id(post_id)

        post.title = post_data.title if post_data.title else post.title
        post.content = post_data.content if post_data.content else post.content
        post.updated_at = datetime.utcnow()

        self.db.commit()
        self.db.refresh(post)

        return post

    def like_post(self, post_id: int):
        post = self.get_post_by_id(post_id)
        post.amount_of_likes += 1
        post.updated_at = datetime.utcnow()

        self.db.commit()
        self.db.refresh(post)

        return post

    def unlike_post(self, post_id: int):
        post = self.get_post_by_id(post_id)
        post.amount_of_likes -= 1
        post.updated_at = datetime.utcnow()

        self.db.commit()
        self.db.refresh(post)

        return post
