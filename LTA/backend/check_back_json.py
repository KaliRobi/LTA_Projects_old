import psycopg2
import re


volume = '1'
id = '1932-2545'
name = 'kovacs julianna'
sex = 'n'
date_of_birth = '1932-06-25'

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
record_hash_keys = ['volume', 'id', 'name_with_aliases', 'sex', 'height_cm', 'build', 'dentition', 'special_peculiarities', 'date_of_birth', 'place_of_birth', 'place_of_residence', 'residence', 'religion', 'childhood_status', 'marital_status', 'number_of_children', 'occupation',
               'occupation_2', 'occupation_3', 'military_service', 'literacy',  'education', 'criminal_history', 'crime', 'crime_sentence_begins', 'sentence_expires', 'prison_term_day', 'ransome', 'associates', 'degree_of_the_crime', 'degree_of_the_punishment', 'notes', 'arrest_site']
dict_of_record_keys = dict.fromkeys(record_hash_keys)

# getting the values of the keys in one list 
record_hash_vals = [volume, id, name_with_aliases, sex, height_cm, build, dentition, special_peculiarities, date_of_birth, place_of_birth, place_of_residence, residence, religion, childhood_status, marital_status, number_of_children, occupation,
                 occupation_2, occupation_3, military_service, literacy, education, criminal_history, crime, crime_sentence_begins, sentence_expires, prison_term_day, ransome, associates, degree_of_the_crime, degree_of_the_punishment, notes, arrest_site]

#ziping it together
check_hash = {k: v for k, v in zip(dict_of_record_keys, record_hash_vals)}


#in this cli version the user gets the dictionary in the terminal, when the gui ready there will be a table, and should be able to manually correct the data there 
print(check_hash)
visual_check = input("all the data s correct? \n")
correction(visual_check)
print(check_hash)

