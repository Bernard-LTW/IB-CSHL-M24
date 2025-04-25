import sqlite3

#connect to file
connection = sqlite3.connect('login_database.db')

#get the cursor to the database
cursor = connection.cursor()

#ready to add sql commands
query = f"CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, email TEXT NOT NULL unique , username TEXT NOT NULL , password TEXT NOT NULL )"

#execute the query
cursor.execute(query)

#commit the changes
connection.commit()

#close the connection
connection.close()
