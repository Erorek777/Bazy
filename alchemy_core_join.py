import os

from dotenv import load_dotenv
from sqlalchemy import *
from sqlalchemy import create_engine

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

metadata = MetaData()

worker_table = Table('workers', metadata,
                     Column('pesel', String(11), primary_key=True),
                     Column('first_name', String(255), nullable=False),
                     Column('last_name', String(255), nullable=False),
                     Column('birthday', Date, nullable=False),
                     Column('address_id', Integer,ForeignKey('address.address_id')),
                     )
address_table = Table('address', metadata,
                      Column('address_id', Integer, primary_key=True),
                      Column('country', String(255), nullable=False),
                      Column('city', String(255), nullable=False),
                      Column('street', String(255), nullable=False),
                      Column('postal_code', String(255), nullable=False),
                      )

connection = engine.connect()

# print(metadata.tables)

#Łączenie table przez klucz obcy

if __name__ == '__main__':
    query = select(worker_table.join(address_table))
    result = connection.execute(query)
    print(worker_table.join(address_table))
    print(result.fetchall())

# Złączenie +konkretne kolumny   Tylko pesel i państwo
query = select(worker_table.c.pesel, address_table.c.country)\
    .select_from(worker_table.join(address_table))
result = connection.execute(query)
print(result.fetchall())

# Złączenie +konkretne kolumny - 2 przyklad
query = select(worker_table.c.pesel, address_table.c.country)\
    .join_from(worker_table, address_table)
result = connection.execute(query)
print(result.fetchall())

# Złączenie +konkretne kolumny - 3 przyklad  - wpisujemy drugą lub pierwszą tebale a on sam się domysla drugie(tylko dwie)
query = select(worker_table.c.pesel, address_table.c.country)\
    .join(address_table)
result = connection.execute(query)
print(result.fetchall())

# Złączenie + ON
query = select(worker_table, address_table.c.country)\
    .join(address_table, worker_table.c.address_id == address_table.c.address_id)
result = connection.execute(query)
print(result.fetchall())

# Potwierdzenie że domyslne złączenie jest złoczeniem inerowym
query = select(worker_table, address_table.c.country) \
    .join(worker_table).where(worker_table.c.last_name == 'Kozłowski')
result = connection.execute(query)
print(result.fetchall())

# alis
w = worker_table.alias()
a = address_table.alias()

query = select(w, a.c.country) \
    .join(w)
result = connection.execute(query)
print(result.all())


#Left join
query = select(worker_table, address_table.c.country) \
   .join(address_table, isouter=True) \
   .where(worker_table.c.last_name == 'Kozłowski')
result = connection.execute(query)
print(result.all())

# full
query = select(func.year(worker_table.c.birthday), func.count().label("Liczba urodzonych w danym roku w Krakowie"))\
    .join(address_table)\
    .where(address_table.c.city == 'Kraków')\
    .group_by(func.year(worker_table.c.birthday))\
    .order_by(Column('Liczba urodzonych w danym roku w Krakowie').desc())\
    .having(func.count() > 1)
result = connection.execute(query)
print(result.fetchall())


insert_sgl = insert(address_table)\
    .values(country='Polska', city='Kraków', street='aleja Kijowska', postal_code='30-387')
connection.execute(insert_sgl)
connection.commit()

#INSERT
# insert_many = insert(worker_table)
# connection.execute(insert_many,[
#     {'pesel':'11111111', 'first_name': 'Nowy', 'last_name': 'Jeden', 'birthday': '2000-01-01',
#      'address_id': 1002},
#     {'pesel':'22222222', 'first_name': 'Nowy', 'last_name': 'Dwa', 'birthday': '2000-01-01',
#      'address_id': 1002}
# ])
# connection.commit()

#update
update.sql = update(worker_table).values(first_name='Zmienione').where(worker_table.c.address_id == 1002)
connection.execute(update.sql)
connection.commit()

#Delete
delete_sgl = delete(worker_table).where(worker_table.c.address_id == 1002)
connection.execute(delete_sgl)
connection.commit()

# Insert - 2
insert_sgl = insert(address_table)\
    .values(country='Polska', city='Kraków', street='aleja Kijowska', postal_code='30-387')
result = connection.execute(insert_sgl)

new_address_id = result.inserted_primary_key[0]

insert_many = insert(worker_table)
connection.execute(insert_many,[
     {'pesel':'1111111111', 'first_name': 'Nowy', 'last_name': 'Jeden', 'birthday': '2000-01-01',
      'address_id': new_address_id},
     {'pesel':'2222222222', 'first_name': 'Nowy', 'last_name': 'Dwa', 'birthday': '2000-01-01',
      'address_id': new_address_id}
 ])
connection.commit()



# Tu zaczyna się LAB 3

query = select(worker_table.c.country, address_table.c.city)\
    .join(address_table)\
    .where(address_table.c.city == 'Warszawa')
result = connection.execute(query)
print(result.fetchall())

query = select(worker_table.c.country, address_table.c.city)\
    .join(address_table)\
    .order_by(Column('name').desc())
result = connection.execute(query)
print(result.fetchall())

query = select(worker_table.c.country, address_table.c.city)\
    .join(address_table)\
    .order_by(Column('name').desc())
result = connection.execute(query)
print(result.fetchall())

query = select(worker_table.c.first_name, worker_table.c.birthday)\
    .join(address_table)\
    .order_by(Column('Data urodzenie').desc())
result = connection.execute(query)
print(result.fetchall())

query = select(worker_table.c.first_name, worker_table.c.last_name)\
    .join(address_table)\
    .worker_table.c.first_name.like('%A%M')

result = connection.execute(query)
print(result.fetchall())

























