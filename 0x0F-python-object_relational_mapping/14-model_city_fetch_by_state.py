#!/usr/bin/python3
""" """

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sqlalchemy
from model_city import City

if __name__ == "__main__":
    en = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                                                                   argv[2],
                                                                   argv[3]))
    Base.metadata.create_all(en)
    Session = sessionmaker(bind=en)
    session = Session()

    first = session.query(City, State).filter(City.state_id == State.id)\
                                      .order_by(City.id).all()
    for ct, st in first:
        print("{}: ({}) {}".format(st.name, ct.id, ct.name))
    session.close()
