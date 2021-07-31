from flask import Blueprint, flash, g, redirect, render_template, request, url_for, Markup, jsonify
from werkzeug.exceptions import abort
from flaskr_011.db_queries import row_counter, current_user_records
from flaskr_011.lta_database import get_dt_db
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


@bp.route('/api/datatransfer', methods=["GET", "POST"])
def analytics_receiver():
    rel3 = []
    rel3_percent = []
    if request.method == 'POST':
        content = request.json
        selected_town = content['town']

        conn = get_dt_db().getconn()
        cur =  conn.cursor() 
        print(selected_town)
        cur.execute(
            "SELECT DISTINCT * FROM (SELECT religion, count(religion)  OVER(PARTITION BY religion) FROM lta_main WHERE place_of_residence = %s) AS view", (selected_town,)
        )
        return_rel = cur.fetchall()
        

        for x in range(len(return_rel)):          
                rel3.append(return_rel[x][0])  
                rel3_percent.append(return_rel[x][1])
            
        comrel = dict(zip(rel3, rel3_percent))      
        print(comrel)
        return content
     
    elif request.method == 'GET':
        allTowns =  ['All Towns','Balmazújváros','Hajdúböszörmény', 'Hajdúszoboszló', 'Debrecen', 'Hajdúnánás', 'Vámospércs', 'Ebes', 'Tiszacsege']

        towns2 = ['Balmazujvaros_female', 'Balmazujvaros_male', 'Hajduboszormeny_female', 'Hajduboszormeny_male', 'hajduszoboszlo_female', 'hajduszoboszlo_male', 'Debrecen_female', 'Debrecen_male']
        nums2 =  [153.26, 164.27, 153.12, 163.12, 153.74, 163.96, 152.30,  163.80]

        nums = [2120, 814, 308,180,24,2]
        rels = ['Ref', 'Kat', 'GörK','Izr', 'Ev', 'Feln']
        
        comrel = dict(zip(rel3, rel3_percent))
        print(comrel )

        rels2 = ['Ref', 'Kat', 'Izr', 'GörK', 'Ev',]
        relnums2 = [155,48,7,6,1,1]

        comrel = dict(zip(rels, nums))
        comrel2 = dict(zip(rels2, relnums2))

        combine  =  dict(zip(towns2, nums2))
        
        adat =  jsonify({"comrel": comrel, "combine": combine, "comrel2": comrel2, "allTowns": allTowns })
        return adat


# @bp.route('/api/sender', methods=["GET"])
# def analytics_sender():
#     allTowns =  ['All Towns','Balmazujvaros','Hajduboszormeny', 'Hajduszoboszlo', 'Debrecen', 'Hajdunanas', 'Hortobagy', 'Vamospercs', 'Ebes', 'Tiszacsege']

#     towns2 = ['Balmazujvaros_female', 'Balmazujvaros_male', 'Hajduboszormeny_female', 'Hajduboszormeny_male', 'hajduszoboszlo_female', 'hajduszoboszlo_male', 'Debrecen_female', 'Debrecen_male']
#     nums2 =  [153.26, 164.27, 153.12, 163.12, 153.74, 163.96, 152.30,  163.80]

#     nums = [2120, 814, 308,180,24,2]
#     rels = ['Ref', 'Kat', 'GörK','Izr', 'Ev', 'Feln']


#     rels2 = ['Ref', 'Kat', 'Izr', 'GörK', 'Ev',]
#     relnums2 = [155,48,7,6,1,1]

#     comrel = dict(zip(rels, nums))
#     comrel2 = dict(zip(rels2, relnums2))

#     combine  =  dict(zip(towns2, nums2))
    
#     adat =  jsonify({"comrel": comrel, "combine": combine, "comrel2": comrel2, "allTowns": allTowns })
#     if request.method == 'GET':           
#         print(adat)
#         return adat




@bp.route('/users')
def users():
    row_count = Markup("<h2>{}</h2>").format(row_counter())
    flash(row_count)
    return render_template('forusers.html')




    




