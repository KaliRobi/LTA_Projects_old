from csv import reader
import sqlite3

conn = sqlite3.connect("LTA_NEW.db")

c = conn.cursor()

c.execute("CREATE TABLE IF NOT EXISTS lta_main (Volume TEXT, ID TEXT, Name_with_aliases TEXT, Sex TEXT, Height_cm INTEGER, Build TEXT, Dentition TEXT, Special_Peculiarities TEXT, Date_of_Birth INTEGER, Place_of_Birth TEXT, Place_of_Residence TEXT, Adress TEXT, Religion TEXT, Childhood_status TEXT, Marital_Status TEXT, Number_of_Children INTEGER, Occupation TEXT, Occupation_2 TEXT, Occupation_3 TEXT, Military_Service TEXT, Literacy TEXT,  Education TEXT, Criminal_History TEXT, crime TEXT, Crime_Sentence_Begins TEXT, Sentence_Expires TEXT, Prison_Term_day INTEGER, Ransome_Pengő_Fillér INTEGER, Associates TEXT, Degree_of_the_Crime TEXT, Degree_of_the_Punishment TEXT, Notes_Arrest_Site TEXT );")




with open("lta.csv") as file:
    csv_reader = reader(file)
    cases = list(csv_reader)
    
    for case in cases:
        case[-1].replace(',', '')
        [f"'{item}'" for item in case]
        #[item.replace(" ", "NA") for item in case]
        #[print(item, len(item)) for item in case]
        #print(case)
        #print(type(case))
        new_items = []
        for item in case:
            if len(item) < 1:
                #print('NA')
                eitem = "'NA'"
                new_items.append(eitem)
            else:
                #print(item)
                new_items.append(f"'{item}'")

        

            



        #print(new_items[2])
        whole_set = f" ({new_items[0]}, {new_items[1]}, {new_items[2]}, {new_items[3]}, {new_items[4]}, {new_items[5]}, {new_items[6]}, {new_items[7]}, {new_items[8]}, {new_items[9]}, {new_items[10]}, {new_items[11]}, {new_items[12]}, {new_items[13]}, {new_items[14]}, {new_items[15]}, {new_items[16]}, {new_items[17]}, {new_items[18]}, {new_items[19]}, {new_items[20]}, {new_items[21]}, {new_items[22]}, {new_items[23]}, {new_items[24]}, {new_items[25]}, {new_items[26]}, {new_items[27]}, {new_items[28]}, {new_items[29]}, {new_items[30]}, {new_items[30]})"
        #print(whole_set)
        #print(f"INSERT INTO lta_main VALUES {whole_set}")
        c.execute(f"INSERT INTO lta_main VALUES {whole_set}")
        print('line was addedd to the LTA_main')
        #print(f"INSERT INTO lta_main VALUES {whole_set}")

        

conn.commit()

conn.close()
        






