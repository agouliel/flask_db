from flask import Blueprint

bp = Blueprint('api', __name__)

from app_pkg.bp_api import routes