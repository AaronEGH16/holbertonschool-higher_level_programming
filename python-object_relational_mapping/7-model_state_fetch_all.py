#!/usr/bin/python3
"""
This module uses SqlAlchemy to make a connection to
DataBase and print all table content in format "id: name"
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":

    user = argv[1]
    passwd = argv[2]
    database = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(user, passwd, database), pool_pre_ping=True)

    session = Session(engine)

    for row in session.query(State).order_by(State.id):
        print("{}: {}".format(row.id, row.name))

    session.close()
