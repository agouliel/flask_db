from flask import render_template
from app_pkg.bp_mis import bp
from app_pkg.bp_mis.models import Monitor

@bp.route('/monitor')
def monitor_view():
  monitors = Monitor.query.all()
  return render_template('monitor.html', records=monitors)