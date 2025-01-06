import sqlite3

# connect to sqlite
connection = sqlite3.connect("student.db")

# create a cursor object to insert record, create table
cursor = connection.cursor()

# create table
table_info = '''
create table student(name varchar(25), class varchar(25), section varchar(25), marks int)
'''

cursor.execute(table_info)

# insert some more records
cursor.execute('''insert into student values('Krish', 'Data Science', 'A', 90)''')
cursor.execute('''insert into student values('John', 'Data Science', 'B', 100)''')
cursor.execute('''insert into student values('Mukesh', 'Data Science', 'A', 86)''')
cursor.execute('''insert into student values('Jacob', 'DEVOPS', 'A', 50)''')
cursor.execute('''insert into student values('Dipesh', 'DEVOPS', 'A', 35)''')

# display all the records
print("The inserted records are")
data = cursor.execute("select * from student")
for row in data:
    print(row)

# commit your changes in the database
connection.commit()
connection.close()