from flask import Flask, Blueprint, render_template, g, request, url_for, session, flash, current_app, redirect
from flaskr_011.db_queries import row_counter, record_counter, current_user_records, edit_pull_record, edit_one_record, update_one_record
from flaskr_011.ltausers import user_session, login_needed, logoff
from flaskr_011.lta_database import get_dt_db
from wtforms import Form, StringField, DateField, validators
from psycopg2 import pool
import functools
import re


bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')

input_from_form = {'volume': '', 'id': '', 'name': '', 'sex': '', 'height': '', 'build': '', 'dentition': '', 'special_peculiarities': '', 'date_of_birth': '', 'place_of_birth': '', 'place_of_residence': '', 'residence': '', 'religion': '', 'childhood_status': '', 'marital_status': '', 'number_of_children': '',
                'occupation': '', 'occupation_2': '', 'occupation_3': '', 'military_service': '', 'literacy': '',  'education': '', 'criminal_history': '', 'crime': '', 'sentence_begins': '', 'sentence_expires': '', 'prison_term_day': '', 'ransome': '', 'associates': '', 'degree_of_crime': '', 'degree_of_punishment': '', 'notes': '', 'arrest_site': ''}

@bp.route('/post_data', methods=["POST", "GET"])
@login_needed
def main_input():
    row_counter()
    
    




    if request.method == "POST":
        # def add_record():
        #     rec = Record_input()
        #     if rec.validate_on_submit()

        volume = request.form['volume']
        input_from_form.update({'volume': volume})

        id = request.form['id']
        input_from_form.update({'id': id})

        name = request.form['name']
        input_from_form.update({'name': name})

        sex = request.form['sex']
        input_from_form.update({'sex': sex})

        height = request.form['height']
        input_from_form.update({'height': height})

        build = request.form['build']
        input_from_form.update({'build': build})

        dentition = request.form['dentition']
        input_from_form.update({'dentition': dentition})

        special_peculiarities = request.form['special_peculiarities']
        input_from_form.update({'special_peculiarities': special_peculiarities})

        date_of_birth = request.form['date_of_birth']
        input_from_form.update({'date_of_birth': date_of_birth})

        place_of_birth = request.form['place_of_birth']
        input_from_form.update({'place_of_birth': place_of_birth})

        place_of_residence = request.form['place_of_residence']
        input_from_form.update({"place_of_residence": place_of_residence})

        residence = request.form['residence']
        input_from_form.update({"residence": residence})

        religion = request.form['religion']
        input_from_form.update({'religion': religion})

        childhood_status = request.form['childhood_status']
        input_from_form.update({'childhood_status': childhood_status})

        marital_status = request.form['marital_status']
        input_from_form.update({'marital_status': marital_status})

        number_of_children = request.form['number_of_children']
        input_from_form.update({'number_of_children': number_of_children})

        occupation = request.form['occupation']
        input_from_form.update({'occupation': occupation})

        occupation_2 = request.form['occupation_2']
        input_from_form.update({'occupation_2': occupation_2})

        occupation_3 = request.form['occupation_3']
        input_from_form.update({'occupation_3': occupation_3})

        military_service = request.form['military_service']
        input_from_form.update({'military_service': military_service})

        literacy = request.form['literacy']
        input_from_form.update({'literacy': literacy})

        education = request.form['education']
        input_from_form.update({'education': education})

        criminal_history = request.form['criminal_history']
        input_from_form.update({'criminal_history': criminal_history})

        crime = request.form['crime']
        input_from_form.update({'crime': crime})

        sentence_begins = request.form['sentence_begins']
        input_from_form.update({'sentence_begins': sentence_begins})

        sentence_expires = request.form['sentence_expires']
        input_from_form.update({'sentence_expires': sentence_expires})

        prison_term_day = request.form['prison_term_day']
        input_from_form.update({'prison_term_day': prison_term_day})

        ransome = request.form['ransome']
        input_from_form.update({'ransome': ransome})

        associates = request.form['associates']
        input_from_form.update({'associates': associates})

        degree_of_crime = request.form['degree_of_crime']
        input_from_form.update({'degree_of_crime': degree_of_crime})

        degree_of_punishment = request.form['degree_of_punishment']
        input_from_form.update({'degree_of_punishment': degree_of_punishment})

        notes = request.form['notes']
        input_from_form.update({'notes': notes})

        arrest_site = request.form['arrest_site']
        input_from_form.update({'arrest_site': arrest_site})

        username = session.get("current_user")



        volume = input_from_form['volume']
        id= input_from_form['id']
        name = input_from_form['name']
        sex= input_from_form['sex']
        height= input_from_form['height']
        build= input_from_form['build']
        dentition= input_from_form['dentition']
        special_peculiarities= input_from_form['special_peculiarities']
        date_of_birth= input_from_form['date_of_birth']
        place_of_birth= input_from_form['place_of_birth']
        place_of_residence= input_from_form['place_of_residence']
        residence= input_from_form['residence']
        religion= input_from_form['religion']
        childhood_status= input_from_form['childhood_status']
        marital_status= input_from_form['marital_status']
        number_of_children= input_from_form['number_of_children']
        occupation= input_from_form['occupation']
        occupation_2= input_from_form['occupation_2']
        occupation_3= input_from_form['occupation_3']
        military_service= input_from_form['military_service']
        literacy= input_from_form['literacy']
        education= input_from_form['education']
        criminal_history= input_from_form['criminal_history']
        crime= input_from_form['crime']
        sentence_begins= input_from_form['sentence_begins']
        sentence_expires= input_from_form['sentence_expires']
        prison_term_day= input_from_form['prison_term_day']
        ransome= input_from_form['ransome']
        associates= input_from_form['associates']
        degree_of_crime= input_from_form['degree_of_crime']
        degree_of_punishment= input_from_form['degree_of_punishment']
        notes= input_from_form['notes']
        arrest_site= input_from_form['arrest_site']

        class Record:
            def __init__(self, volume, id, name, sex, height, build, dentition, special_peculiarities, date_of_birth, place_of_birth, place_of_residence, residence, religion, childhood_status, marital_status, number_of_children, occupation,
                    occupation_2, occupation_3, military_service, literacy, education, criminal_history, crime, sentence_begins, sentence_expires, prison_term_day, ransome, associates, degree_of_crime, degree_of_punishment, notes, arrest_site):
                self._volume = volume
                self._id = id
                self._name = name
                self._sex = sex
                self._height = height
                self._build = build
                self._dentition = dentition
                self._special_peculiarities = special_peculiarities
                self._date_of_birth = date_of_birth
                self._place_of_birth = place_of_birth
                self._place_of_residence = place_of_residence
                self._residence = residence
                self._religion = religion
                self._childhood_status = childhood_status
                self._marital_status = marital_status
                self._number_of_children = number_of_children
                self._occupation = occupation
                self._occupation_2 = occupation_2
                self._occupation_3 = occupation_3
                self._military_service = military_service
                self._literacy = literacy
                self._education = education
                self._criminal_history = criminal_history
                self._crime = crime
                self._sentence_begins = sentence_begins
                self._sentence_expires = sentence_expires
                self._prison_term_day = prison_term_day
                self._ransome = ransome
                self._associates = associates
                self._degree_of_crime = degree_of_crime
                self._degree_of_punishment = degree_of_punishment
                self._arrest_site = arrest_site
                self._notes = notes

            @property
            def volume (self):
                return self._volume

            @volume.setter
            def set_volume (self, volume):
                self._volume = volume

            @property
            def id (self):
                return self._id

            @id.setter
            def set_id (self,id):
                self._id = id

            @property
            def name (self):
                return self._name

            @name.setter
            def set_name (self, name):
                self._name = name

            @property
            def sex (self):
                return self._sex

            @sex.setter
            def set_sex (self, sex):
                self._sex = sex

            @property
            def height(self):
                return self._height

            @height.setter
            def set_height(self, height):
                self._height = height

            @property
            def build(self):
                return self._build

            @build.setter
            def set_build(self, build):
                self._build = build

            @property
            def dentition(self):
                return self._dentition

            @dentition.setter
            def set_dentition(self, dentition):
                self._dentition = dentition

            @property
            def special_peculiarities(self):
                return self._special_peculiarities

            @special_peculiarities.setter
            def set_special_peculiarities(self, special_peculiarities):
                self._special_peculiarities =  special_peculiarities

            @property
            def date_of_birth (self):
                return self._date_of_birth

            @date_of_birth.setter
            def set_date_of_birth (self, date_of_birth):
                self._date_of_birth = date_of_birth

            @property
            def place_of_birth (self):
                return self._place_of_birth

            @date_of_birth.setter
            def set_place_of_birth (self, place_of_birth):
                self._place_of_birth = place_of_birth

            @property
            def place_of_residence (self):
                return self._place_of_residence

            @place_of_residence.setter
            def set_place_of_residence (self, place_of_residence):
                self._place_of_residence = place_of_residence

            @property
            def residence (self):
                return self._residence

            @place_of_residence.setter
            def set_residence (self, residence):
                self._residence = residence

            @property
            def religion (self):
                return self._religion

            @religion.setter
            def set_religion (self, religion):
                self._religion = religion

            @property
            def childhood_status (self):
                return self._childhood_status

            @childhood_status.setter
            def set_childhood_status (self, childhood_status):
                self._childhood_status = childhood_status

            @property
            def marital_status (self):
                return self._marital_status

            @marital_status.setter
            def set_marital_status (self, marital_status):
                self._marital_status = marital_status


            @property
            def marital_status (self):
                return self._marital_status

            @marital_status.setter
            def set_marital_status (self, marital_status):
                self._marital_status = marital_status

            @property
            def number_of_children (self):
                return self._number_of_children

            @number_of_children.setter
            def set_number_of_children (self, number_of_children):
                self._number_of_children= number_of_children

            @property
            def occupation (self):
                return self._occupation

            @occupation.setter
            def set_occupation (self, occupation):
                self._occupation= occupation

            @property
            def occupation_2 (self):
                return self._occupation_2

            @occupation_2.setter
            def set_occupation_2 (self, occupation_2):
                self._occupation_2= occupation_2

            @property
            def occupation_3 (self):
                return self._occupation_3

            @occupation_3.setter
            def set_occupation_3 (self, occupation_3):
                self._occupation_3= occupation_3

            @property
            def military_service (self):
                return self._military_service

            @military_service.setter
            def set_military_service (self, military_service):
                self._military_service= military_service

            @property
            def literacy (self):
                return self._literacy

            @literacy.setter
            def set_literacy (self, literacy):
                self._literacy= literacy

            @property
            def education (self):
                return self._education

            @education.setter
            def set_education (self, education):
                self._education= education

            @property
            def criminal_history (self):
                return self._criminal_history

            @criminal_history.setter
            def set_criminal_history (self, criminal_history):
                self._criminal_history= criminal_history

            @property
            def criminal_history (self):
                return self._criminal_history

            @criminal_history.setter
            def set_criminal_history (self, criminal_history):
                self._criminal_history= criminal_history

            @property
            def crime (self):
                return self._crime

            @crime.setter
            def set_crime (self, crime):
                self._crime= crime

            @property
            def sentence_begins (self):
                return self._sentence_begins

            @sentence_begins.setter
            def sentence_begins (self, sentence_begins):
                self._sentence_begins= sentence_begins

            @property
            def sentence_expires (self):
                return self._sentence_expires

            @sentence_expires.setter
            def sentence_expires (self, sentence_expires):
                self._sentence_expires= sentence_expires

            @property
            def prison_term_day (self):
                return self._prison_term_day

            @prison_term_day.setter
            def prison_term_day (self, prison_term_day):
                self._prison_term_day= prison_term_day

            @property
            def ransome (self):
                return self._ransome

            @ransome.setter
            def ransome (self, ransome):
                self._ransome= ransome

            @property
            def associates (self):
                return self._associates

            @associates.setter
            def associates (self, associates):
                self._associates= associates

            @property
            def degree_of_crime(self):
                return self._degree_of_crime

            @degree_of_crime.setter
            def associates (self, degree_of_crime):
                self._degree_of_crime= degree_of_crime

            @property
            def degree_of_punishment(self):
                return self._degree_of_punishment

            @degree_of_punishment.setter
            def degree_of_punishment (self, degree_of_punishment):
                self._degree_of_punishment= degree_of_punishment

            @property
            def arrest_site(self):
                return self._arrest_site

            @arrest_site.setter
            def arrest_site (self, arrest_site):
                self._arrest_site= arrest_site

            @property
            def notes(self):
                return self._notes

            @notes.setter
            def notes (self, notes):
                self._notes= notes

        new_record = Record(volume,
        id,
        name,
        sex,
        height,
        build,
        dentition,
        special_peculiarities,
        date_of_birth,
        place_of_birth,
        place_of_residence,
        residence,
        religion,
        childhood_status,
        marital_status,
        number_of_children,
        occupation,
        occupation_2,
        occupation_3,
        military_service,
        literacy,
        education,
        criminal_history,
        crime,
        sentence_begins,
        sentence_expires,
        prison_term_day,
        ransome,
        associates,
        degree_of_crime,
        degree_of_punishment,
        notes,
        arrest_site)

        
        conn = get_dt_db().getconn()
        with conn.cursor() as cursor:
            username = session['current_user']
            dbquery = current_app.open_resource('insert_input.sql').read()
            cursor.execute(dbquery, (
            new_record.volume,
            new_record.id,
            new_record.name,
            new_record.sex,
            new_record.height,
            new_record.build,
            new_record.dentition,
            new_record.special_peculiarities,
            new_record.date_of_birth,
            new_record.place_of_birth,
            new_record.place_of_residence,
            new_record.residence,
            new_record.religion,
            new_record.childhood_status,
            new_record.marital_status,
            new_record.number_of_children,
            new_record.occupation,
            new_record.occupation_2,
            new_record.occupation_3,
            new_record.military_service,
            new_record.literacy,
            new_record.education,
            new_record.criminal_history,
            new_record.crime,
            new_record.sentence_begins,
            new_record.sentence_expires,
            new_record.prison_term_day,
            new_record.ransome,
            new_record.associates,
            new_record.degree_of_crime,
            new_record.degree_of_punishment,
            new_record.notes,
            new_record.arrest_site,
            username ))
        conn.commit()
        #SESSION when it is submitted t gets a record_session which is uniqe. this record_session will be use as the identifier instead ov the id what can be messes up byt the user
    record_num = record_counter()
    return render_template('input.html', records = record_num)


