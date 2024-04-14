import mysql.connector

mydb = mysql.connector.connect(  host="localhost",  user="abc",  password="password")
print(mydb)

mycursor = mydb.cursor() #this will tell that we are pointing to this database.

mycursor.execute('create table IF NOT EXISTS GenAI.GenAI_new_data(col1 INT(10) ,col2 float(10,5),col3 float(10,5) ,col4 float(10,5) , col5 float(10,5),col6 float(10,5) ,clo7 float(10,5) , col8 float(10,5) , col9 float(10,5) , col10 float(10,5) , col11 INT(10)) ')

import csv
with open('./Queries/glass.data' , 'r') as f :
    glass_data = csv.reader(f, delimiter = '\n')
    for i in glass_data:
        print(i[0])

with open('./Queries/glass.data' , 'r') as f:
    glass_data=csv.reader(f,delimiter='\n')
    for i in glass_data:
        print(type(i[0]))
        print(f'insert into glassdata values ({str(i[0])})')
        mycursor.execute('insert into GenAI.GenAI_new_data values({values})'.format(values = ((i[0]))))

mydb.commit()
