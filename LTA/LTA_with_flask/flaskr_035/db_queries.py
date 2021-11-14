from flask import Flask, current_app, Blueprint, session
import psycopg2
from psycopg2 import pool
from flaskr_011.lta_database import get_users_db, get_dt_db
import time




def row_counter():
        conn = get_users_db().getconn()
        cur =  conn.cursor() 
        data2 = "Select count(username) from lta_users;"        
        cur.execute(data2)
        row_num = cur.fetchone()
        rows = str(row_num[0]).strip('(').rstrip('L)')
        return rows
        
            

def record_counter():
        conn = get_dt_db().getconn()
        cur =  conn.cursor() 
        data2 = "Select count(*) from lta_main;"        
        cur.execute(data2)
        row_num = cur.fetchone()
        rows = str(row_num[0]).strip('(').rstrip('L)')
        return rows


def data_all():
        username = session['current_user']
        conn = get_dt_db().getconn()
        cur =  conn.cursor() 
        cur.execute("Select TO_CHAR(date_of_birth, 'YYYY-MM-DD') from lta_main where username = %s " , (username,))
        row_num = cur.fetchall()
        strrow = []
        years  = [row[0] for row in row_num]
        

def current_user_records():
        username = session['current_user']
        conn = get_dt_db().getconn()
        cur =  conn.cursor() 
        cur.execute("Select COUNT(username) from lta_main where username = %s " , (username,))
        row_num = cur.fetchone()
        row_num = str(row_num[0]).strip('(').rstrip('L)')

        return row_num
        pass
        
        
def edit_pull_record():
        
        username = session['current_user']
        conn = get_dt_db().getconn()
        cur =  conn.cursor() 
        query = "SELECT  volume, id, name, sex, height, build, dentition, special_peculiarities, TO_CHAR(date_of_birth, 'YYYY-MM-DD'), place_of_birth, place_of_residence, residence, religion, childhood_status, marital_status, number_of_children, occupation, occupation_2, occupation_3, military_service, literacy, education, criminal_history, crime, TO_CHAR(sentence_begins, 'YYYY-MM-DD'), TO_CHAR(sentence_expires, 'YYYY-MM-DD'), prison_term_day, ransome, associates, degree_of_crime, degree_of_punishment, notes, arrest_site, record_session from lta_main where username = %s  limit 10;"
        cur.execute(query, (username,))
        row_num = cur.fetchall()
        
       
        return row_num       


        
def edit_one_record(val):
        
        conn = get_dt_db().getconn()
        cur =  conn.cursor() 
        query = "SELECT  volume, id, name, sex, height, build, dentition, special_peculiarities, TO_CHAR(date_of_birth, 'YYYY-MM-DD'), place_of_birth, place_of_residence, residence, religion, childhood_status, marital_status, number_of_children, occupation, occupation_2, occupation_3, military_service, literacy, education, criminal_history, crime, TO_CHAR(sentence_begins, 'YYYY-MM-DD'), TO_CHAR(sentence_expires, 'YYYY-MM-DD'), prison_term_day, ransome, associates, degree_of_crime, degree_of_punishment, notes, arrest_site from lta_main where record_session= %s ;"
        cur.execute(query, (val,))
        row_num = cur.fetchone()
       
        return row_num         
            


def update_one_record(*args):
        
        conn = get_dt_db().getconn()
        cur = conn.cursor()
        query = "UPDATE lta_main set  (volume, id, name, sex, height, build, dentition, special_peculiarities, date_of_birth, place_of_birth, place_of_residence, residence, religion, childhood_status, marital_status, number_of_children, occupation, occupation_2, occupation_3, military_service, literacy, education, criminal_history, crime, sentence_begins, sentence_expires, prison_term_day, ransome, associates, degree_of_crime, degree_of_punishment, notes, arrest_site) = (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) where record_session = %s;"
        cur.execute(query, args[-1])
        conn.commit()
        




