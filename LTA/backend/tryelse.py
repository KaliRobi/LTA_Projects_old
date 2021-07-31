
import re



# def is_date(val):
#         val = '1'  #something that doesn't validate
#         while not re.match((r"\d{4}-\d{2}.\d{2}"), val):
#             val = input("Entered wrong data format please try (yyyy-mm-ddd) \n")
#         else:
#             print("Dataformat valid")
    

# #print(re.match(r"\d{4}-\d{2}.\d{2}", date))


# date = input("inp?\n")
# if re.match((r"\d{4}-\d{2}.\d{2}"), date) == None:
#     is_date(date)
# else:
#     pass


# #is_date(date)

sex = input("Sex of the captive?\n")

def is_these(val):
    while not re.match((r"\b([f]|[n]){1}"), val):
        val = input("please enter n or f \n")
    

print(is_these(sex))