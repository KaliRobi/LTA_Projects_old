import re


def is_date(val):
    val = '1'  # something that doesn't validate
    while not re.match((r"\d{4}-\d{2}.\d{2}"), val):
        val = input("Entered wrong data format please try (yyyy-mm-ddd) \n")
    else:
        print("Dataformat valid")


date = input("inp?\n")
if re.match((r"\d{4}-\d{2}.\d{2}"), date) == None:
    is_date(date)
else:
    pass


# is_date(date)
