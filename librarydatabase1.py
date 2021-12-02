import sqlite3
connection = sqlite3.connect("librarybook1.db")
print("Database opened successfully")
cursor = connection.cursor()
#delete
connection.execute("create table book1 (id INTEGER PRIMARY KEY AUTOINCREMENT,pubisher TEXT NOT NULL, bookname TEXT NOT NULL, author TEXT NOT NULL, total INTEGER NOT NULL)")
print("Table created successfully")
connection.close()  
