from flask import Blueprint

bp = Blueprint('mis', __name__, template_folder='templates')

from app_pkg.bp_mis import routes