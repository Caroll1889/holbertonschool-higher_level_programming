#!/usr/bin/python3
""" """

from sys import argv
import MySQLdb

if __name__ == "__main__":

    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], 
                         state name searched=argv[4])
    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name LIKE '{:s}' ORDER BY id ASC"
                .format(argv[4]))
    res = cur.fetchall()

    for row in res:
        print(row)
    db.close()
