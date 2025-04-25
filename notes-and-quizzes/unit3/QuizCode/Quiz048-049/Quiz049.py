#2023-02-23 Quiz049
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from secure_password import check_password

Base = declarative_base()

red = "\33[0;31m"
green = "\33[0;32m"
end = "\33[0m"

temp = 0
class ledger(Base):
    __tablename__ = 'ledger'
    id = Column(Integer, primary_key=True)
    sender_id = Column(Integer, nullable=False)
    receiver_id = Column(Integer, nullable=False)
    amount = Column(Integer, nullable=False)
    signature = Column(String, nullable=False)

engine = create_engine(f"sqlite:///bitcoin_exchange.db")
Session = sessionmaker(bind=engine)
session = Session()
rows = session.query(ledger).all()
for row in rows:
    unhashed = f"id {row.id},sender_id {row.sender_id},receiver_id {row.receiver_id},amount {row.amount}"
    if check_password(row.signature, unhashed):
        temp += row.amount

print(f"{green}Total amount of valid bitcoin transferred: {temp}{end}")