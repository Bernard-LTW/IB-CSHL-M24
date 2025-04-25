from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from secure_password import check_password, encrypt_password
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.datatables import MDDataTable

Base = declarative_base()
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


class TableScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data_table = MDDataTable(
            size_hint=(0.8, 0.5),
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            use_pagination=True,
            check=True,
            column_data=[("ID", 40), ("Sender_ID", 40), ("Receiver_ID", 40), ("Amount", 30), ("Signature", 100)],
            row_data=[]
        )
        self.data_table.bind(on_row_press=self.on_row_press)
        self.data_table.bind(on_check_press=self.on_check_press)
        self.add_widget(self.data_table)

    def on_pre_enter(self, *args):
        self.load()

    def on_row_press(self, table, row):
        print(f"Row was pressed. Data is: {row.text}")

    def on_check_press(self, table, current_row):
        print(f"Row {current_row} was checked")

    def save(self):
        print("Trying to save new Tx...")
        sender = self.ids.sender.text
        receiver = self.ids.receiver.text
        amount = self.ids.amount.text
        if sender == "" or receiver == "" or amount == "":
            print("Error: Empty field!")
            return
        else:
            sender = int(sender)
            receiver = int(receiver)
            amount = int(amount)
            signature = encrypt_password(f"sender_id {sender},receiver_id {receiver},amount {amount}")
            new_tx = ledger(sender_id=sender, receiver_id=receiver, amount=amount, signature=signature)
            session.add(new_tx)
            session.commit()
            print("New tx saved")
            self.load()

    def load(self):
        print("Trying to load all Tx...")
        self.data_table.row_data.clear()
        rows = session.query(ledger).all()
        for row in rows:
            row = [row.id, row.sender_id, row.receiver_id, row.amount, row.signature]
            if row not in self.data_table.row_data:
                self.data_table.row_data.append(row)


    def delete(self):
        print("Trying to delete selected Tx...")
        checked = self.data_table.get_row_checks()
        for row in checked:
            row = row[0]
            session.query(ledger).filter(ledger.id == row).delete()
            session.commit()
            print(f"Tx(id={row}) deleted")
            self.load()
class table_example(MDApp):
    def build(self):
        pass


boi = table_example()
boi.run()