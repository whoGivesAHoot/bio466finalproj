#!/usr/bin/env python3
import pymysql
import cgi, cgitb

cgitb.enable();

db = pymysql.connect(host="localhost",  # your host
                     user="ballarmi",       # username
                     passwd="bio466",     # password
                     db="ballarmi")   # name of the database

# Create a Cursor object to execute queries.
cur = db.cursor()

# Select data from table using SQL query.
cur.execute("SELECT * FROM hbonds")

# Start webpage
print ("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<head>")
print ("<title>Form Results</title>")
print ("</head>")
print ("<body>")

# print the first, second, and third columns to a table
print ("<table border=1 cellspacing=0 cellpadding=3><tr><th>frame</th><th>donor_index</th><th>hydrogen_index</th><th>acceptor</th><th>distance</th><th>angle</th></tr>")
for row in cur.fetchall() :
    print ("<tr><td>" + str(row[0]) + "</td><td>" + str(row[1]) + "</td><td>"  + str(row[2]) + "</td><td>" + str(row[3]) + "</td><td>" + str(row[4]) + "</td><td>" + str(row[5]) + "</td></tr>")

print ("</table>")

cur.close()
del cur
db.close()

print ("</body>")
print ("</html>")
