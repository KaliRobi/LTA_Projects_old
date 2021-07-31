import psycopg2
from csv import reader




with open('lta.csv') as f:
    thefile = reader(f)
    for cases in thefile:      
        db_clear = ['Null' if case == ''  else case for case in cases ]
        db_clear = ['Null' if case == 'na' else case for case in db_clear]
        db_clear = ['Null' if case == 'NA' else case for case in db_clear]
        db_clear = ['Null' if case == 'N.A' else case for case in db_clear]
        db_clear = ['Null' if case == 'n.a' else case for case in db_clear]
        


        print(db_clear)






  # new_line = []
        # for i in range(len(cases)):
        #     if cases[i] == '':
        #         cases[i] = 'Null'
        #         new_line.append(cases[i])
        #     else:
        #         cases[i] = cases[i]
        #         new_line.append(cases[i])
        # print(new_line)