from flask import Blueprint

bp = Blueprint('auth', __name__, template_folder='templates')

from app_pkg.bp_auth import routes