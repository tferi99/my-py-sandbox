from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost/easytrader')
Session = sessionmaker(bind=engine)
session = Session()

result = session.execute(text("SELECT * FROM app_user"))
for row in result:
    print(row)
