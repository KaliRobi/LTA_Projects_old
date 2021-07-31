import psycopg2

conn = psycopg2.connect(
dbname = "lta_test",
user = "ltauser2",
host = "localhost",
password = "Terve1990+"
)
cur = conn.cursor()
commands = (
        """
        CREATE TABLE IF NOT EXISTS test_table (
            data_id SERIAL ,
            data_name VARCHAR(255) NOT NULL,
            data_location VARCHAR(255) NOT NULL,
            data_height VARCHAR(255) NOT NULL
        )
        """)
data = (
    """
    Insert into test_table values('7', 'nem', 'annyira', 'miert?')
    """
)



return_command = (
        """ 
        SELECT * from test_table;
        """
)



cur.execute(commands)
cur.execute(data)
cur.execute(return_command)
res = cur.fetchmany(size=3)
print(res)
cur.close()
conn.commit()