class Record:
    def __init__(self, volume, id, name_with_aliases, sex, height_cm, build, dentition, special_peculiarities, date_of_birth, place_of_birth, place_of_residence, residence, religion, childhood_status, marital_status, number_of_children, occupation,
                 occupation_2, occupation_3, military_service, literacy, education, criminal_history, crime, crime_sentence_begins, sentence_expires, prison_term_day, ransome, associates, degree_of_the_crime, degree_of_the_punishment, notes, arrest_site):
        self._volume = volume
        self._id = id
        self._name_with_aliases = name_with_aliases
        self._sex = sex
        self._height_cm = height_cm
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
        self._crime_sentence_begins = crime_sentence_begins
        self._sentence_expires = sentence_expires
        self._prison_term_day = prison_term_day
        self._ransome = ransome
        self._associates = associates
        self._degree_of_the_crime = degree_of_the_crime
        self._degree_of_the_punishment = degree_of_the_punishment
        self._arrest_site = arrest_site
        self._notes = notes
    # setter getter properties for the modificatiot

    @property
    def volume(self):
        return self._volume

    @volume.setter
    def set_volume(self, volume):
        self._volume = volume

    @property
    def id(self):
        return self._id

    @id.setter
    def set_id(self, id):
        self._id = id

    @property
    def name_with_aliases(self):
        return self._name_with_aliases

    @name_with_aliases.setter
    def set_name_with_aliases(self, name):
        self._name_with_aliases = name

    @property
    def sex(self):
        return self._sex

    @sex.setter
    def set_sex(self, sex):
        self._sex = sex

    @property
    def height_cm(self):
        return self._height_cm

    @height_cm.setter
    def set_height_cm(self, height_cm):
        self._height_cm = height_cm

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
        self._special_peculiarities = special_peculiarities

    @property
    def date_of_birth(self):
        return self._date_of_birth

    @date_of_birth.setter
    def set_date_of_birth(self, date_of_birth):
        self._date_of_birth = date_of_birth

    @property
    def place_of_residence(self):
        return self._place_of_residence

    @place_of_residence.setter
    def set_place_of_residence(self, place_of_residence):
        self._place_of_residence = place_of_residence

    @property
    def residence(self):
        return self._residence

    @place_of_residence.setter
    def set_residence(self, residence):
        self._residence = residence

    @property
    def religion(self):
        return self._religion

    @religion.setter
    def set_religion(self, religion):
        self._religion = religion

    @property
    def childhood_status(self):
        return self._childhood_status

    @childhood_status.setter
    def set_childhood_status(self, childhood_status):
        self._childhood_status = childhood_status

    @property
    def marital_status(self):
        return self._marital_status

    @marital_status.setter
    def set_marital_status(self, marital_status):
        self._marital_status = marital_status

    @property
    def marital_status(self):
        return self._marital_status

    @marital_status.setter
    def set_marital_status(self, marital_status):
        self._marital_status = marital_status

    @property
    def number_of_children(self):
        return self._number_of_children

    @number_of_children.setter
    def set_number_of_children(self, number_of_children):
        self._number_of_children = number_of_children

    @property
    def occupation(self):
        return self._occupation

    @occupation.setter
    def set_occupation(self, occupation):
        self._occupation = occupation

    @property
    def occupation_2(self):
        return self._occupation_2

    @occupation_2.setter
    def set_occupation_2(self, occupation_2):
        self._occupation_2 = occupation_2

    @property
    def occupation_3(self):
        return self._occupation_3

    @occupation_3.setter
    def set_occupation_3(self, occupation_3):
        self._occupation_3 = occupation_3

    @property
    def military_service(self):
        return self._military_service

    @military_service.setter
    def set_military_service(self, military_service):
        self._military_service = military_service

    @property
    def literacy(self):
        return self._literacy

    @literacy.setter
    def set_literacy(self, literacy):
        self._literacy = literacy

    @property
    def education(self):
        return self._education

    @education.setter
    def set_education(self, education):
        self._education = education

    @property
    def criminal_history(self):
        return self._criminal_history

    @criminal_history.setter
    def set_criminal_history(self, criminal_history):
        self._criminal_history = criminal_history

    @property
    def criminal_history(self):
        return self._criminal_history

    @criminal_history.setter
    def set_criminal_history(self, criminal_history):
        self._criminal_history = criminal_history

    @property
    def crime(self):
        return self._crime

    @crime.setter
    def set_crime(self, crime):
        self._crime = crime

    @property
    def crime_sentence_begins(self):
        return self._crime_sentence_begins

    @crime_sentence_begins.setter
    def crime_sentence_begins(self, crime_sentence_begins):
        self._crime_sentence_begins = crime_sentence_begins

    @property
    def sentence_expires(self):
        return self._sentence_expires

    @sentence_expiress.setter
    def sentence_expires(self, sentence_expires):
        self._sentence_expires = sentence_expires

    @property
    def prison_term_day(self):
        return self._prison_term_day

    @prison_term_day.setter
    def prison_term_day(self, prison_term_day):
        self._prison_term_day = prison_term_day

    @property
    def ransome(self):
        return self._ransome

    @ransome.setter
    def ransome(self, ransome):
        self._ransome = ransome

    @property
    def associates(self):
        return self._associates

    @associates.setter
    def associates(self, associates):
        self._associates = associates

    @property
    def degree_of_the_crime(self):
        return self._degree_of_the_crime

    @degree_of_the_crime.setter
    def associates(self, degree_of_the_crime):
        self._degree_of_the_crime = degree_of_the_crime

    @property
    def degree_of_the_punishment(self):
        return self._degree_of_the_punishment

    @degree_of_the_punishment.setter
    def degree_of_the_punishment(self, degree_of_the_punishment):
        self._degree_of_the_punishment = degree_of_the_punishment

    @property
    def arrest_site(self):
        return self._arrest_site

    @arrest_site.setter
    def arrest_site(self, arrest_site):
        self._arrest_site = arrest_site

    @property
    def notes(self):
        return self._notes

    @notes.setter
    def notes(self, notes):
        self._notes = notes


new_record = Record(volume, id, name, sex, date_of_birth)


print(new_record.volume)

if new_record.volume != check_hash['volume']:
    new_record.set_volume = check_hash['volume']

