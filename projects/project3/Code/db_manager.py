from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound

from models import Users, Base, Vocabulary, UserStats
from secure_password import check_password


def create_base():
    engine = create_engine('sqlite:///vocab_app.db')
    Base.metadata.bind = engine
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)
    my_session = session()
    print(Base.metadata.tables.keys())
    print(engine.connect())
    return None


class database_handler:
    def __init__(self, dbname):
        self.session = None
        engine = create_engine(f"sqlite:///{dbname}")
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def close(self):
        self.session.close()

    def insert_user(self, email, username, password):
        if not self.session.query(Users).filter_by(email=email).first():
            new_user = Users(email=email, username=username, password=password)
            self.session.add(new_user)
            self.session.commit()
            print("User registered")
        else:
            print("User already exists")

    def check_user(self, email):
        try:
            user = self.session.query(Users).filter_by(email=email).one()
            return True
        except NoResultFound:
            return False

    def login_check(self, username, password):
        user = self.session.query(Users).filter_by(username=username).first()
        if not user:
            return False

        return bool(check_password(password, user.password))

    def get_vocab(self):
        vocab = self.session.query(Vocabulary).all()
        return vocab

    def insert_vocab(self, lesson, part, hiragana, katakana, definition):
        exists = self.session.query(Vocabulary).filter_by(hiragana=hiragana).exists()
        if exists is True:
            print("Vocab already exists")
            return False
        else:
            new_vocab = Vocabulary(lesson=lesson, part_of_lesson=part, hiragana=hiragana, katakana=katakana,
                                   definition=definition)
            self.session.add(new_vocab)
            self.session.commit()
            print("Vocab added")
            return None

    def update_vocab(self, lesson, part, hiragana, katakana, definition):
        vocab = self.session.query(Vocabulary).filter_by(hiragana=hiragana).first()
        vocab.lesson = lesson
        vocab.part = part
        vocab.hiragana = hiragana
        vocab.katakana = katakana
        vocab.definition = definition
        self.session.commit()
        return None

    def delete_vocab(self, vocab_id):
        vocab = self.session.query(Vocabulary).filter_by(id=vocab_id).first()
        self.session.delete(vocab)
        self.session.commit()
        return None

    def get_vocab_by_id(self, vocab_id):
        if self.session.query(Vocabulary).filter_by(id=vocab_id).first() is None:
            return None
        else:
            return self.session.query(Vocabulary).filter_by(id=vocab_id).first()

    def get_vocab_by_lesson_and_part(self, lesson, part):
        vocab = self.session.query(Vocabulary).filter_by(lesson=lesson, part_of_lesson=part).all()
        return vocab

    def update_user_stats(self, user_id, vocab_id, point_change):
        user_stats = self.session.query(UserStats).filter_by(user_id=user_id, vocabulary_id=vocab_id).first()
        print(f"User stats: {user_stats}")
        if user_stats is None:
            new_user_stats = UserStats(user_id=user_id, vocabulary_id=vocab_id, points=100)
            new_user_stats.points += point_change
            self.session.add(new_user_stats)
            self.session.commit()
        else:
            user_stats.points += point_change
            self.session.commit()
        return None

    def get_vocab_by_user_stats(self, user_id):
        # get all vocabs from user stats where user_id = user_id sort by points ascending
        vocab = self.session.query(Vocabulary).join(UserStats).filter(UserStats.user_id == user_id).order_by(
            UserStats.points).all()
        return vocab

    def username_exists(self, username):
        if self.session.query(Users).filter_by(username=username).first() is None:
            return False
        else:
            return True

    def email_exists(self, email):
        if self.session.query(Users).filter_by(email=email).first() is None:
            return False
        else:
            return True

create_base()
test = database_handler("vocab_app.db")
print(test.check_user("haha@haha.com"))
