#many to many relationships..
import json
import sqlite3

conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS Users;
DROP TABLE IF EXISTS Course;
DROP TABLE IF EXISTS Member;


CREATE TABLE Users (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE,
    email TEXT UNIQUE
);

CREATE TABLE Course (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title   TEXT UNIQUE
);

CREATE TABLE Member (
    user_id INTEGER,
    course_id INTEGER,
    role INTEGER,
    PRIMARY KEY(user_id, course_id)
);
'''
#Member table is connector table and has many-to-many relationship.
)

fname = input('Enter file names: ')
if ( len(fname) < 1 ) : fname = 'py4e\ex_04\week4assignment\\roster_data.json'

str_data = open(fname).read()
json_data = json.loads(str_data)

for entry in json_data:
    name = entry[0]
    title = entry[1]
    role = entry[2]
    
    cur.execute('''INSERT OR IGNORE INTO Users (name) 
        VALUES ( ? )''', ( name, ) )
    cur.execute('SELECT id FROM Users WHERE name = ? ', (name, ))
    user_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Course (title) 
        VALUES ( ? )''', ( title, ) )
    cur.execute('SELECT id FROM Course WHERE title = ? ', (title, ))
    course_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Member (user_id, course_id, role) 
        VALUES ( ?, ?, ?)''', ( user_id,course_id,role ) )

  
cur.execute('''
    SELECT 'XYZZY' || hex(Users.name || Course.title || Member.role ) AS X FROM 
    Users JOIN Member JOIN Course 
    ON Users.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY X LIMIT 1;
    ''')
record = cur.fetchone()
print(record)
conn.commit()