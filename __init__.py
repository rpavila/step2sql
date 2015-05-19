from schema import *

__author__ = 'rpavila'

if __name__ == "__main__":

    engine = create_engine('driver://user:password@host/dbname')
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

