from flask import render_template, redirect, url_for
from app_pkg.bp_songs import bp
from app_pkg.bp_songs.models import Tblsongs
from app_pkg.bp_songs.forms import SongForm
from app_pkg import db
from flask_login import login_required

@bp.route('/all_songs')
def songs_view():
  songs = Tblsongs.query.all()
  # https://blog.miguelgrinberg.com/post/beautiful-flask-tables-part-2
  return render_template('songs_gridjs.html', records=songs)

@bp.route('/all_songs_with_api')
@login_required
def songs_with_api_view():
  return render_template('songs_gridjs_api.html')

@bp.route('/new_song', methods=['GET', 'POST'])
def new_song_view():
  form = SongForm()
  if form.validate_on_submit():
    song = Tblsongs(title=form.title.data, artist=form.artist.data,
      album=form.album.data, composer=form.composer.data, comment=form.comment.data)
    db.session.add(song)
    db.session.commit()
    return redirect(url_for('songs.songs_view'))
  return render_template('new_song.html', form=form)
