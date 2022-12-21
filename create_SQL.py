import sqlite3

conn = sqlite3.connect('test_database')
c = conn.cursor()

c.execute(
    'CREATE TABLE IF NOT EXISTS patients (NAME_PS text, ENTRY_DATE_PS,ENTRY_HOUR_PS,EXIT_DATE_PS,EXIT_HOUR_PS,DESTINATION)')
conn.commit()

table.to_sql('patients', conn, if_exists='replace', index = False)

c.execute('''  
    SELECT * FROM patients
          ''')

for row in c.fetchall():
    print (row)