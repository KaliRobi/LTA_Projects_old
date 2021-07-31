from flask import Flask, Blueprint, redirect, render_template, g, request, url_for, flash, session
from werkzeug.security import check_password_hash, generate_password_hash
from flaskr.lta_database import get_users_db
from flaskr.db_queries import record_counter
from psycopg2 import pool
import functools



bp = Blueprint('users', __name__, url_prefix='/users' )


@bp.route('/login', methods=('GET', 'POST'))
def login_to_app():
    record_num = record_counter()
    if request.method == 'POST':        
        username = request.form['username']
        password = request.form['password']
        
        conn = get_users_db().getconn()
        cur = conn.cursor()
        error = None
        cur.execute(
            "SELECT * FROM lta_users WHERE username = %s", (username,)
        )
        user = cur.fetchone()
        

        if user is None:
            error = 'Username or password is incorrect'
        elif not user[2] == password:
        # elif not check_password_hash(user['password'], password):
            error = 'Username or password is incorrect'
        
        if error is None:
            session.clear()
            session["current_user"] = user[1]           
            flash(session["current_user"])
            return render_template('input.html', records = record_num)
        
        flash(error)

    return render_template('forusers.html')


@bp.before_app_request
def user_session():
    if "current_user" not in session:
        g.user = None
    else:
        user = session["current_user"]
        conn = get_users_db().getconn()
        cur = conn.cursor()
        cur.execute(
            "SELECT * FROM lta_users WHERE username = %s", (user,)
        )
        g.user = cur.fetchone()
        print(g.user[1])
        

def login_needed(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if session["current_user"] is None:
            return redirect(url_for('users.login_to_app'))
        
        return view(**kwargs)
    
    return wrapped_view

@bp.route('/logoff')
def logoff():
    session.clear()
    print(g.user[1])
    return redirect(url_for('users.login_to_app'))