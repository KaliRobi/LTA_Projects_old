CREATE TABLE IF NOT EXISTS test_lta_main (
            serial SERIAL NOT NULL,
            volume INTEGER NOT NULL,
            id VARCHAR(15) PRIMARY KEY NOT NULL, 
            name TEXT,
            sex VARCHAR(1), 
            height INTEGER, 
            build VARCHAR(3), 
            dentition VARCHAR(1), 
            special_peculiarities TEXT, 
            date_of_birth DATE, 
            place_of_birth VARCHAR(50), 
            place_of_residence VARCHAR(50), 
            residence VARCHAR(50), 
            religion VARCHAR(2), 
            childhood_status VARCHAR(2), 
            marital_status VARCHAR(50), 
            number_of_children INTEGER, 
            occupation VARCHAR(50), 
            occupation_2 VARCHAR(50), 
            occupation_3 VARCHAR(50), 
            military_service VARCHAR(50), 
            literacy VARCHAR(50),  
            education VARCHAR(50), 
            criminal_history VARCHAR(50), 
            crime VARCHAR(50), 
            sentence_begins DATE, 
            sentence_expires DATE, 
            prison_term_day INTEGER, 
            ransome INTEGER, 
            associates VARCHAR(50), 
            degree_of_crime VARCHAR(50), 
            degree_of_punishment VARCHAR(50), 
            notes VARCHAR(300),
            arrest_site VARCHAR(50), 
            username VARCHAR(30) Not Null
        );