import sqlite3

conn = sqlite3.connect('database.db')
print "Opened database successfully";

conn.execute('CREATE TABLE upcoming_workshop (name Text, cont INT, appdate Text, dept Text, duration Text, wtopic Text, followup1 Text, remark1 Text, followup2 Text, remark2 Text)')

conn.execute('CREATE TABLE free_workshop (srno Text,collegename TEXT, seminardate TEXT, hod TEXT, department TEXT, expectation TEXT, mail TEXT, reply TEXT, followup1 TEXT, remark1 TEXT, followup2 TEXT, remark2  TEXT )')

print "Table created successfully";
conn.close()
