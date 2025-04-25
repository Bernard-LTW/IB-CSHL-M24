import sqlite3

from kivymd.app import MDApp

from secure_password import encrypt_password, check_password
class database_worker:
    def __init__(self, name):
        self.connection = sqlite3.connect(name)
        self.cursor = self.connection.cursor()

    def search(self, query):
        result = self.cursor.execute(query).fetchall()
        return result

    def run_save(self, query):
        self.cursor.execute(query)
        self.connection.commit()

    def close(self):
        self.connection.close()


class quiz047(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.components = {"basic": 0}
        self.hash = ""


    def build(self):
        return
    def update(self):
        hash_string = ""
        base_widget = self.root.ids.base
        base = base_widget.text.strip()
        self.hash = ""
        if base:
            total = int(base)
            hash_string += f"base{total}"
            for id in ["inhabitant", "income_tax", "pension", "health"]:
                widget = self.root.ids[id]
                value = widget.text.strip()
                if value:
                    new_value = int(base) * int(value) // 100
                    value = f"{new_value} JPY"
                    self.root.ids[id + "_label"].text = value
                    total -= new_value
                    hash_string += f"{id}{value}"
                    self.root.ids.salary_label.text = f"{total} JPY"
                elif value == "":
                    new_value = ""
                    self.root.ids[id + "_label"].text = new_value

            self.hash = encrypt_password(f"{hash_string}")
            self.root.ids.hash_label.text = self.hash[-50:]
        else:
            return

    def save(self):
        base_widget = self.root.ids.base
        base = base_widget.text.strip()
        values = {
            "base": self.root.ids.base_label.text.strip()[:-4],
            "inhabitant": self.root.ids.inhabitant_label.text.strip()[:-4],
            "income_tax": self.root.ids.income_tax_label.text.strip()[:-4],
            "pension": self.root.ids.pension_label.text.strip()[:-4],
            "health": self.root.ids.health_label.text.strip()[:-4],
            "salary": self.root.ids.salary_label.text.strip()[:-4],
            "hash": self.hash,
        }

        query = "INSERT INTO payments (base, inhabitant, income_tax, pension, health, total, hash) VALUES (?, ?, ?, ?, ?, ?, ?)"
        db = database_worker("payments.db")
        try:
            db.cursor.execute(query, [values[key] for key in values.keys()])
            db.connection.commit()
            self.root.ids.hash_label.text = "Payment saved"
        except Exception as e:
            print(f"Error saving payment: {e}")
        finally:
            db.close()
    def clear(self):
        for label in ["base", "inhabitant", "income_tax", "pension", "health"]:
            self.root.ids[label].text = ""
            self.root.ids[label + "_label"].text = " JPY"
            self.hash = ""

        self.root.ids["salary_label"].text = " JPY"
        self.root.ids.hash_label.text = "----"


import sqlite3
from secure_password import check_password


def check_database_integrity(db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT id, base, inhabitant, income_tax, pension, health, total, hash FROM payments")
        rows = cursor.fetchall()

        for row in rows:
            (id, base, inhabitant, income_tax, pension, health, total, hash) = row
            to_hash = f"base{base}inhabitant{inhabitant}income_tax{income_tax}pension{pension}health{health}"
            if not check_password(hash, to_hash):
                print(f"Payment record {id} has been tampered with.")

        print("Database integrity check complete. No tampered payment records found.")

    except Exception as e:
        print(f"Error checking database integrity: {e}")

    finally:
        conn.close()


test = quiz047()
create = """CREATE TABLE if not exists payments(
     id         INTEGER primary key,
     base       INTEGER,
     inhabitant INTEGER,
     income_tax INTEGER,
     pension    INTEGER,
     health     INTEGER,
     total      INTEGER,
     hash       TEXT);"""
db = database_worker("payments.db")
db.run_save(create)
db.close()
check_database_integrity("payments.db")
test.run()
