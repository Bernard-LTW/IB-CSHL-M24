import sqlalchemy as db
from sqlalchemy.orm import Session
from db_models import Base, Users, Post
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from secure_password import hash_password, check_password



class DBHandler:
    def __init__(self,path):
        self.engine = db.create_engine(path, echo=False)
        self.session = Session(self.engine)
    def create_user(self,username, password):
        if not self.session.query(Users).filter_by(username=username).first():
            new_user = Users(username=username, password=hash_password(password))
            self.session.add(new_user)
            self.session.commit()
            print("User registered")
            return True
        else: return False

    def check_user(self,username):
        return bool(self.session.query(Users).filter_by(username=username).first())


    def login(self,username, password):
        user = self.session.query(Users).filter_by(username=username).first()
        if not user:
            return False
        return bool(check_password(password, user.password))

    def create_post(self,title, content, code, language, username):
        user = self.session.query(Users).filter_by(username=username).first()
        new_post = Post(title=title, content=content, code=code, user_id=user.id,datetime_posted=datetime.now(),code_language=language)
        self.session.add(new_post)
        self.session.commit()

    def get_users(self):
        return self.session.query(Users).all()

    def get_posts(self):
        posts = self.session.query(Post).all()
        for post in posts:
            user = self.session.query(Users).filter_by(id=post.user_id).first()
            print(f"post {post.id} belongs to user {user.username} with id {user.id}")
            post.username = user.username
            #post.datetime_posted = post.datetime_posted.strftime("%d/%m/%Y %H:%M")
        posts.reverse()
        return posts

    def get_own_posts(self, username):
        user = self.session.query(Users).filter_by(username=username).first()
        print(f"selecting posts from user {user.username} with id {user.id}")
        posts = self.session.query(Post).filter_by(user_id=user.id).all()
        #print(f"posts: {posts[0].code}")
        for post in posts:
            post.username = user.username
            #post.datetime_posted = post.datetime_posted.strftime("%d/%m/%Y %H:%M")
        posts.reverse()
        return posts

    def delete_post(self, post_id):
        post = self.session.query(Post).filter_by(id=post_id).first()
        self.session.delete(post)
        self.session.commit()
        return

    def add_like(self, post_id):
        post = self.session.query(Post).filter_by(id=post_id).first()
        post.like_count += 1
        self.session.commit()
        return

    def remove_like(self, post_id):
        post = self.session.query(Post).filter_by(id=post_id).first()
        post.like_count -= 1
        self.session.commit()
        return

    def get_sorted_posts(self, sort_by):
        posts = None
        if sort_by == "time":
            posts = self.session.query(Post).order_by(Post.datetime_posted.desc()).all()
        elif sort_by == "likes":
            posts = self.session.query(Post).order_by(Post.like_count.desc()).all()
        if posts:
            for post in posts:
                user = self.session.query(Users).filter_by(id=post.user_id).first()
                post.username = user.username
                #post.datetime_posted = post.datetime_posted.strftime("%d/%m/%Y %H:%M")
            return posts

    def get_user(self, username):
        user = self.session.query(Users).filter_by(username=username).first()
        return user

    def get_user_stats(self, username):
        user = self.session.query(Users).filter_by(username=username).first()
        posts = self.session.query(Post).filter_by(user_id=user.id).all()
        return len(posts), sum(post.like_count for post in posts)

    def get_password(self, username):
        user = self.session.query(Users).filter_by(username=username).first()
        return user.password

    def change_password(self, username, new):
        user = self.session.query(Users).filter_by(username=username).first()
        user.password = hash_password(new)
        self.session.commit()
        return

    def edit_post(self, post_id, title, content, code, language):
        post = self.session.query(Post).filter_by(id=post_id).first()
        post.title = title
        post.content = content
        post.code = code
        post.code_language = language
        self.session.commit()
        return

    def get_post(self, post_id):
        post = self.session.query(Post).filter_by(id=post_id).first()
        return post



