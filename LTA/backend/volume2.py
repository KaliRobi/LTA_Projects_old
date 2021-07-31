import re


def is_it(val):
    while not re.match(r"\b\d{1,3}\b|^Null$", str(val)):
            val = input("val!\n")


val = input("val?\n")
is_it(val)



    











# t = input('is it?\n')
# b = is_value(t)
# print(b)