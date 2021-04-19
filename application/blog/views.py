from flask import Blueprint, request

from application import api, Resource
from .models import db, Post, PostSchema

blog = Blueprint("blog", __name__)

post_schema = PostSchema()
posts_schema = PostSchema(many=True)

class PostListResource(Resource):
    """
        Obtenir tous les posts
    """
    def get(self):
        posts = Post.query.order_by(Post.date).all()
        return posts_schema.dump(posts)

    def post(self):
        """
            Créer un post
        """
        new_post = Post(
            title=request.json["title"],
            author=request.json["author"],
            content=request.json["content"],
            date=request.json["date"]
        )
        db.session.add(new_post)
        db.session.commit()
        return post_schema.dump(new_post)

api.add_resource(PostListResource, "/posts/")


class PostResource(Resource):
    def get(self, post_id):
        """
            Obtenir un post dans la base de données
        """
        post = Post.query.get_or_404(post_id)
        return post_schema.dump(post)

    def patch(self, post_id):
        """
            Modifier un post 
        """
        post = Post.query.get_or_404(post_id)
        if "title" in request.json:
            post.title = request.json["title"]
        if "author" in request.json:
            post.author = request.json["author"]
        if "content" in request.json:
            post.content = request.json["content"]
        if "date" in request.json:
            post.date = request.json["date"]
        db.session.commit()
        return post_schema.dump(post)

    def delete(self, post_id):
        """
            Suppression d'un post
        """
        post = Post.query.get_or_404(post_id)
        db.session.delete(post)
        db.session.commit()
        return "", 204

api.add_resource(PostResource, "/posts/<int:post_id>/")