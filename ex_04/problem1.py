import sqlite3

conn = sqlite3.connect('orgcount.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts (org TEXT, count integer)')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'D:\python\py4e\ex_04\\mbox.txt'
#print(fname)
fhandle = open(fname)

for line in fhandle:
    if not line.startswith('From '): continue
    pieces = line.split()
    email = pieces[1]
    org = email[email.find('@')+1:]
    #print(domain)
    cur.execute('SELECT count FROM Counts WHERE org = ?',(org,))
    row = cur.fetchone()
    if row is None:
        cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 where org = ?', (org,))
    
conn.commit()


sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 1'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()