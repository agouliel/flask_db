from app_pkg.bp_api import bp
from app_pkg.bp_songs.models import Tblsongs
from flask import request
from app_pkg import db

@bp.route('/songs')
def songs_api_view():
  songs = Tblsongs.query.all()
  return {'data': [row.to_dict() for row in songs],}

@bp.route('/songs/search/')
def songs_api_search_all_view():
  page = request.args.get('page', 1, type=int)
  pagination = db.paginate(
      Tblsongs.query,
      page=page,
      per_page=50,
      error_out=False)
  songs = pagination.items
  prev = page-1 if pagination.has_prev else None
  next = page+1 if pagination.has_next else None
  return {
    'data': [row.to_dict() for row in songs],
    'prev': prev,
    'next': next,
    'count': pagination.total
  }

@bp.route('/songs/search/<search_term>')
def songs_api_search_view(search_term):
  page = request.args.get('page', 1, type=int)
  pagination = db.paginate(
      Tblsongs.query.filter(Tblsongs.title.contains(search_term)),
      page=page,
      per_page=50,
      error_out=False)
  songs = pagination.items
  prev = page-1 if pagination.has_prev else None
  next = page+1 if pagination.has_next else None
  return {
    'data': [row.to_dict() for row in songs],
    'prev': prev,
    'next': next,
    'count': pagination.total
  }
