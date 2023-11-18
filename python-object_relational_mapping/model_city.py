#!/usr/bin/python3
"""
This module contains a class definition of
database table "states"
"""
from sqlalchemy import Column, ForeignKey, Integer, String
from model_state import Base, State


class City(Base):
    """
    Table cities:
        id = INT, AUTO INCREMENT, NOT NULL, PK
        name = CHAR(128), NOT NULL
        state_id = INT, NOT NULL, FK
    """

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)
