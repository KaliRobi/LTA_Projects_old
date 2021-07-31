from flask import Flask, request, render_template
import time 

app = Flask(__name__, template_folder='../templates/')

#start the app
@app.route('/')
def home():
    return render_template("input.html")
# at the begining two pages will be available for the users. the input and the 'validator' where they can access and modify the records 
# input_line dictionary supposed to be serve this data in short term, which goes to the databse. in long term UI database interraction is a must
input_line = {}
input_from_form = {'volume': '', 'id': '', 'name': '', 'sex': '', 'height': '', 'build': '', 'dentition': '', 'special_peculiarities': '', 'date_of_birth': '', 'place_of_birth': '', 'place_of_residence': '', 'residence': '', 'religion': '', 'childhood_status': '', 'marital_status': '', 'number_of_children': '',
                'occupation': '', 'occupation_2': '', 'occupation_3': '', 'military_service': '', 'literacy': '',  'education': '', 'criminal_history': '', 'crime': '', 'sentence_begins': '', 'sentence_expires': '', 'prison_term_day': '', 'ransome': '', 'associates': '', 'degree_of_the_crime': '', 'degree_of_the_punishment': '', 'notes': '', 'arrest_site': ''}


@app.route('/post_data', methods=['POST'])
def post_data():    
   
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

    degree_of_the_crime= request.form['degree_of_the_crime']
    input_from_form.update({'degree_of_the_crime': degree_of_the_crime})

    degree_of_the_punishment = request.form['degree_of_the_punishment']
    input_from_form.update({'degree_of_the_punishment': degree_of_the_punishment})

    notes = request.form['notes']
    input_from_form.update({'notes': notes})

    arrest_site = request.form['arrest_site']
    input_from_form.update({'arrest_site': arrest_site})



    input_line.update({id: input_from_form}   )
    print(input_line)
    return home()




# this part vill serve the data into the new_record = Record()  

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
religion= input_from_form['residence']
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
degree_of_the_crime= input_from_form['degree_of_the_crime']
degree_of_the_punishment= input_from_form['degree_of_the_punishment']
notes= input_from_form['notes']
arrest_site= input_from_form['arrest_site']

# an option should be provided to verify the data in a new record right after the input. this will be optional. 

app.run(debug=True, port=5502)
