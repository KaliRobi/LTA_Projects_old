import psycopg2

volume = input("What is the VOLUME? \n")  
id = input("what is the ID: \n")
name_with_aliases = input("What is the NAME of the captive?\n")
sex = input("Sex of the captive?\n")
height_cm = input("Height?\n")  
build = input("Build? \n")  
dentition = input("Dentition? \n")  
special_peculiarities = input("Any Special Peculiarities? \n")



class Record:
    def __init__(self, volume, id, name_with_aliases, sex, height_cm, build, dentition, special_peculiarities):
        self.volume = volume 
        self.id = id
        self.name_with_aliases = name_with_aliases 
        self.sex = sex
        self.height_cm  =  height_cm 
        self.build  = build 
        self.dentition = dentition
        self.special_peculiarities = special_peculiarities
        print(self.volume, self.id, self.name_with_aliases)


new_record = Record(volume, id, name_with_aliases, sex, height_cm, build, dentition, special_peculiarities)
print(new_record.volume, new_record.id, new_record.name_with_aliases)


def databse():
    print('Connecting... ')
    try:
        conn = psycopg2.connect(
        dbname = "lta_test",
        user = "ltauser2",
        host = "localhost",
        password = "Terve1990+"
        )
        c = conn.cursor()
        print('Making sure the table is there...')
        c.execute("""CREATE TABLE IF NOT EXISTS sec_lta_main (
            volume INTEGER NOT NULL,
            id VARCHAR(15) NULL, 
            name_with_aliases TEXT,
            sex VARCHAR(1), 
            height_cm INTEGER, 
            build VARCHAR(3), 
            dentition VARCHAR(1), 
            special_peculiarities TEXT);""")
        print('Table is ready.')
        c.close()
        conn.commit()
    except:
        raise EnvironmentError(" Connection has failed ")

def insert_into(val):
    try:
        conn = psycopg2.connect(
            dbname = "lta_test",
            user = "ltauser2",
            host = "localhost",
            password = "Terve1990+"
            )
        c = conn.cursor()
        row = (f"INSERT INTO sec_lta_main VALUES('{val.volume}', '{val.id}', '{val.name_with_aliases}', '{val.sex}', '{val.height_cm}', '{val.build}',  '{val.dentition}',  '{val.special_peculiarities}');")
        print(f'{val.volume}')
        print(row)
        c.execute(row)
        print('row is insterted into the databse')
        c.close()
        conn.commit()
    except:
        raise EnvironmentError('smt went wrong...')


print(new_record.height_cm)

databse()
insert_into(new_record)
print('job is done ')









