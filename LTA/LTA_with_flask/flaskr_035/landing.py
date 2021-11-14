from flask import Blueprint, flash, g, redirect, render_template, request, url_for, Markup
from werkzeug.exceptions import abort
from flaskr_011.db_queries import row_counter, current_user_records, record_counter
from flaskr_011.lta_database import get_dt_db
import time
import json
from containerFunction import getContainer, setContaner


bp = Blueprint('main', __name__)

@bp.route('/')
def index():
        row_count = Markup("<h4>Number of Records: {}</h4>").format(record_counter())
        flash(row_count)
        return render_template('index.html')
        



@bp.route('/map')
def map():
    row_count = Markup("<h4>Number of Records: {}</h4>").format(record_counter())
    flash(row_count)
    return render_template('map.html')
  

@bp.route('/analytics')
def analytics():
    row_count = Markup("<h4>Number of Records: {}</h4>").format(record_counter())
    flash(row_count)
    
    return render_template('analytics.html')

def getdata(town):
    conn = get_dt_db().getconn()
    rel3 = []
    
    rel3_percent = []
    cur =  conn.cursor() 
    print(town)
    cur.execute(
        "SELECT DISTINCT * FROM (SELECT religion, count(religion)  OVER(PARTITION BY religion) FROM lta_main WHERE place_of_residence = %s) AS view", (town,)
    )
    return_rel = cur.fetchall()
    setContaner(town)

    for x in range(len(return_rel)):          
            rel3.append(return_rel[x][0])  
            rel3_percent.append(return_rel[x][1])
    return dict(zip(rel3, rel3_percent))  
        
def getApi_data_rel():
    conn = get_dt_db().getconn()
    city = []
    dimension = []
    metric = []
    
    rel3_percent = []
    cur =  conn.cursor() 
    
    cur.execute(
        "SELECT place_of_residence, religion,  count(religion)  FROM lta_main WHERE place_of_residence in (SELECT city FROM geo WHERE county = 'Hajdú-Bihar' order by city)  group by place_of_residence, religion   ORDER BY place_of_residence;"
            )
    data_list = cur.fetchall()
    
    
    for x in range(len(data_list)):          
            city.append(data_list[x][0])  
            dimension.append(data_list[x][1])
            metric.append(data_list[x][1])
    return True


def getApi_data_rel(town):
    conn = get_dt_db().getconn()
    city = []
    dimension = []
    metric = []
    
    rel3_percent = []
    cur =  conn.cursor() 
    
    cur.execute(
            "SELECT religion, count(*) from lta_main where place_of_residence = %s and religion != 'Null' group by religion order by count(*);", (town,)
            )
    data_list = cur.fetchall()
    
    
    for x in range(len(data_list)):          
            dimension.append(data_list[x][0])  
            metric.append(data_list[x][1])
    comrel= dict(zip(dimension,metric))

    adat =  json.dumps({"religion": comrel })
    print(adat)
    return adat

def addHeadersThreeDim(headers, list):
        headed = []
        for x in range(len(list)):
            auList = []
            for k in range(len(list[x])):
                auList.append(list[x][k])
            headedUnit = dict(zip(headers, auList))   
            headed.append(headedUnit)        
        return headed        
def tupleToDict(list):
    eList = []
    keyList = []
    valueList = []
    for i in range(len(list)):
        keyList.append(list[i][0])
        valueList.append(list[i][1])
    eList = dict(zip(keyList, valueList))     
    return eList


def getApi_data_perTown(town):
    conn = get_dt_db().getconn()
    cur =  conn.cursor() 
    # vallasi eloszlas
    cur.execute(
        "SELECT religion,  count(religion)  FROM lta_main WHERE place_of_residence = %s and religion != 'Null' group by place_of_residence, religion ;", (town,) 
            )
    ret_rel = cur.fetchall()
    # iskolazottsag nemek szerint
    cur.execute(
        "SELECT sex, education, count(education)  FROM lta_main WHERE place_of_residence = %s and sex <> 'Null' and  education not in ( 'Null', 'nt', '-')  group by sex, education  ORDER BY count(education) desc;", (town,) 
            )
    ret_edu = cur.fetchall()

    # crime vs kor
    cur.execute(
        "SELECT sex, CAST(CAST(SUBSTRING(id,1,4)as INTEGER)  - extract('year' from date_of_birth) as INT) as age, count(crime) from lta_main where place_of_residence = %s and crime is not null and date_of_birth is not null group by age, sex  order by count(crime) desc;", (town,) 
            )
    ret_crime = cur.fetchall()

    #fogalakozas es kor
    cur.execute(
    "SELECT count(*), occupation, CAST(SUBSTRING(id,1,4)as INTEGER) from lta_main where place_of_residence = %s and occupation != 'Null'   group by occupation, CAST(SUBSTRING(id,1,4)as INTEGER) order by  CAST(SUBSTRING(id,1,4)as INTEGER), count(occupation) desc ;", (town,) 
        )
    #bekerules    
    cur.execute(
    "SELECT to_char(sentence_begins, 'YYYY-MM') as time, count(*)   from lta_main where place_of_residence = %s and sentence_begins is not Null group by time order by time;", (town,) 
        )

    ret_sent = cur.fetchall()
    ret_sent = tupleToDict(ret_sent)    
    ret_occu = cur.fetchall()
    header_edu = ['s', 'e', 'n']
    header_crime = ['s', 'a', 'n']
    header_occu = ['n', 'o', 'a']
    ret_edu = addHeadersThreeDim(header_edu, ret_edu)
    ret_crime= addHeadersThreeDim(header_crime, ret_crime)
    ret_occu = addHeadersThreeDim(header_occu, ret_occu)
    ret_rel = tupleToDict(ret_rel)
    return json.dumps({"ret_edu": ret_edu, "ret_crime": ret_crime, "ret_rel": ret_rel, "ret_occu": ret_occu, "ret_sent": ret_sent},  indent=4)
    


@bp.route('/api/datatransfer/<town>', methods=["GET"])
def analytics_unde(town):     
    
    if request.method == 'GET':        
        
        townso =  getApi_data_perTown(town)
        
        return townso
        

@bp.route('/api/datatransfer/towns', methods=["GET"])
def analytics_towns():
    conn = get_dt_db().getconn()
    cur =  conn.cursor() 
    cur.execute(
        "SELECT city FROM geo WHERE county = 'Hajdú-Bihar' order by city;"
    )
    list_of_towns = []
    return_rel = cur.fetchall()
    for x in range(len(return_rel)): 
        list_of_towns.append(return_rel[x])         
        
    return json.dumps({"towns": list_of_towns})




@bp.route('/users')
def users():
    row_count = Markup("<h4>Number of Records: {}</h4>").format(record_counter())
    flash(row_count)
    return render_template('forusers.html')




    




