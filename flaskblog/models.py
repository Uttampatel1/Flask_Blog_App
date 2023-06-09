from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flaskblog import db , login_manager 
from flask import current_app
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.png')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    @staticmethod
    def search(query):
        words = query.split()
        filters = [Post.title.ilike(f'%{word}%') | Post.content.ilike(f'%{word}%') for word in words]
        return Post.query.filter(*filters).join(User).all()

    @staticmethod
    def latest_posts(limit=4):
        return Post.query.order_by(Post.date_posted.desc()).limit(limit).all()

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

# code Sqlite3 Commands

# with app.app_context():
#     db.create_all()

# user = User(username='Uttam',email = 'u@demo.com',password='password')
# db.session.add(user)
# db.session.commit()

#  User.query.all()
#  User.query.first()
#  User.query.filter_by(username='Uttam').all()
#  User.query.filter_by(username='Uttam').first()
#  user = User.query.filter_by(username='Uttam').first()
#  user = User.query.get(1)


