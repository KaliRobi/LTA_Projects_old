import os
from time import timezone
from flask import Flask
from flaskr_011.db_queries import row_counter, record_counter, data_all
from flask_cors import CORS



def create_app(test_config=None):
    #create and configure the base of the app
    # so the folders are relative to this currecnt one.
    app = Flask(__name__, instance_relative_config=True)
    CORS(app)
    cors = CORS(app, resources={
        r"/*": {
            "origins": "*"
        }

    })
    app.config.from_mapping(
        SECRET_KEY= 'J={IAGMn0i3,e9)*v8Stq^',
        RECORDS_DATABASE  =  os.path.join(app.instance_path, 'lta_data.pgsql'),
        USERS_DATABASE = os.path.join(app.instance_path, 'lta_users.pgsql')

    )

    

    # scheduler = BackgroundScheduler()

    # scheduler = BackgroundScheduler()
    # scheduler.add_job(row_counter, 'interval', seconds=10)
    # scheduler.add_job(record_counter, 'interval', seconds=10)
    # scheduler.add_job(data_all, 'interval', seconds=5)
    # scheduler.start()





     #registering the other blueprints

    from . import lta_database
    lta_database.init_app(app)

    from . import landing
    app.register_blueprint(landing.bp)

    from . import ltausers
    app.register_blueprint(ltausers.bp)
    
    from . import input
    app.register_blueprint(input.bp)


    
    if test_config is None:
         app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)
    
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    
    
    
    return app