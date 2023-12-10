from flask import render_template
from app_pkg.bp_songs import bp
from app_pkg.bp_songs.models import Tblsongs

@bp.route('/')
def index():
  songs = Tblsongs.query.all()
  return render_template('index.html', records=songs)

