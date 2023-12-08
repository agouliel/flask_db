from flask import render_template
from app_pkg import app
from app_pkg.models import Monitor

@app.route('/')
def index():
  monitors = Monitor.query.all()
  return render_template('index.html', records=monitors)

