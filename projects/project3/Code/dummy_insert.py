from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Vocabulary, Base

# create an engine and session
engine = create_engine('sqlite:///vocab_app.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

# create some dummy data for the Vocabulary table
dummy_data = [
    {'lesson': 1, 'part_of_lesson': 1, 'katakana': 'ア', 'hiragana': 'あ', 'definition': 'a'},
    {'lesson': 1, 'part_of_lesson': 2, 'katakana': 'イ', 'hiragana': 'い', 'definition': 'i'},
    {'lesson': 1, 'part_of_lesson': 3, 'katakana': 'ウ', 'hiragana': 'う', 'definition': 'u'},
    {'lesson': 1, 'part_of_lesson': 4, 'katakana': 'エ', 'hiragana': 'え', 'definition': 'e'},
    {'lesson': 1, 'part_of_lesson': 5, 'katakana': 'オ', 'hiragana': 'お', 'definition': 'o'},
]
# insert the dummy data into the Vocabulary table
for data in dummy_data:
    vocab = Vocabulary(**data)
    session.add(vocab)
# commit the changes to the database
session.commit()