if new_record.id != check_hash['id']:
    new_record.set_id = check_hash['id']

if new_record.sex!= check_hash['sex']:
    new_record.set_sex = check_hash['sex']

if new_record.height_cm!= check_hash['height_cm']:
    new_record.set_height_cm = check_hash['height_cm']

if new_record.build!= check_hash['build']:
    new_record.set_build= check_hash['build']

if new_record.dentition != check_hash['dentition']:
    new_record.set_dentition= check_hash['dentition']

if new_record.special_peculiarities != check_hash['special_peculiarities']:
    new_record.set_special_peculiarities= check_hash['special_peculiarities']

if new_record.date_of_birt!= check_hash['date_of_birt']:
    new_record.date_of_birt = check_hash['date_of_birt']

if new_record.place_of_birth!= check_hash['place_of_birth']:
    new_record.set_place_of_birth = check_hash['place_of_birth']

if new_record.place_of_residen != check_hash['place_of_residen']:
    new_record.set_place_of_residen = check_hash['place_of_residen']

if new_record.residence != check_hash['residence']:
    new_record.set_residence= check_hash['residence']

if new_record.religion != check_hash['religion']:
    new_record.set_religion= check_hash['religion']

if new_record.childhood_status!= check_hash['childhood_status']:
    new_record.childhood_status = check_hash['childhood_status']

if new_record.marital_status!= check_hash['marital_status']:
    new_record.set_marital_status = check_hash['marital_status']

if new_record.number_of_children!= check_hash['number_of_children']:
    new_record.set_number_of_children = check_hash['number_of_children']

if new_record.occupation != check_hash['occupation']:
    new_record.set_occupation = check_hash['occupation']

if new_record.occupation_3 != check_hash['occupation_3']:
    new_record.set_occupation_3= check_hash['occupation_3']

if new_record.occupation_3 != check_hash['occupation_3']:
    new_record.set_occupation_3= check_hash['occupation_3']

if new_record.childhood_status!= check_hash['childhood_status']:
    new_record.childhood_status = check_hash['childhood_status']

if new_record.marital_status!= check_hash['marital_status']:
    new_record.set_marital_status = check_hash['marital_status']

if new_record.number_of_children!= check_hash['number_of_children']:
    new_record.set_number_of_children = check_hash['number_of_children']


if new_record.military_service != check_hash['military_service']:
    new_record.set_military_service= check_hash['military_service']

if new_record.literacy != check_hash['literacy']:
    new_record.set_literacy= check_hash['literacy']


if new_record.education!= check_hash['education']:
    new_record.education = check_hash['education']

if new_record.criminal_history!= check_hash['criminal_history']:
    new_record.set_criminal_history = check_hash['criminal_history']

if new_record.crime!= check_hash['crime']:
    new_record.set_crime = check_hash['crime']

if new_record.crime_sentence_begins != check_hash['crime_sentence_begins']:
    new_record.set_crime_sentence_begins= check_hash['crime_sentence_begins']

if new_record.sentence_expiresy != check_hash['sentence_expires']:
    new_record.set_sentence_expires= check_hash['sentence_expires']

if new_record.prison_term_day!= check_hash['prison_term_day']:
    new_record.prison_term_day = check_hash['prison_term_day']

if new_record.criminal_ransome!= check_hash['ransome']:
    new_record.set_ransome = check_hash['ransome']

if new_record.associates!= check_hash['associates']:
    new_record.set_associates = check_hash['associates']

if new_record.degree_of_the_crime != check_hash['degree_of_the_crime']:
    new_record.set_degree_of_the_crime= check_hash['degree_of_the_crime']

if new_record.degree_of_the_punishment!= check_hash['degree_of_the_punishment']:
    new_record.degree_of_the_punishment = check_hash['degree_of_the_punishment']

if new_record.arrest_site!= check_hash['arrest_site']:
    new_record.set_arrest_site = check_hash['arrest_site']

if new_record.notes!= check_hash['notes']:
    new_record.set_notes = check_hash['notes']
        
         
      
       








print(new_record.volume)
