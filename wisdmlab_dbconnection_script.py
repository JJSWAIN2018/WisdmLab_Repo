"""
import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","testuser","test123","TESTDB" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# Create table as per requirement
sql = CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )

cursor.execute(sql)

#execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchoneall() method.
data = cursor.fetchoneall(sql=FIRST_NAME)
visitors=[]
for visitors in data:
    count=len(visitors)
    visitorno+1=count
    Print("You are visitors no." visitorno)
    
    

# disconnect from server
db.close()
"""



