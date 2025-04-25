from sqlalchemy import create_engine, ForeignKey,Column, String, Integer, CHAR
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()

class Person(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    address = Column(String(100))
    email = Column(String(50))

    def __init__(self, name, age, address, email):
        self.name = name
        self.age = age
        self.address = address
        self.email = email

    def __repr__(self):
        return f"{self.name} is {self.age} years old and lives at {self.address}"

engine = create_engine('sqlite:///people.db', echo=True)
Base.metadata.create_all(bind = engine)

Session = sessionmaker(bind=engine)
session = Session()

person = Person(name="John", age=25, address="123 Main St", email="john@email.com")
session.add(person)
session.commit()
