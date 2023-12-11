import os

server = 'servsrv\mssql2016'
database = 'MIS'
user = os.environ['SERVDBUSER']
passw = os.environ['SERVDBPASS']

uname = os.popen('uname').read()

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
  CURR_ARCH = ''
  if uname.startswith('Darwin'):
    CURR_ARCH = 'mac'
    # four slashes when using absolute paths
    SQLALCHEMY_DATABASE_URI = 'sqlite:////Users/agou/Library/Mobile Documents/com~apple~CloudDocs/Diafora/alexdb.sqlite3'
  else:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')

  SQLALCHEMY_BINDS = {'mis': f'mssql+pyodbc://{user}:{passw}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server',}
  
  SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

  PREFIX = '/flask'
  