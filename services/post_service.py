from fastapi import Depends

from database.session import Session, get_db
from models import Post
from repository.post_repository import PostRepository
from schemas.post_schema import PostCreate


class PostService:

    def __init__(self, db: Session):
        self.db = db

    repository = PostRepository(Session)

    def get_all_posts(self):
        return self.repository.get_all_posts()

    def get_post_by_id(self, post_id: int):
        return self.repository.get_post_by_id(post_id)

    def create_post(self, post: PostCreate):
        return self.repository.create_post(post)

    def update_post(self, post_id: int, post: PostCreate):
        return self.repository.update_post(post_id, post)

    def delete_post(self, post_id: int):
        return self.repository.delete_post(post_id)

    def like_post(self, post_id: int):
        return self.repository.like_post(post_id)

    def unlike_post(self, post_id: int):
        return self.repository.unlike_post(post_id)
