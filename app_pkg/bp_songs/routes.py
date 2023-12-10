from flask import render_template
from app_pkg.bp_songs import bp
from app_pkg.bp_songs.models import Tblsongs

@bp.route('/')
def songs_view():
  songs = Tblsongs.query.all()
  # https://blog.miguelgrinberg.com/post/beautiful-flask-tables-part-2
  return render_template('songs_gridjs.html', records=songs)