@bp.route('/myrecords', methods=["GET", "POST"])
@login_needed
def myrecords():
    my_record_num = current_user_records()    # SESSION needs to call the record_session too
    headers = ["Volume", "Id", "Name", "Sex", "Height", "Build", "Dentition", "Special Peculiarities", "Date of Birth", "Place of Birth", "Place of Residence", "Residence", "Religion", "Childhood", "Marital Status", "Children", "Occupation","Occupation 2", "Occupation 3", "Military Service", "Literacy", "Eduction", "Criminal History", "Crime", "Sentence Begins", "Sentence Expires", "Prisonterm (days)", "Ransome", "Associates", "Degree of Crime", "Degree of Punishment", "Notes", "Arrest Site"]
    records = edit_pull_record()
    if request.method == "GET":
        
        

        
#MY RECORD MY RECORDSMY RECORD MY RECORDSMY RECORD MY RECORDSMY RECORD MY RECORDSMY RECORD MY RECORDSMY RECORD MY RECORDSMY RECORD MY RECORDSMY RECORD MY RECORDSMY RECORD MY RECORDSMY RECORD MY RECORDSMY RECO
        volume = [val[0] for val in records]
        id = [val[1] for val in records]
        names = [val[2] for val in records]
        sex = [val[3] for val in records]
        height = [val[4] for val in records]
        build = [val[5] for val in records]
        dentition = [val[6] for val in records]
        peculiarities = [val[7] for val in records]
        birthdate = [val[8] for val in records]
        birthplace = [val[9] for val in records]
        place_of_residence = [val[10] for val in records]
        residence = [val[11] for val in records]
        religion = [val[12] for val in records]
        childhood = [val[13] for val in records]
        marital_status = [val[14] for val in records]
        children = [val[15] for val in records]
        occupation= [val[16] for val in records]
        occupation_2 = [val[17] for val in records]
        occupation_3 = [val[18] for val in records]
        military_service = [val[19] for val in records]
        literacy= [val[20] for val in records]
        eduction = [val[21] for val in records]
        criminal_history = [val[22] for val in records]
        crime= [val[23] for val in records]
        sentence_begins = [val[24] for val in records]
        sentence_expires = [val[25] for val in records]
        prison_term_day = [val[26] for val in records]
        ransome = [val[27] for val in records]
        associates = [val[28] for val in records]
        degree_of_crime = [val[29] for val in records]
        degree_of_punishment = [val[30] for val in records]
        notes = [val[31] for val in records]
        arrest_site = [val[32] for val in records]
        record_session = [val[33] for val in records]
        session['record_session'] = record_session
        
        #SESSION the jinja loop needs to be set for record_session instead of id
        #IF I put this in a class no need to add so many variables
