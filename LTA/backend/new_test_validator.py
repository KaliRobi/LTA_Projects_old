import re

# def is_three_dchar(val):
#     while not re.match(r"\b\d{1,3}\b|^Null$", str(val)):
#         val = input("please try again. This field takes max three digits or null!\n")
    


# val = input("What is the VOLUME? \n"),  # \d{3} # regardless of validness calls the function fix is needed.
# is_three_dchar(val)

def is_three_dchar(val):
    while not re.match(r"\b\d{1,3}\b|^Null$", str(val)):
            val = input("please try again. This field takes max three digits or null!\n")


val = input("What is the VOLUME? \n")
is_three_dchar(val)


def is_three_dchar(val):
    while not re.match(r"\b\d{1,3}\b|^Null$", str(val)):
            val = input("please try again. This field takes max three digits or null!\n")


val = input("What is the VOLUME? \n")
is_three_dchar(val)