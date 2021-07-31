import click
from flask import current_app, g
from flask.cli import with_appcontext
import psycopg2
from psycopg2 import pool



# function to connect the database for data for the users
def get_users_db():
    init_users_db = psycopg2.pool.SimpleConnectionPool(1,20,            
            dbname = "lta_users",
            user = "lta_user_mas",
            host =  "localhost",
            password="proba123")
    if(init_users_db):
        print('pool created')
    conn = init_users_db.getconn()
    if(conn):
        print('conencted too')
        c = conn.cursor()
    return init_users_db
    

def get_dt_db():
    data_pool = psycopg2.pool.ThreadedConnectionPool(1,20,
                dbname = "lta_data",
                user = "lta_data_mas",
                password = "proba123",
                host = "localhost")
    if(data_pool):
        print('data pool created')
    conn = data_pool.getconn()
    if(conn):
        print('data connection')
    return data_pool


def init_dt_db():
    init_data_db = psycopg2.pool.ThreadedConnectionPool(1,20,
                dbname = "lta_data",
                user = "lta_data_mas",
                password = "proba123",
                host = "localhost")
    conn = init_data_db.getconn()
    with conn.cursor() as cursor:
        dbquery = current_app.open_resource('records.sql').read()
        
        cursor.execute(dbquery)
    conn.commit()
        
        
            
        
def init_users_db():
            init_users_db = psycopg2.pool.SimpleConnectionPool(1,20,            
            dbname = "lta_users",
            user = "lta_user_mas",
            host =  "localhost",
            password="proba123")
            conn = init_users_db.getconn()   
            with conn.cursor()  as cursor:
                dbquery =  current_app.open_resource('users.sql').read()
                print(dbquery)
                cursor.execute(dbquery)
            conn.commit()

                    
def init_log_db():
    init_usrdt = psycopg2.pool.SimpleConnectionPool(1,5,
            dbname = "lta_ownership",
            user = "lta_owners",
            host =  "localhost",
            password="proba123")
    conn = init_usrdt.getconn()
    with conn .cursor() as cur:
        dbquery = current_app.open_resource('lta_ownership.sql').read()
        cur.execute(dbquery)
    conn.commit()
    
    
    
    

def get_userdt():
    pass
                  

#closes the conenction
def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

# cleans up after call

@click.command('init-users-db')
@with_appcontext
def init_user_command():
    """Clear the existsing data and create new tables"""
    init_users_db()
    click.echo('Initialized the user database')

@click.command('init-dt-db')
@with_appcontext
def init_db_command():
    """Clear the existsing data and create new tables"""
    init_dt_db()
    click.echo('Initialized the data database')



def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
    app.cli.add_command(init_user_command)




