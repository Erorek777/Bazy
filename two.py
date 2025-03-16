import pyodbc
import os
from dotenv import load_dotenv

load_dotenv()
# for d in pyodbc.drivers():
#     print(d)
# print(os.environ.get('DATABASE_PASSWORD'))
database_password = os.environ.get('DATABASE_PASSWORD')
suszi_login = 'krmazurb'
server = 'morfeusz.wszib.edu.pl'

connection_string = (
'DRIVER={ODBC Driver 17 for SQL Server};'
f'SERVER={server};'
f'DATABASE={suszi_login};' # database
f'UID={suszi_login};' #user id
f'PWD={database_password};'
'Ecrypt=no'
)
connection = pyodbc.connect(connection_string)

# start tranzakcji 1
# connection.execute("CREATE TABLE users(id int identity, name varchar(255), age int)")
# start tranzakcji 1
# connection.execute("INSERT INTO users(name, age) values ('Andrzej', 18), ('Maciej', 30)")
# connection.commit()
 # tranzakcja2 bez komita
# connection.execute("INSERT INTO users(name, age) values ('Jan', 30)")


cursor = connection.cursor()

# cursor.execute("select * from users")


# for row in cursor:
#     print(row)

# for user_id, name, age in cursor:
#     print(user_id, name, age, sep='\n')

# results = cursor.fetchall()
# print(results)

# print(cursor.fetchone())  #iteruje o jeden po kursorze
# print(cursor.fetchone())
# results = cursor.fetchall()
# results = cursor.fetchmany(2)
# print(results)


# for row in results:
#     print(row)

#
# for row in results:
#     print(row)

new_name = input("Podaj nowe Imie: ")
old_name = input("Podaj stare Imie: ")

cursor.execute(f"UPDATE users SET name=? WHERE name =?",  (new_name, old_name))
connection.commit()
print(f'{cursor.rowcount} wiersz zmieniony')

# cursor.execute("SELECT name FROM users")
#     # print(row)
# print(cursor.fetchall())


# cursor.close()
# connection.close()



