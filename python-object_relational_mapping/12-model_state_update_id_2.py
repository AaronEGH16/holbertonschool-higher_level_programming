#!/usr/bin/python3
"""
This module uses SqlAlchemy to make a connection to
DataBase, update state name with id=2 to "New Mexico"
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

    updte = session.query(State).filter_by(id=2).first()
    updte.name = "New Mexico"
    session.commit()

    session.close()
