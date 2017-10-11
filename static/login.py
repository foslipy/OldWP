import sqlite3

conn = sqlite3.connect('User.db')
print "Opened database successfully";

conn.execute('CREATE TABLE Users(USERNAME TEXT PRIMARY KEY NOT NULL, PASSWORD TEXT NOT NULL)')
print "Table created successfully";
conn.close()
