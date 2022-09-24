import sqlalchemy

from sqlalchemy.orm import sessionmaker

from Models2 import create_tables, Publisher, Book,  Stock, Sale, Shop

DSN = 'postgresql://postgres:dima1983@localhost:5432/homework'
engine = sqlalchemy.create_engine(DSN )

# create_tables(engine)

Session = sessionmaker(bind = engine)
session = Session()


number_id_publisher = int(input('Введите ID: '))
for i in session.query(Publisher).filter(Publisher.id == number_id_publisher).all():
    print(i)

session.close