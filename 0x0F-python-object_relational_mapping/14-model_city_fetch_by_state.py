#!/usr/bin/python3
"""Script prints all City objects
"""
from sqlalchemy import (create_engine)
from sqlalchemy.orm import aliased, sessionmaker
from model_state import Base, State
from model_city import City
from sys import argv

if __name__ == "__main__":
    Session = sessionmaker()
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                           argv[1], argv[2], argv[3]), pool_pre_ping=True)
    session = Session(bind=engine)
    Base.metadata.create_all(engine)
    for instance in session.query(State).order_by(State.id):
        print("{}: {}".format(instance.id, instance.name))
    session.close()
