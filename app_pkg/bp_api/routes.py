from app_pkg.bp_api import bp
from app_pkg.bp_songs.models import Tblsongs

@bp.route('/songs')
def songs_api_view():
  songs = Tblsongs.query.all()
  return {'data': [row.to_dict() for row in songs],}
