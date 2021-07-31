import re
import psycopg2


# functions for data validation with regexp
# class for data validation?

# for date
def is_date(val):
    while not re.match((r"\d{4}-\d{2}-\d{2}|^Null$"), val):
        val = input(
            "Entered wrong data format please try (yyyy-mm-ddd) or Null \n")

# to check if there is only three word chars or Null


def is_three_wchar(value):
    while not re.match(r"\b\D{1,3}\b|^Null$", value):
        value = input(
            "Please enter the correct format, in this field 3 word charaters or Null is allowed \n")


def is_sex(val):
    while not re.match((r"\b([f]|[n])\b|^Null$"), val):
        val = input("Please enter n or f \n")


def is_dentition(val):
    while not re.match((r"\b([é]|[h])\b|^Null$"), val):
        val = input("Please enter é or h \n")


def is_childhood(val):
    pass
    # while not re.match((r"\b([t]|[tt])\b|^Null$"), val):
    #     val = input("please enter t or according to the documentation  \n") # not working


def is_id(val):
    while not re.match((r"\b\d{4}-\d{0,8}\b|^Null$"), val):
        val = input(
            "Year and serial number on the left upper corner of the record \n")


def is_literacy(val):
    while not re.match((r"\b([io]|[nt])\b|^Null$"), val):
        val = input("This filed accepts  io, nt or Null  \n")  # bug, takes the value, the function still alerts and moves on only with Null


def is_ransome(val):
    while not re.match((r"\d{0,8}\b|^Null$"), val):
        val = input("The summ of the ransome, takes 0-8 digits \n")


def is_religion(val):
    while not re.match(
            (r"\b(gk)\b|\be\b|\bb\b|\bi\b|\b(lu)\b|\br\b|\b(rk)\b|\bu\b|\b(fn)\b|^Null$"), val):
        val = input(
            "Incorrect input, if you are not sure what are the keys for each religion, please check the documentation \n")


def is_three_dchar(val):
    while not re.match(r"\b\d{1,3}\b|^Null$", str(val)):
        val = input(
            "Please try again. This field takes max three digits or Nll!\n")



    
    

build = input("Build? \n")
is_three_wchar(build)

dentition = input("Dentition? \n")  # \w
is_dentition(dentition)

special_peculiarities = input("Any Special Peculiarities? \n")
# plain text allowed. the description about tattoos, scars and other

date_of_birth = input("Date of Birth? \n")
is_date(date_of_birth)


place_of_birth = input("Place of Birth? \n")
# here only word character should be allowed

place_of_residence = input("Place of Residence? \n")
# here only word character should be allowed


residence = input("Address? \n")
# plain text because the formating is also diverse


religion = input("Religion? \n")
is_religion(religion)


childhood_status = input("Childhood status? \n")  # \w
is_childhood(childhood_status)


marital_status = input("Marital Status? \n")
is_three_wchar(marital_status)

number_of_children = input("Number of Children? \n")
is_three_dchar(number_of_children)


occupation = input("Occupation? \n")


occupation_2 = input("Occupation 2? \n")
# this needs to be pulled out from a pool based on occupation

occupation_3 = input("Occupation 3? \n")
# this should be pulled out from a pool based on occupation


military_service = input("Military Service? \n")


literacy = input("Literacy? \n")  # \w
is_literacy(literacy)


education = input("Education \n")
# not specified

criminal_history = input("Criminal History? \n")

crime = input("committed crime? \n")


sentence_begins = input("Crime Sentence Begins? \n")
is_date(sentence_begins)

sentence_expires = input("Sentence Expires? \n")
is_date(sentence_expires)

prison_term_day = input("Prison Term day? \n")

ransome = input("Ransome? \n")
is_ransome(ransome)

associates = input("Associates? \n")

degree_of_the_crime = input("Degree of the Crime? \n")
is_three_wchar(degree_of_the_crime)

degree_of_the_punishment = input("Degree of the Punishment? \n")
is_three_wchar(degree_of_the_crime)

notes = input("any notes - 150 - char? \n")

arrest_site = input("The location where the prisoner got arrested: \n")
# create the new Record
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
    degree_of_the_crime,
    degree_of_the_punishment,
    notes,
    arrest_site)

# creates a visualised json file where we can correct error. the table
# filds  will be associated with the keys so user can easily modify them


