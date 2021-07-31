import re

def is_three_dchar(value):
    while not re.match(r"\b\d{1,3}\b|^Null$", str(value)):
        value = input("please try again. This field takes max three digits or null!\n")
    else:
        print("Valid format!")
        pass


Volume = input("What is the VOLUME? \n"),  # \d{3} # regardless of validness calls the function fix is needed.
if re.match(r"\b\d{1,3}\b|^Null$", str(Volume)) != None:
    pass
else:
    is_three_dchar(Volume)