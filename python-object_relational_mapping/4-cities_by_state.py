#!/usr/bin/python3
"""
This module contains a program to connect to a database and print all rows.
This code is safe of MySQL Injection.
This MySQL script lists all cities from the database.
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
    cur.execute("SELECT cities.id, cities.name, states.name\
                FROM cities JOIN states ON cities.state_id = states.id\
                ORDER BY cities.id ASC")
    for row in cur:
        print(row)
    cur.close()
    db.close()