#MY RECORD MY RECORDSMY RECORD MY RECORDSMY RECORD MY RECORDSMY RECORD MY RECORDSMY RECORD MY RECORDSMY RECORD MY RECORDSMY RECORD MY RECORDSMY RECORD MY RECORDSMY RECORD MY RECORDSMY RECORD MY RECORDS
        return render_template('myrecords.html', own_records = my_record_num, headers=headers,  volume=volume, id=id, names=names, sex=sex, height=height, build=build, dentition=dentition, peculiarities=peculiarities, birthdate=birthdate, birthplace=birthplace, place_of_residence=place_of_residence, residence=residence, religion=religion, childhood=childhood, marital_status=marital_status, children=children, occupation=occupation,occupation_2=occupation_2, occupation_3=occupation_3, military_service=military_service, literacy=literacy, eduction=eduction, criminal_history=criminal_history, crime=crime, sentence_begins=sentence_begins, sentence_expires=sentence_expires, prison_term_day=prison_term_day, ransome=ransome, associates=associates, degree_of_crime=degree_of_crime, degree_of_punishment=degree_of_punishment, notes=notes, arrest_site=arrest_site )
    if request.method == "POST":
#MY RECORD MY RECORDSMY RECORD MY RECORDSMY RECORD MY RECORDSMY RECORD MY RECORDSMY RECORD MY RECORDSMY RECORD MY RECORDSMY RECORD MY RECORDSMY RECORD MY RECORDSMY RECORD MY RECORDSMY RECORD MY RECORDSMY 

            

            # the value which the query bases on will be the record_session session['record'] = request.form.get('edit record )
            print(session['record_session'][0])
            record_for_edit = edit_one_record(session['record_session'][0])
            
    
            volume = record_for_edit[0]
            id = record_for_edit[1]
            names =record_for_edit[2]
            sex =record_for_edit[3]
            height =record_for_edit[4]
            build =record_for_edit[5]
            dentition =record_for_edit[6]
            peculiarities =record_for_edit[7]
            birthdate =record_for_edit[8]
            birthplace =record_for_edit[9]
            place_of_residence = record_for_edit[10]
            residence = record_for_edit[11]
            religion = record_for_edit[12]
            childhood = record_for_edit[13]
            marital_status = record_for_edit[14]
            children = record_for_edit[15]
            occupation= record_for_edit[16]
            occupation_2 = record_for_edit[17]
            occupation_3 = record_for_edit[18]
            military_service = record_for_edit[19]
            literacy= record_for_edit[20]
            eduction = record_for_edit[21]
            criminal_history = record_for_edit[22]
            crime= record_for_edit[23]
            sentence_begins = record_for_edit[24]
            sentence_expires = record_for_edit[25]
            prison_term_day = record_for_edit[26]
            ransome = record_for_edit[27]
            associates = record_for_edit[28]
            degree_of_crime = record_for_edit[29]
            degree_of_punishment = record_for_edit[30]
            notes = record_for_edit[31]
            arrest_site = record_for_edit[32]
            print('now it goes to the edit page')
            
        

            #return render_template('edit.html', headers=headers, volume=volume, id=id, names=names, sex=sex, height=height, build=build, dentition=dentition, peculiarities=peculiarities, birthdate=birthdate, birthplace=birthplace, place_of_residence=place_of_residence, residence=residence, religion=religion, childhood=childhood, marital_status=marital_status, children=children, occupation=occupation,occupation_2=occupation_2, occupation_3=occupation_3, military_service=military_service, literacy=literacy, eduction=eduction, criminal_history=criminal_history, crime=crime, sentence_begins=sentence_begins, sentence_expires=sentence_expires, prison_term_day=prison_term_day, ransome=ransome, associates=associates, degree_of_crime=degree_of_crime, degree_of_punishment=degree_of_punishment, notes=notes, arrest_site=arrest_site )

            return redirect(url_for('dashboard.edit_record'))



