from flask import Flask, render_template
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
login = LoginManager(app)

from app_pkg.bp_songs import bp as songs_bp
app.register_blueprint(songs_bp, url_prefix=f"{app.config['PREFIX']}/songs")
from app_pkg.bp_api import bp as api_bp
app.register_blueprint(api_bp, url_prefix=f"{app.config['PREFIX']}/api")
from app_pkg.bp_mis import bp as mis_bp
app.register_blueprint(mis_bp, url_prefix=f"{app.config['PREFIX']}/mis")
from app_pkg.bp_auth import bp as auth_bp
app.register_blueprint(auth_bp, url_prefix=f"{app.config['PREFIX']}/auth")

# https://abstractkitchen.com/blog/how-to-create-custom-jinja-filters-in-flask/
def replace_double_quotes(value):
  if value:
    return value.replace('"', "'")
  else:
    return value
app.jinja_env.filters['replace_double_quotes'] = replace_double_quotes

def replace_newlines(value):
  if value:
    return value.replace('\n', ' ')
  else:
    return value
app.jinja_env.filters['replace_newlines'] = replace_newlines

@app.route(f"{app.config['PREFIX']}/")
def home_view():
  return render_template('home.html')