#!/usr/bin/python3
"""
This module contains a class definition of
database table "states"
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    Table states:
        id = INT, NOT NULL, PK
        name = CHAR(128), NOT NULL
    """

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
