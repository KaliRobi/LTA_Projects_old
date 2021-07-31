import re
#\d{4}-\d{2}.\d{2}


def is_date(val):
    val = "dummy123"  # something that doesn't validate
    while not re.match((r"\d{4}-\d{2}-\d{2}|^Null$"), val):
        val = input("Entered wrong data format please try (yyyy-mm-ddd) or Null \n")
    else:
        print("Dataformat valid")
        pass
#\w{4}


def is_three_wchar(value):
    value = "dummy123"
    while not re.match(r"\b\D{1,3}\b|^Null$", value):
        value = input("Please enter the correct format, in this field 3 word charaters or Null is allowed \n")
    else:
        print("dataformat valid")
        pass

#\d{3}#################
# def is_three_dchar(value):
#     value = "dummy123"
#     while not re.match(r"\b\d{1,3}\b|^Null$", value):
#         value = input("please try again. This field takes max three digits or null!\n")
#     else:
#         print("Valid format!")
#         pass

def is_three_dchar(val):
    while not re.match(r"\b\d{1,3}\b|^Null$", str(val)):
            val = input("please try again. This field takes max three digits or null!\n")

#\w


Volume = input("What is the VOLUME? \n"),  # \d{3} # regardless of validness calls the function fix is needed.
is_three_dchar(Volume)



ID = input("what is the ID: \n"),
Name_with_aliases = input("What is the NAME of the captive?\n"),
Sex = input("Sex of the captive?\n")  # \w
while not re.match(r"\bf\b|\bn\b", Sex):
    Sex = input("Please enter n for woman or f for man\n")
else:
    pass

Height_cm = input("Height?\n")  # \d{3}#################
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
Number_of_Children = input("Number of Children? \n")  # \d{3}#################
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
