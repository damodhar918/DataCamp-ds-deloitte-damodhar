# from sqlite3 import connect
# from argon2 import PasswordHasher
import mysql.connector 

"""
show databases;
create database dj;

use dj; 
create table student(name varchar(20), college varchar(20));

insert into student values ('naji','crec'),('vijay', 'srec');
select * from student
"""






mydb =  mysql.connector.connect(
    host='localhost',
    user='root',
    password ='Dam560037KA',
    database = 'dj'
)
print(mydb)






mycursor = mydb.cursor()

# # mycursor.execute('show databases')

# # [print(i) for i in mycursor]

# # mycursor.execute('use dj')

mycursor.execute('select * from student')


[print(i) for i in mycursor]

# result = mycursor.fetchone()
# [print(i) for i in result]


