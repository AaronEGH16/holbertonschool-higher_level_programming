#!/usr/bin/python3
"""
This module contains a program to connect to a database and print all rows.
When "name" starts with "N"
"""
from sys import argv
import MySQLdb


if __name__ == "__main__":

    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=mysql_username,
                         passwd=mysql_password,
                         db=database_name)

    cur = db.cursor()
    cur.execute("SELECT * FROM states\
                WHERE name LIKE \"N%\"\
                ORDER BY id ASC")
    for row in cur:
        print(row)
    cur.close()
    db.close()
