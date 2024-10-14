from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import os
import time
import logging

logging.basicConfig(level=logging.DEBUG)

print("Starting...")

DB_USER = os.getenv('POSTGRES_USER')
DB_PASS = os.getenv('POSTGRES_PASSWORD')
DB_HOST = os.getenv('POSTGRES_HOST')
DB_NAME = os.getenv('POSTGRES_DB')

def main():
    try:
        connect_str = f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}'
        logging.info(connect_str)

        engine = create_engine(connect_str)

        Base = declarative_base()
        class User(Base):
            __tablename__ = 'users'

            id = Column(Integer, primary_key=True)
            name = Column(String)
            email = Column(String)

        Base.metadata.create_all(engine)

        Session = sessionmaker(bind=engine)
        session = Session()

        new_user = User(name='John Doe', email='john@example.com')
        session.add(new_user)
        session.commit()

    except Exception as ex:
        logging.error('error while connect db')
        raise ex

    while True:
        logging.info('work work work')
        time.sleep(1)

if __name__ == "__main__":
   main()
   
