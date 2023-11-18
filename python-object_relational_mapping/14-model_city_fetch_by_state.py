#!/usr/bin/python3
"""
This module uses SqlAlchemy to make a connection to
Database and join two tables to print all the elements they contain
in format "{state.name}: ({city.id}) city.name"
"""
from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


if __name__ == "__main__":

    user = argv[1]
    passwd = argv[2]
    database = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(user, passwd, database), pool_pre_ping=True)

    session = Session(engine)

    sql = session.query(State, City).\
        filter(City.state_id == State.id).\
        order_by(City.id).all()

    for state, city in sql:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
