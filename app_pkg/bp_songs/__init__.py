from flask import Blueprint

bp = Blueprint('songs', __name__, template_folder='templates')

from app_pkg.bp_songs import routes