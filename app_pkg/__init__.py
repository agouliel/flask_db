from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

from app_pkg.bp_main import bp as main_bp
app.register_blueprint(main_bp)


