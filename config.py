import os

server = 'servsrv\mssql2016'
database = 'MIS'
user = os.environ['SERVDBUSER']
passw = os.environ['SERVDBPASS']

class Config:
  SQLALCHEMY_DATABASE_URI = f'mssql+pyodbc://{user}:{passw}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server'
