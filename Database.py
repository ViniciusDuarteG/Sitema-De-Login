import sqlite3

conn = sqlite3.connect('AuditoriaSystem.DB')

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Users(
    Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    NAME TEXT NOT NULL,   
    EMAIL TEXT NOT NULL,
    USER TEXT NOT NULL,
    PASSWORD TEXT NOT NULL           
);
""")

print("Connect sucessfull")

