from sqlalchemy import create_engine, Integer, Column, text, String
from sqlalchemy.orm import declarative_base, sessionmaker


def get_mydb():
    engine = create_engine('mysql://root:liumiao271937@localhost:3306/shopping_serve?charset=utf8')
    Sesson = sessionmaker(bind=engine)
    sesson = Sesson()
    return sesson
