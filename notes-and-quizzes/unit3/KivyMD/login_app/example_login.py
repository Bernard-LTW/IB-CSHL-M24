#Login App

from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
import sqlite3
from secure_password import hash_password, check_password

class database_handler:
    def __init__(self,dbname):
        self.connection = sqlite3.connect(dbname)
        self.cursor = self.connection.cursor()

    def create_table(self):
        query = f"CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, email TEXT NOT NULL unique , username TEXT NOT NULL , password TEXT NOT NULL )"
        self.run_query(query)

    def run_query(self, query):
        self.cursor.execute(query)
        self.connection.commit()

    def close(self):
        self.connection.close()

    def insert_user(self, email, username, password):
        # Check if user exists in database and if not insert use
        if self.check_user(email) == False:
            query = f"INSERT into users (email, username, password) VALUES('{email}', '{username}', '{password}')"
            self.run_query(query)
            print("User registered")
        else:
            print("User already exists")

    def check_user(self, email):
        query = f"SELECT * from users WHERE email = '{email}'"
        self.run_query(query)
        if self.cursor.fetchone() is None:
            return False
        else:
            return True

    def login_check(self, username, password):
        query = f"SELECT * from users WHERE username = '{username}'"
        self.run_query(query)
        result = self.cursor.fetchone()
        if result is None:
            return False
        else:
            id, email, db_username, hashed_password = result
            if check_password(password, hashed_password):
                return True
            else:
                return False


class LoginScreen(MDScreen):
    def login(self):
        print(f"Username: {self.ids.uname.text} Password: {self.ids.pwd.text}")
        username = self.ids.uname.text
        password = self.ids.pwd.text
        if  example_login.db.login_check(username, password) == True:
            print("Login success")
        else:
            print("Login failed")
class RegisterScreen(MDScreen):
    def register(self):
        print(f"Username: {self.ids.uname.text} Email:{self.ids.email.text} Password: {self.ids.pwd.text}")
        uname  = self.ids.uname.text
        email = self.ids.email.text
        pwd = self.ids.pwd.text
        cpwd = self.ids.cpwd.text
        if pwd != cpwd:
            print("Passwords do not match")
            self.ids.cpwd.error = True
            self.ids.cpwd.md_bg_color = "red"
        else:
            pwd = hash_password(pwd)
            self.ids.cpwd.error = False
            self.ids.cpwd.md_bg_color = "green"
            db = database_handler("login_database.db")
            db.insert_user(email, uname, pwd)
            db.close()
            self.parent.current = "LoginScreen"






class example_login(MDApp):
    db = database_handler("login_database.db")
    db.create_table()
    def build(self):
        return


boi = example_login()
boi.run()