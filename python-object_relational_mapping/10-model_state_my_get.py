#!/usr/bin/python3
"""
This module uses SqlAlchemy to make a connection to
DataBase and print id of searched State name
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":

    user = argv[1]
    passwd = argv[2]
    database = argv[3]
    state_name = argv[4]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(user, passwd, database), pool_pre_ping=True)

    session = Session(engine)

    row = session.query(State).filter(State.name.like(state_name)).first()
    if row:
        print("{}".format(row.id))
    else:
        print("Not found")

    session.close()
