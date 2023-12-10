from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

from app_pkg.bp_songs import bp as songs_bp
app.register_blueprint(songs_bp, url_prefix='/songs')

from app_pkg.bp_api import bp as api_bp
app.register_blueprint(api_bp, url_prefix='/api')

# https://abstractkitchen.com/blog/how-to-create-custom-jinja-filters-in-flask/
def replace_double_quotes(value):
  return value.replace('"', "'")
app.jinja_env.filters['replace_double_quotes'] = replace_double_quotes

def replace_newlines(value):
  if value:
    return value.replace('\n', ' ')
  else:
    return value
app.jinja_env.filters['replace_newlines'] = replace_newlines