# postgresql
# connecting to the databse and verifing the existence of the databes, if
# does not exists it creates it
def database():
    print('Connecting... ')
    try:
        conn = psycopg2.connect(
            dbname="lta_test",
            user="ltauser2",
            host="localhost",
            password="Terve1990+"
        )
        c = conn.cursor()
        print('Making sure the table is there...')
        c.execute("""CREATE TABLE IF NOT EXISTS sec_lta_main (
            LTAuser VARCHAR, NOT NULL,
            volume INTEGER NOT NULL,
            id VARCHAR(15) NOT NULL,
            name TEXT,
            sex VARCHAR(1),
            height INTEGER,
            build VARCHAR(3),
            dentition VARCHAR(1),
            special_peculiarities TEXT,
            date_of_birth DATE,
            place_of_birth VARCHAR(50),
            place_of_residence VARCHAR(50),
            residence VARCHAR(50),
            religion VARCHAR(2),
            childhood_status VARCHAR(2),
            marital_status VARCHAR(50),
            number_of_children INTEGER,
            occupation VARCHAR(50),
            occupation_2 VARCHAR(50),
            occupation_3 VARCHAR(50),
            military_service VARCHAR(50),
            literacy VARCHAR(50),
            education VARCHAR(50),
            criminal_history VARCHAR(50),
            crime VARCHAR(50),
            sentence_begins DATE,
            sentence_expires DATE,
            prison_term_day INTEGER,
            ransome INTEGER,
            associates VARCHAR(50),
            degree_of_the_crime VARCHAR(50),
            degree_of_the_punishment VARCHAR(50),
            notes VARCHAR(150),
            arrest_site VARCHAR(50)
        );""")
        print('Table is ready.')
        c.close()
        conn.commit()
    except BaseException:
        raise EnvironmentError(" Connection has failed ")
# when the table is there we can reconnect when ever a new record gets
# pushed to the databse


def insert_into(val):
    try:
        conn = psycopg2.connect(
            dbname="lta_test",
            user="ltauser2",
            host="localhost",
            password="Terve1990+"
        )
        c = conn.cursor()
        row = (f"INSERT INTO sec_lta_main VALUES('{LTAuser}','{val.volume}', '{val.id}', '{val.name}', '{val.sex}', '{val.height}', '{val.build}',  '{val.dentition}',  '{val.special_peculiarities}', '{val.date_of_birth}', '{val.place_of_birth}', '{val.place_of_residence}', '{val.residence}', '{val.religion}',  '{val.childhood_status}',  '{val.marital_status}', '{val.number_of_children}', '{val.occupation}', '{val.occupation_2}', '{val.occupation_3}', '{val.military_service}', '{val.literacy}',  '{val.education}', '{val.criminal_history}', '{val.crime}', '{val.sentence_begins}' , '{val.sentence_expires}', '{val.prison_term_day}', '{val.ransome}', '{val.associates}', '{val.degree_of_the_crime}', '{val.degree_of_the_punishment}', '{val.notes}','{val.arrest_site}');")
        print(row)
        c.execute(row)
        print('row is insterted into the databse')
        c.close()
        conn.commit()
    except BaseException:
        raise EnvironmentError(
            'This record was not inserted to the database...')



#if not correct, here can reassign entering the fileld name
def modify_hash(dicts):
    wrong_key = input(
        "which values are wrong, please enter the key(filed)? \n")
    wrong_val = check_hash[wrong_key]
    check_hash[wrong_key] = input(f"{wrong_key} is {wrong_val} now, it should be : \n")

#user decides if the dictionary is correct, if it is, then we continue to enter the data to the database
def correction(val):
    while val != 'yes':
        modify_hash(check_hash)
        val = input("all the data is correct? \n")

#start to bild the hash table which will provide option fast data correction
record_hash_keys = ['volume', 'id', 'name', 'sex', 'height', 'build', 'dentition', 'special_peculiarities', 'date_of_birth', 'place_of_birth', 'place_of_residence', 'residence', 'religion', 'childhood_status', 'marital_status', 'number_of_children', 'occupation',
               'occupation_2', 'occupation_3', 'military_service', 'literacy',  'education', 'criminal_history', 'crime', 'sentence_begins', 'sentence_expires', 'prison_term_day', 'ransome', 'associates', 'degree_of_the_crime', 'degree_of_the_punishment', 'notes', 'arrest_site']
dict_of_record_keys = dict.fromkeys(record_hash_keys)

