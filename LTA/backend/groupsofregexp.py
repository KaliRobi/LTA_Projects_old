import re

date = input("date of Birth? \n")


# def is_under_three_wchar(val):
#     val = "1"
#     while not re.match(r"\b\D{1,4}\b", val):
#         val = input(" please enter the correct format, in this field 4 word charaters allowed \n")
#     else:
#         print("dataformat valid")
#         pass

# is_under_three_wchar(date)

def is_there_dchar(value):
    val = 'abd'
    while not re.match(r"\b\d{1,3}\b|^Null$", value):
        value = input("please try again. This field takes max three digits or null!\n")
    else:
        print("Valid format!")
        pass
is_there_dchar(date)

# def is_date(val):
#     val = '1'  # something that doesn't validate
#     while not re.match((r"\d{4}-\d{2}-\d{2}|^Null$"), val):
#         val = input("Entered wrong data format please try (yyyy-mm-ddd) \n")
#     else:
#         print("Dataformat valid")
#         pass
# is_date(date)


# print(item)

# def is_date(val):
#     	regex = re.compile(r"\d{4}-\d{2}.\d{2}")
#     	item = str(regex.search(date_of_Birth))
#     	val = "xy"
#     	print(item)


#     	while val not in item:
#     				print(item)
#         			#val = input("entered wrong data format please try (yyyy-mm-ddd) \n")

# is_date(date_of_Birth)


# 1

# date = 'aaaa'  #something that doesn't validate
# while not re.match(r"\b\D{1,3}\b", date):
#     date = input("Please enter your name: ")
#     print ("Error! Make sure you only use letters in your name")
# else:
#     print("Hello! "+ date)


# def is_three_words(val):
#     	val = "1"
# 	while not re.match(r"\b\D{1,4}\b", val):
#     		val = input(" please enter the correct format, in this max field 3 word charaters allowed \n")
# 	else:
#     		print("dataformat valid")

# is_three_words(date)


# def is_date(val):
#         val = '1'  #something that doesn't validate
#         while not re.match((r"\d{4}-\d{2}.\d{2}"), val):
#             val = input("Entered wrong data format please try (yyyy-mm-ddd) \n")
#         else:
#             print("Dataformat valid")

# is_date(date_of_Birth)
