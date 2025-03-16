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



# import os
#
# import pyodbc
#
# for driver in pyodbc.drivers():
#     print(driver)
# from dotenv import load_dotenv
# load_dotenv()
# print(os.environ.get('DATABASE_PASSWORD'))