# getting the values of the keys in one list 
record_hash_vals = [volume, id, name, sex, height, build, dentition, special_peculiarities, date_of_birth, place_of_birth, place_of_residence, residence, religion, childhood_status, marital_status, number_of_children, occupation,
                 occupation_2, occupation_3, military_service, literacy, education, criminal_history, crime, sentence_begins, sentence_expires, prison_term_day, ransome, associates, degree_of_the_crime, degree_of_the_punishment, notes, arrest_site]

#ziping it together
check_hash = {k: v for k, v in zip(dict_of_record_keys, record_hash_vals)}


#in this cli version the user gets the dictionary in the terminal, when the gui ready there will be a table, and should be able to manually correct the data there 
print(check_hash)
visual_check = input("all the data s correct? \n")
correction(visual_check)
print(check_hash)


if new_record.volume != check_hash['volume']:
    new_record.set_volume = check_hash['volume']

if new_record.id != check_hash['id']:
    new_record.set_id = check_hash['id']

if new_record.sex!= check_hash['sex']:
    new_record.set_sex = check_hash['sex']

if new_record.height!= check_hash['height']:
    new_record.set_height = check_hash['height']

if new_record.build!= check_hash['build']:
    new_record.set_build= check_hash['build']

if new_record.dentition != check_hash['dentition']:
    new_record.set_dentition= check_hash['dentition']

if new_record.special_peculiarities != check_hash['special_peculiarities']:
    new_record.set_special_peculiarities= check_hash['special_peculiarities']

if new_record.date_of_birth!= check_hash['date_of_birth']:
    new_record.set_date_of_birth = check_hash['date_of_birth']

if new_record.place_of_birth!= check_hash['place_of_birth']:
    new_record.set_place_of_birth = check_hash['place_of_birth']

if new_record.place_of_residence != check_hash['place_of_residence']:
    new_record.set_place_of_residence = check_hash['place_of_residence']

if new_record.residence != check_hash['residence']:
    new_record.set_residence= check_hash['residence']

if new_record.religion != check_hash['religion']:
    new_record.set_religion= check_hash['religion']

if new_record.childhood_status!= check_hash['childhood_status']:
    new_record.set_childhood_status = check_hash['childhood_status']

if new_record.marital_status!= check_hash['marital_status']:
    new_record.set_marital_status = check_hash['marital_status']

if new_record.number_of_children!= check_hash['number_of_children']:
    new_record.set_number_of_children = check_hash['number_of_children']

if new_record.occupation != check_hash['occupation']:
    new_record.set_occupation = check_hash['occupation']

if new_record.occupation_2 != check_hash['occupation_2']:
    new_record.set_occupation_2= check_hash['occupation_2']

if new_record.occupation_3 != check_hash['occupation_3']:
    new_record.set_occupation_3= check_hash['occupation_3']

if new_record.military_service != check_hash['military_service']:
    new_record.set_military_service= check_hash['military_service']

if new_record.literacy != check_hash['literacy']:
    new_record.set_literacy= check_hash['literacy']


if new_record.education!= check_hash['education']:
    new_record.set_education = check_hash['education']

if new_record.criminal_history!= check_hash['criminal_history']:
    new_record.set_criminal_history = check_hash['criminal_history']

if new_record.crime!= check_hash['crime']:
    new_record.set_crime = check_hash['crime']

if new_record.sentence_begins != check_hash['sentence_begins']:
    new_record.set_sentence_begins= check_hash['sentence_begins']

if new_record.sentence_expires != check_hash['sentence_expires']:
    new_record.set_sentence_expires= check_hash['sentence_expires']

if new_record.prison_term_day!= check_hash['prison_term_day']:
    new_record.set_prison_term_day = check_hash['prison_term_day']

if new_record.ransome!= check_hash['ransome']:
    new_record.set_ransome = check_hash['ransome']

if new_record.associates!= check_hash['associates']:
    new_record.set_associates = check_hash['associates']

if new_record.degree_of_the_crime != check_hash['degree_of_the_crime']:
    new_record.set_degree_of_the_crime= check_hash['degree_of_the_crime']

if new_record.degree_of_the_punishment!= check_hash['degree_of_the_punishment']:
    new_record.set_degree_of_the_punishment = check_hash['degree_of_the_punishment']

if new_record.arrest_site!= check_hash['arrest_site']:
    new_record.set_arrest_site = check_hash['arrest_site']

if new_record.notes!= check_hash['notes']:
    new_record.set_notes = check_hash['notes']

#at this point the data in the record should be correct 

database()
insert_into(new_record)
