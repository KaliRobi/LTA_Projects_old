from csv import reader

import psycopg2

conn = sqlite3.connect("LTA_NEW.db")

c = conn.cursor()

c.execute("CREATE TABLE IF NOT EXISTS lta_main(
    volume INTEGER NOT NULL,
    id INTEGER NOT NULL, 
    name_with_aliases TEXT,
    sex VARCHAR(1), 
    height_cm INTEGER, 
    build VARCHAR(3), 
    dentition VARCHAR(1), 
    special_peculiarities TEXT, 
    date_of_birth DATE, 
    place_of_birth VARCHAR(50), 
    place_of_residence VARCHAR(50), 
    Address VARCHAR(50), 
    Religion VARCHAR(2), 
    Childhood_status VARCHAR(2), 
    Marital_Status VARCHAR(50), 
    Number_of_Children INTEGER, 
    Occupation VARCHAR(50), 
    Occupation_2 VARCHAR(50), 
    Occupation_3 VARCHAR(50), 
    Military_Service VARCHAR(50), 
    Literacy VARCHAR(50),  
    Education VARCHAR(50), 
    Criminal_History VARCHAR(50), 
    crime VARCHAR(50), 
    Crime_Sentence_Begins DATE, 
    Sentence_Expires DATE, 
    Prison_Term_day INTEGER, 
    Ransome_Pengő_Fillér INTEGER, 
    Associates VARCHAR(50), 
    Degree_of_the_Crime VARCHAR(50), 
    Degree_of_the_Punishment VARCHAR(50), 
    Notes VARCHAR(150)
    Arrest_Site VARCHAR(50) 
);")




with open("lta.csv") as file:
    csv_reader = reader(file)
    cases = list(csv_reader)
    
    for case in cases:
        case[-1].replace(',', '')
        [f"'{item}'" for item in case]
        new_items = []
        for item in case:
            if len(item) < 1 or 'n.a':
                Null_item = "'Null'"
                new_items.append(Null_item)
            else:
                new_items.append(f"'{item}'")
            

        

            



        #print(new_items[2])
        whole_set = f" ({new_items[0]}, {new_items[1]}, {new_items[2]}, {new_items[3]}, {new_items[4]}, {new_items[5]}, {new_items[6]}, {new_items[7]}, {new_items[8]}, {new_items[9]}, {new_items[10]}, {new_items[11]}, {new_items[12]}, {new_items[13]}, {new_items[14]}, {new_items[15]}, {new_items[16]}, {new_items[17]}, {new_items[18]}, {new_items[19]}, {new_items[20]}, {new_items[21]}, {new_items[22]}, {new_items[23]}, {new_items[24]}, {new_items[25]}, {new_items[26]}, {new_items[27]}, {new_items[28]}, {new_items[29]}, {new_items[30]}, {new_items[31]}, {new_items[32]})"
        #print(whole_set)
        #print(f"INSERT INTO lta_main VALUES {whole_set}")
        c.execute(f"INSERT INTO lta_main VALUES {whole_set}")
        print('line was addedd to the LTA_main')
        #print(f"INSERT INTO lta_main VALUES {whole_set}")

        

conn.commit()

conn.close()



import psycopg2

conn = psycopg2.connect(
dbname = "lta_test",
user = "ltauser2",
host = "localhost",
password = "password"
)
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS lta_main(
    volume INTEGER NOT NULL,
    id INTEGER NOT NULL, 
    name_with_aliases TEXT,
    sex VARCHAR(1), 
    height_cm INTEGER, 
    build VARCHAR(3), 
    dentition VARCHAR(1), 
    special_peculiarities TEXT, 
    date_of_birth DATE, 
    place_of_birth VARCHAR(50), 
    place_of_residence VARCHAR(50), 
    Address VARCHAR(50), 
    Religion VARCHAR(2), 
    Childhood_status VARCHAR(2), 
    Marital_Status VARCHAR(50), 
    Number_of_Children INTEGER, 
    Occupation VARCHAR(50), 
    Occupation_2 VARCHAR(50), 
    Occupation_3 VARCHAR(50), 
    Military_Service VARCHAR(50), 
    Literacy VARCHAR(50),  
    Education VARCHAR(50), 
    Criminal_History VARCHAR(50), 
    crime VARCHAR(50), 
    Crime_Sentence_Begins DATE, 
    Sentence_Expires DATE, 
    Prison_Term_day INTEGER, 
    Ransome_Pengő_Fillér INTEGER, 
    Associates VARCHAR(50), 
    Degree_of_the_Crime VARCHAR(50), 
    Degree_of_the_Punishment VARCHAR(50), 
    Notes VARCHAR(150),
    Arrest_Site VARCHAR(50) 
);")



commands = (
        """
        CREATE TABLE test_table (
            data_id SERIAL PRIMARY KEY,
            data_name VARCHAR(255) NOT NULL,
            data_location VARCHAR(255) NOT NULL,
            data_height VARCHAR(255) NOT NULL
        )
        """)
data = (
    """
    Insert into test_table("1", "nem", "annyira", "miert?")
    """
)
cur.execute(commands)
cur.execute(data)
cur.close()
conn.commit()

create table another_table(id serial primary key, name varchar(255), data_of_birth date);
insert into another_table values( '1', 'Seres Zsuzsa', '1925-25-15');