import psycopg2
import re

def is_date(val):
    while not re.match((r"\d{4}-\d{2}-\d{2}|^Null$"), val):
        val = input("Entered wrong data format please try (yyyy-mm-ddd) or Null \n")
    
# to check if there is only three word chars or Null
def is_three_wchar(value):
    while not re.match(r"\b\D{1,3}\b|^Null$", value):
        value = input("Please enter the correct format, in this field 3 word charaters or Null is allowed \n")
   
def is_sex(val):
    while not re.match((r"\b([f]|[n])\b|^Null$"), val):
        val = input("please enter n or f \n")

def is_dentition(val):
    while not re.match((r"\b([é]|[h])\b|^Null$"), val):
        val = input("please enter é or h \n")

def is_childhood(val):
    while not re.match((r"\b([t]|[tt])\b|^Null$"), val):
        val = input("please enter t or tt according to the documentation  \n")
def is_id(val):
    while not re.match((r"\b\d{4}-\d{0,8}\b|^Null$"), val):
        val = input("year and serial number on the left upper corner of the record \n")

def is_literacy(val):
    while not re.match((r"\b([io]|[nt])\b|^Null$"), val):
        val = input("This filed accepts  io, nt or Null  \n")

def is_ransome(val):
    while not re.match((r"\d{0,8}\b|^Null$"), val):
        val = input("the summ of the ransome, takes 0-8 digits \n")

def is_religion(val):
    while not re.match((r"\b(gk)\b|\be\b|\bb\b|\bi\b|\b(lu)\b|\br\b|\b(rk)\b|\bu\b|\b(fn)\b|^Null$"), val):
        val = input("incorrect input, if you are not sure what are the keys for each realigion, please check the documentation \n")


def is_three_dchar(val):
    while not re.match(r"\b\d{1,3}\b|^Null$", str(val)):
            val = input("please try again. This field takes max three digits or null!\n")
    

volume = input("What is the VOLUME? \n")  
is_three_dchar(volume)


id = input("what is the ID: \n")
is_id(id)

name_with_aliases = input("What is the NAME of the captive?\n")

sex = input("Sex of the captive?\n")
is_sex(sex)

height_cm = input("Height?\n")  
is_three_dchar(height_cm)

build = input("Build? \n")  
is_three_wchar(build)

dentition = input("Dentition? \n")  # \w
is_dentition(dentition)

special_peculiarities = input("Any Special Peculiarities? \n")
# plain text allowed. the description about tattoos, scars and other physical peculiarities are varying.

date_of_birth = input("Date of Birth? \n")
is_date(date_of_birth)


place_of_birth = input("Place of Birth? \n")  
# here only word character should be allowed 

place_of_residence = input("Place of Residence? \n")
# here only word character should be allowed 



residence = input("Address? \n")
#plain text because the formating is also diverse


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

crime= input("committed crime? \n")


crime_sentence_begins = input("Crime Sentence Begins? \n")
is_date(crime_sentence_begins)

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



class Record:
    def __init__(self, volume, id, name_with_aliases, sex, height_cm, build, dentition, special_peculiarities, date_of_birth, place_of_birth, place_of_residence,residence, religion, childhood_status, marital_status, number_of_children, occupation, occupation_2, occupation_3, military_service, literacy,  education, criminal_history, crime, crime_sentence_begins, sentence_expires, prison_term_day, ransome, associates, degree_of_the_crime, degree_of_the_punishment, notes, arrest_site ):
        self.volume = volume  
        self.id = id
        self.name_with_aliases = name_with_aliases 
        self.sex = sex 
        self.height_cm  =  height_cm 
        self.build  = build 
        self.dentition = dentition 
        self.special_peculiarities = special_peculiarities
        self.date_of_birth = date_of_birth 
        self.place_of_birth = place_of_birth 
        self.place_of_residence = place_of_residence 
        self.residence=residence 
        self.religion = religion 
        self.childhood_status = childhood_status 
        self.marital_status = marital_status 
        self.number_of_children = number_of_children 
        self.occupation  = occupation 
        self.occupation_2 = occupation_2 
        self.occupation_3 = occupation_3 
        self.military_service = military_service 
        self.literacy = literacy  
        self.education = education 
        self.criminal_history = criminal_history  
        self.crime = crime
        self.crime_sentence_begins = crime_sentence_begins 
        self.sentence_expires = sentence_expires
        self.prison_term_day = prison_term_day
        self.ransome =  ransome
        self.associates = associates 
        self.degree_of_the_crime = degree_of_the_crime 
        self.degree_of_the_punishment = degree_of_the_punishment 
        self.notes = notes
        self.arrest_site = arrest_site
        


new_record = Record(volume, id, name_with_aliases, sex, height_cm, build, dentition, special_peculiarities, date_of_birth, place_of_birth, place_of_residence,residence, religion, childhood_status, marital_status, number_of_children, occupation, occupation_2, occupation_3, military_service, literacy,  education, criminal_history, crime, crime_sentence_begins, sentence_expires, prison_term_day, ransome, associates, degree_of_the_crime, degree_of_the_punishment, notes, arrest_site)



def databse():
    print('Connecting... ')
    try:
        conn = psycopg2.connect(
        dbname = "lta_test",
        user = "ltauser2",
        host = "localhost",
        password = "Terve1990+"
        )
        c = conn.cursor()
        print('Making sure the table is there...')
        c.execute("""CREATE TABLE IF NOT EXISTS sec_lta_main (
            volume INTEGER NOT NULL,
            id VARCHAR(15) NOT NULL, 
            name_with_aliases TEXT,
            sex VARCHAR(1), 
            height_cm INTEGER, 
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
            crime_sentence_begins DATE, 
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
    except:
        raise EnvironmentError(" Connection has failed ")



def insert_into(val):
    try:
        conn = psycopg2.connect(
            dbname = "lta_test",
            user = "ltauser2",
            host = "localhost",
            password = "Terve1990+"
            )
        c = conn.cursor()
        row = (f"INSERT INTO sec_lta_main VALUES('{val.volume}', '{val.id}', '{val.name_with_aliases}', '{val.sex}', '{val.height_cm}', '{val.build}',  '{val.dentition}',  '{val.special_peculiarities}', '{val.date_of_birth}', '{val.place_of_birth}', '{val.place_of_residence}', '{val.residence}', '{val.religion}',  '{val.childhood_status}',  '{val.marital_status}', '{val.number_of_children}', '{val.occupation}', '{val.occupation_2}', '{val.occupation_3}', '{val.military_service}', '{val.literacy}',  '{val.education}', '{val.criminal_history}', '{val.crime}', '{val.crime_sentence_begins}' , '{val.sentence_expires}', '{val.prison_term_day}', '{val.ransome}', '{val.associates}', '{val.degree_of_the_crime}', '{val.degree_of_the_punishment}', '{val.notes}','{val.arrest_site}');")
        print(row)
        c.execute(row)
        print('row is insterted into the databse')
        c.close()
        conn.commit()
    except:
        raise EnvironmentError('smt went wrong...')


print(new_record.height_cm)

databse()
insert_into(new_record)
print('job is done ')









