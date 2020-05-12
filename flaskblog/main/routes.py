from flask import render_template, request, Blueprint
from flaskblog.models import Post


main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    q = request.args.get('q')
    page = request.args.get('page', 1, type=int)
    if q:
        posts = Post.query.filter(Post.title.contains(q) | Post.content.contains(q)).paginate(page=page, per_page=5)
    else:
        posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    
    
    return render_template('home.html', posts=posts)


