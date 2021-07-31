import re
def is_three_dchar(val):
    while not re.match(r"\b\d{1,3}\b|^Null$", str(val)):
            val = input("please try again. This field takes max three digits or null!\n")



volume = input("What is the VOLUME? \n")  # \d{3} 
is_three_dchar(volume)


