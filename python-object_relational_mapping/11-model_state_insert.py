#!/usr/bin/python3
"""
This module uses SqlAlchemy to make a connection to
DataBase, add new state to them and print the new state id
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

    new = State(name="Louisiana")
    session.add(new)
    session.commit()

    print(new.id)

    session.close()
