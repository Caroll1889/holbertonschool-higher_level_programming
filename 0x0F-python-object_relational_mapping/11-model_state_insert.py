#!/usr/bin/python3
""" """

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sqlalchemy

if __name__ == "__main__":
    en = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                                                                   argv[2],
                                                                   argv[3]))
    Base.metadata.create_all(en)
    Session = sessionmaker(bind=en)
    session = Session()
    new = State(name='Louisiana')
    session.add(new)

    first = session.query(State).filter_by(name='Louisiana').first()
    print(first.id)
    session.commit()
    session.close()
