#!/usr/bin/python3

import MySQLdb

data_base = MySQLdb.connect(host="localhost", port="3306", user="", passwd="", data_base="hbtn_0e_0_usa")
cursor = data_base.cursor()

cursor.execute("SELECT * FROM states ORDER BY ASC states.id")
res = cursor.fetchall()

for row in res:
    print row

cursor.close()
data_base.close()
