CREATE TABLE IF NOT EXISTS lta_main (
            volume INTEGER NOT NULL,
            id VARCHAR(15) PRIMARY KEY NOT NULL, 
            name TEXT,
            sex VARCHAR(4), 
            height INTEGER, 
            build VARCHAR(4), 
            dentition VARCHAR(4), 
            special_peculiarities TEXT, 
            date_of_birth DATE, 
            place_of_birth VARCHAR(50), 
            place_of_residence VARCHAR(50), 
            residence VARCHAR(100), 
            religion VARCHAR(4), 
            childhood_status VARCHAR(4), 
            marital_status VARCHAR(10), 
            number_of_children INTEGER, 
            occupation VARCHAR(60), 
            occupation_2 VARCHAR(115), 
            occupation_3 VARCHAR(60), 
            military_service VARCHAR(50), 
            literacy VARCHAR(4),  
            education VARCHAR(50), 
            criminal_history VARCHAR(400), 
            crime VARCHAR(100), 
            sentence_begins DATE, 
            sentence_expires DATE, 
            prison_term_day INTEGER, 
            ransome INTEGER, 
            associates VARCHAR(50), 
            degree_of_crime VARCHAR(10), 
            degree_of_punishment VARCHAR(10), 
            notes VARCHAR(500),
            arrest_site VARCHAR(50), 
            username VARCHAR(30) Not Null,
            record_session SERIAL NOT NULL,
            created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
        );