@bp.route('/myrecords/edit/', methods=["POST", "GET", "PUT" ])
@login_needed
def edit_record():
    my_record_num = current_user_records()
    headers = ["Volume", "Id", "Name", "Sex", "Height", "Build", "Dentition", "Special Peculiarities", "Date of Birth", "Place of Birth", "Place of Residence", "Residence", "Religion", "Childhood", "Marital Status", "Children", "Occupation","Occupation 2", "Occupation 3", "Military Service", "Literacy", "Eduction", "Criminal History", "Crime", "Sentence Begins", "Sentence Expires", "Prisonterm (days)", "Ransome", "Associates", "Degree of Crime", "Degree of Punishment", "Notes", "Arrest Site"]
#EDIT RECORS EDIT RECORDS  EDIT RECORS EDIT RECORDS  EDIT RECORS EDIT RECORDS  EDIT RECORS EDIT RECORDS  EDIT RECORS EDIT RECORDS  EDIT RECORS EDIT RECORDS  EDIT RECORS EDIT RECORDS  EDIT RECORS EDIT RECORDS  
    if request.method == "GET":

                
#EDIT RECORS EDIT RECORDS  EDIT RECORS EDIT RECORDS  EDIT RECORS EDIT RECORDS  EDIT RECORS EDIT RECORDS  EDIT RECORS EDIT RECORDS  EDIT RECORS EDIT RECORDS  EDIT RECORS EDIT RECORDS  EDIT RECORS EDIT RECORDS 

                record_for_edit = edit_one_record(session['record_session'][0])
                
        
                volume = record_for_edit[0]
                id = record_for_edit[1]
                names =record_for_edit[2]
                sex =record_for_edit[3]
                height =record_for_edit[4]
                build =record_for_edit[5]
                dentition =record_for_edit[6]
                peculiarities =record_for_edit[7]
                birthdate =record_for_edit[8]
                birthplace =record_for_edit[9]
                place_of_residence = record_for_edit[10]
                residence = record_for_edit[11]
                religion = record_for_edit[12]
                childhood = record_for_edit[13]
                marital_status = record_for_edit[14]
                children = record_for_edit[15]
                occupation= record_for_edit[16]
                occupation_2 = record_for_edit[17]
                occupation_3 = record_for_edit[18]
                military_service = record_for_edit[19]
                literacy= record_for_edit[20]
                eduction = record_for_edit[21]
                criminal_history = record_for_edit[22]
                crime= record_for_edit[23]
                sentence_begins = record_for_edit[24]
                sentence_expires = record_for_edit[25]
                prison_term_day = record_for_edit[26]
                ransome = record_for_edit[27]
                associates = record_for_edit[28]
                degree_of_crime = record_for_edit[29]
                degree_of_punishment = record_for_edit[30]
                notes = record_for_edit[31]
                arrest_site = record_for_edit[32]



                

                return render_template('edit.html', own_records = my_record_num, headers=headers, volume=volume, id=id, names=names, sex=sex, height=height, build=build, dentition=dentition, peculiarities=peculiarities, birthdate=birthdate, birthplace=birthplace, place_of_residence=place_of_residence, residence=residence, religion=religion, childhood=childhood, marital_status=marital_status, children=children, occupation=occupation,occupation_2=occupation_2, occupation_3=occupation_3, military_service=military_service, literacy=literacy, eduction=eduction, criminal_history=criminal_history, crime=crime, sentence_begins=sentence_begins, sentence_expires=sentence_expires, prison_term_day=prison_term_day, ransome=ransome, associates=associates, degree_of_crime=degree_of_crime, degree_of_punishment=degree_of_punishment, notes=notes, arrest_site=arrest_site )

    if request.method == "POST":
        modified_volume = request.form.get('edit_volume')
        modified_id = request.form.get('edit_id')
        modified_names = request.form.get('edit_names')
        modified_sex = request.form.get('edit_sex')
        modified_height = request.form.get('edit_height')
        modified_build = request.form.get('edit_build')
        modified_dentition = request.form.get('edit_dentition')
        modified_peculiarities = request.form.get('edit_peculiarities')
        modified_birthdate = request.form.get('edit_birthdate')
        modified_birthplace = request.form.get('edit_birthplace')
        modified_place_of_residence = request.form.get('edit_place_of_residence')
        modified_residence = request.form.get('edit_residence')
        modified_religion = request.form.get('edit_religion')
        modified_childhood = request.form.get('edit_childhood')
        modified_marital_status = request.form.get('edit_marital_status')
        modified_children = request.form.get('edit_children')
        modified_occupation= request.form.get('edit_occupation')
        modified_occupation_2 = request.form.get('edit_occupation_2')
        modified_occupation_3 = request.form.get('edit_occupation_3')
        modified_military_service = request.form.get('edit_military_service')
        modified_literacy= request.form.get('edit_literacy')
        modified_eduction = request.form.get('edit_eduction')
        modified_criminal_history = request.form.get('edit_criminal_history')
        modified_crime= request.form.get('edit_crime')
        modified_sentence_begins = request.form.get('edit_sentence_begins')
        modified_sentence_expires = request.form.get('edit_sentence_expires')
        modified_prison_term_day = request.form.get('edit_prison_term_day')
        modified_ransome = request.form.get('edit_ransome')
        modified_associates = request.form.get('edit_associates')
        modified_degree_of_crime = request.form.get('edit_degree_of_crime')
        modified_degree_of_punishment = request.form.get('edit_degree_of_punishment')
        modified_notes = request.form.get('edit_notes')
        modified_arrest_site = request.form.get('edit_arrest_site')
        session_record = session['record_session'][0]
