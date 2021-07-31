import re


# functions for data validation with regexp

# for date
def is_date(val):
    val = "dummy123"
    while not re.match((r"\d{4}-\d{2}-\d{2}|^Null$"), val):
        val = input(
            "Entered wrong data format please try (yyyy-mm-ddd) or Null \n")
    else:
        print("Dataformat valid")
        pass
#\w{4}

# to check if there is only three word chars or Null


def is_three_wchar(value):
    value = "dummy123"
    while not re.match(r"\b\D{1,3}\b|^Null$", value):
        value = input(
            "Please enter the correct format, in this field 3 word charaters or Null is allowed \n")
    else:
        print("dataformat valid")
        pass

# to check if there is only there digits or null


def is_three_dchar(value):
    value = "dummy123"
    while not re.match(r"\b\d{1,3}\b|^Null$", value):
        value = input(
            "please try again. This field takes max three digits or null!\n")
    else:
        print("Valid format!")
        pass


# ro check if there is only one word chars of null

# class for each record, each captive has 31 properties. The calss will make the the sql execution easier as the data is oragnised already.
class Record:
    def __init__(self, Volume, ID, Name_with_aliases, Sex, Height_cm, Build, Dentition, Special_Peculiarities, Date_of_Birth, Place_of_Birth, Place_of_Residence, Address, Religion, Childhood_status, Marital_Status, Number_of_Children, Occupation, Occupation_2, Occupation_3, Military_Service, Literacy,  Education, Criminal_History,  Crime_Sentence_Begins, Sentence_Expires, Prison_Term_day, Ransome, Associates, Degree_of_the_Crime, Degree_of_the_Punishment, Notes_Arrest_Site):
        self.Volume = Volume,
        self.ID = ID,
        self.Name_with_aliases = Name_with_aliases,
        self.Sex = Sex,
        self.Height_cm = Height_cm,
        self.Build = Height_cm,
        self.Dentition = Dentition,
        self.Special_Peculiarities = Special_Peculiarities,
        self.Date_of_Birth = Date_of_Birth,
        self.Place_of_Birth = Place_of_Birth,
        self.Place_of_Residence = Place_of_Residence,
        self.Address = Address,
        self.Religion = Religion,
        self.Childhood_status = Childhood_status,
        self.Marital_Status = Marital_Status,
        self.Number_of_Children = Marital_Status,
        self.Occupation = Occupation,
        self.Occupation_2 = Occupation_2,
        self.Occupation_3 = Occupation_3,
        self.Military_Service = Military_Service,
        self.Literacy = Literacy,
        self.Education = Education,
        self.Criminal_History = Criminal_History,
        self.Crime_Sentence_Begins = Criminal_History,
        self.Sentence_Expires = Sentence_Expires,
        self.Prison_Term_day = Prison_Term_day,
        self.Ransome = Ransome,
        self.Associates = Associates,
        self.Degree_of_the_Crime = Degree_of_the_Crime,
        self.Degree_of_the_Punishment = Degree_of_the_Punishment,
        self.Notes_Arrest_Site = Degree_of_the_Punishment


# every each new record should have a method verify whith option to overwrite
    def show_record(self,):
        pass

    def verify_data(self):
        pass
# every each new record shuld have a new mehod called execute


# all the input should be callable at once


# create a workflow which creates gets the data.

# inputs


# when it is ok, pass it to the database


# \d{3} # ISSUE: regardless of validness calls the function fix is needed.
Volume = input("What is the VOLUME? \n"),
if re.match(r"\b\d{1,3}\b|^Null$", Volume) == None:
    is_three_dchar(Volume)
else:
    pass

ID = input("what is the ID: \n"),
Name_with_aliases = input("What is the NAME of the captive?\n"),
Sex = input("Sex of the captive?\n")  # \w
while not re.match(r"\bf\b|\bn\b", Sex):  # checks if the info is .
    Sex = input("Please enter n for woman or f for man\n")
else:
    pass

Height_cm = input("Height?\n")  # \d{3}
if re.match(r"\b\d{1,3}\b|^Null$", Height_cm) == None:
    is_three_dchar(Height_cm)
else:
    pass

Build = input("Build? \n")  # \w{3}
if re.match(r"\b\D{1,3}\b", Build) == None:
    is_three_wchar(Build)
else:
    pass


Dentition = input("Dentition? \n")  # \w
Special_Peculiarities = input("Any Special Peculiarities? \n")
Date_of_Birth = input("Date of Birth? \n")
if re.match((r"\d{4}-\d{2}-\d{2}"), Date_of_Birth) == None:
    is_date(Date_of_Birth)
else:
    pass
Place_of_Birth = input("Place of Birth? \n")
Place_of_Residence = input("Place of Residence? \n")
Address = input("Address? \n"),
Religion = input("Religion? \n")  # \w{3}
if re.match(r"\b\D{1,3}\b", Religion) == None:
    is_three_wchar(Religion)
else:
    pass
Childhood_status = input("Childhood status? \n")  # \w
Marital_Status = input("Marital Status? \n")  # \w{3}
if re.match(r"\b\D{1,3}\b", Marital_Status) == None:
    is_three_wchar(Marital_Status)
else:
    pass
Number_of_Children = input("Number of Children? \n")  # \d{3}
if re.match(r"\b\d{1,3}\b|^Null$", Number_of_Children) == None:
    is_three_dchar(Number_of_Children)
else:
    pass

Occupation = input("Occupation? \n")
# this should be pulled out from a pool based on occupation
Occupation_2 = input("Occupation 2? \n")
# this needs to be pulled out from a pool based on occupation
Occupation_3 = input("Occupation 3? \n")
Military_Service = input("Military Service? \n")
Literacy = input("Literacy? \n")  # \w
Education = input("Education \n")
Criminal_History = input("Criminal History? \n")
Crime_Sentence_Begins = input("Crime Sentence Begins? \n")
if re.match((r"\{4}-\d{2}-\d{2}"), Crime_Sentence_Begins) == None:
    is_date(Crime_Sentence_Begins)
else:
    pass
Sentence_Expires = input("Sentence Expires? \n")
if re.match((r"\d{4}-\d{2}-\d{2}"), Sentence_Expires) == None:
    is_date(Sentence_Expires)
else:
    pass
is_date(Sentence_Expires)
Prison_Term_day = input("Prison Term day? \n")
Ransome = input("Ransome? \n")
Associates = input("Associates? \n")
Degree_of_the_Crime = input("Degree of the Crime? \n")  # \w{3}
if re.match(r"\b\D{1,3}\b", Degree_of_the_Crime) == None:
    is_three_wchar(Degree_of_the_Crime)
else:
    pass
Degree_of_the_Punishment = input("Degree of the Punishment? \n")  # \w{3}
if re.match(r"\b\D{1,3}\b", Degree_of_the_Crime) == None:
    is_three_wchar(Degree_of_the_Crime)
else:
    pass
Notes_Arrest_Site = input("Degree of the Punishment? \n")
# create the new Record
new_record = Record(Volume, ID, Name_with_aliases, Sex, Height_cm, Build, Dentition, Special_Peculiarities, Date_of_Birth, Place_of_Birth, Place_of_Residence, Address, Religion, Childhood_status, Marital_Status, Number_of_Children, Occupation, Occupation_2, Occupation_3, Military_Service, Literacy,  Education, Criminal_History,  Crime_Sentence_Begins, Sentence_Expires, Prison_Term_day, Ransome, Associates, Degree_of_the_Crime, Degree_of_the_Punishment, Notes_Arrest_Site.
