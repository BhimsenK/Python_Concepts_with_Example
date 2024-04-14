import mysql.connector

mydb = mysql.connector.connect(  host="localhost",  user="abc",  password="password")
print(mydb)

mycursor = mydb.cursor() #this will tell that we are pointing to this database.

#creating table and inserting data
mycursor.execute("use GenAI")
mycursor.execute("CREATE TABLE GenAI_code (student INT(10), Name VARCHAR(15), class VARCHAR(20))") #creating table.
mycursor.execute("SHOW Tables")

#if below code doesn't work, comment the above 3 lines.
mycursor.execute("use GenAI")
mycursor.execute("select * from GenAI_course")
for x in mycursor:
  print(x)