#EDIT RECORS EDIT RECORDS  EDIT RECORS EDIT RECORDS  EDIT RECORS EDIT RECORDS  EDIT RECORS EDIT RECORDS  EDIT RECORS EDIT RECORDS  EDIT RECORS EDIT RECORDS  EDIT RECORS EDIT RECORDS  EDIT RECORS EDIT RECORDS  
        modified_record = [modified_volume, modified_id, modified_names, modified_sex, modified_height, modified_build, modified_dentition, modified_peculiarities, modified_birthdate, modified_birthplace, modified_place_of_residence, modified_residence, modified_religion, modified_childhood, modified_marital_status, modified_children, modified_occupation, modified_occupation_2, modified_occupation_3,  modified_military_service, modified_literacy, modified_eduction, modified_criminal_history, modified_crime, modified_sentence_begins, modified_sentence_expires, modified_prison_term_day, modified_ransome, modified_associates, modified_degree_of_crime, modified_degree_of_punishment, modified_notes, modified_arrest_site, session_record]
        print('hettttttttttttttttttttttttttt')
        for i in range(0,len(modified_record)):
            
            if modified_record[i]  ==  None or "":
                print(modified_record[i])
                error = "You cant submit None value"
                flash(error)
        
        
        
        update_one_record(tuple(modified_record))
        
        
        return redirect(url_for('dashboard.myrecords'))

   




@login_needed
def back_to_input():
    row_counter()
    return render_template('input.html')
