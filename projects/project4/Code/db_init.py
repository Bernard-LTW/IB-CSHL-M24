import sqlalchemy as db
from db_models import Base, Users, Post
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from db_manager import DBHandler
from secure_password import hash_password, check_password

db = DBHandler("sqlite:///social_media.sqlite")
## Create tables
Base.metadata.create_all(db.engine)
def dummy_insert_user():
    users = ["alice123", "bob123"]
    passwords = ["alice123", "bob123"]
    for user, password in zip(users, passwords):
        new_user = Users(username=user, password=hash_password(password))
        db.session.add(new_user)
    db.session.commit()

def dummy_insert_post():
    titles = ["First Post", "Second Post"]
    contents = ["This is my first post", "This is my second post"]
    codes = ["print('Hello World')", "SELECT * FROM users"]
    code_languages = ["python", "sql"]
    user_ids = [1, 2]
    for title, content, code, user_id,code_languages in zip(titles, contents, codes, user_ids,code_languages):
        new_post = Post(title=title, content=content, code=code, code_language = code_languages,user_id=user_id)
        db.session.add(new_post)
    db.session.commit()

dummy_insert_user()
dummy_insert_post()


