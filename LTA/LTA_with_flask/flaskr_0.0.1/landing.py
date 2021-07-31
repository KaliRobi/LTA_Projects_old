from flask import Blueprint, flash, g, redirect, render_template, request, url_for, Markup
from werkzeug.exceptions import abort
from flaskr_p3.db_queries import row_counter, current_user_records
import time


bp = Blueprint('main', __name__)

@bp.route('/')
def index():
        row_count = Markup("<h4>{}</h4>").format(row_counter())
        return render_template('index.html', row_count=row_count)
        



@bp.route('/map')
def map():
    row_count = Markup("<h2>{}</h2>").format(row_counter())
    flash(row_count)
    return render_template('map.html')
  

@bp.route('/analytics')
def analytics():
    row_count = Markup("<h2>{}</h2>").format(row_counter())
    flash(row_count)
    return render_template('analytics.html')


@bp.route('/users')
def users():
    row_count = Markup("<h2>{}</h2>").format(row_counter())
    flash(row_count)
    return render_template('forusers.html')




    




