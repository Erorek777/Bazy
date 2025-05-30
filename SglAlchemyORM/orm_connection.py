import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.schema import CreateSchema
from alchemy_orm import Base

load_dotenv()

database_password = os.environ.get('DATABASE_PASSWORD')
suszi_login = 'krmazurb'
server = 'morfeusz.wszib.edu.pl'
driver = 'ODBC+Driver+17+for+SQL+Server'

# dialect+driver://username:password@host:port/database?dodtkowe_opcje_klucz_wartość
engine = create_engine(
    f'mssql+pyodbc://{suszi_login}:{database_password}@{server}/{suszi_login}?driver={driver}&Encrypt=no',
    echo=False
)

Session = sessionmaker(engine)

if __name__ == '__main__':
    session = Session()
    # session.execute(CreateSchema('library_orm'))
    session.commit()

    Base.metadata.create_all(engine)

