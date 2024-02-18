from app_pkg.bp_api import bp
from app_pkg.bp_songs.models import Tblsongs

@bp.route('/songs')
@bp.route('/songs/search/')
def songs_api_view():
  songs = Tblsongs.query.all()
  return {'data': [row.to_dict() for row in songs],}

@bp.route('/songs/search/<search_term>')
def songs_api_search_view(search_term):
  songs = Tblsongs.query.filter(Tblsongs.title.contains(search_term))
  return {'data': [row.to_dict() for row in songs],}
