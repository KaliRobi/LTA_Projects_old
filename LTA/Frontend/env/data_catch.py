from flask import Flask, request, render_template


app = Flask(__name__, template_folder='../templates/')


@app.route('/')
def home():
    return render_template("input.html")

input_from_form  = {'volume': '', 'id': '', 'name_with_aliases': '', 'sex': '', 'height_cm': '', 'build': '', 'dentition': '', 'special_peculiarities': '', 'date_of_birth': '', 'place_of_birth': '', 'place_of_residence': '', 'residence': '', 'religion': '', 'childhood_status': '', 'marital_status': '', 'number_of_children': '',
                'occupation': '', 'occupation_2': '', 'occupation_3': '', 'military_service': '', 'literacy': '',  'education': '', 'criminal_history': '', 'crime': '', 'sentence_begins': '', 'sentence_expires': '', 'prison_term': '', 'ransome': '', 'associates': '', 'degree_crime': '', 'degree_punishment': '', 'notes': '', 'arrest_site': ''}


@app.route('/post_data', methods=['POST'])
def post_data():
    volume = request.form['volume']
    input_from_form.update({'volume': volume})

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

    prison_term = request.form['prison_term']
    input_from_form.update({'prison_term': prison_term})

    ransome = request.form['ransome']
    input_from_form.update({'ransome': ransome})

    associates = request.form['associates']
    input_from_form.update({'associates': associates})

    degree_crime = request.form['degree_crime']
    input_from_form.update({'degree_crime': degree_crime})

    degree_punishment = request.form['degree_punishment']
    input_from_form.update({'degree_punishment': degree_punishment})

    notes = request.form['notes']
    input_from_form.update({'notes': notes})

    arrest_site = request.form['arrest_site']
    input_from_form.update({'arrest_site': arrest_site})

    return input_from_form


app.run(debug=True, port=5502)
