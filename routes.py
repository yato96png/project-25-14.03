from flask import Blueprint, request, jsonify
from models import db, Post

bp = Blueprint('api', __name__)

@bp.route("/posts", methods=["GET"])
def get_posts():
    posts = Post.query.all()
    return jsonify([{"id": p.id, "content": p.content, "likes": p.likes, "reposts": p.reposts, "parent_id": p.parent_id} for p in posts])

@bp.route("/posts", methods=["POST"])
def create_post():
    data = request.json
    new_post = Post(content=data["content"], parent_id=data.get("parent_id"))
    db.session.add(new_post)
    db.session.commit()
    return jsonify({"message": "Post created"}), 201

@bp.route("/posts/<int:post_id>/like", methods=["POST"])
def like_post(post_id):
    post = Post.query.get(post_id)
    if not post:
        return jsonify({"error": "Post not found"}), 404
    post.likes += 1
    db.session.commit()
    return jsonify({"message": "Post liked"})

@bp.route("/posts/<int:post_id>/repost", methods=["POST"])
def repost_post(post_id):
    post = Post.query.get(post_id)
    if not post:
        return jsonify({"error": "Post not found"}), 404
    post.reposts += 1
    db.session.commit()
    return jsonify({"message": "Post reposted"})
