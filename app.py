from mysql import connector

conn = connector.connect(
    user="ardit700_student",
    password="ardit700_student",
    host="108.167.140.122",
    database="ardit700_pm1database"
)

cursor = conn.cursor()

user_input = input('Enter term: ')
query = cursor.execute('select * from Dictionary where Expression = \'%s\'' % user_input)

results = cursor.fetchall()

print(len(results))
if results:
    for result in results:
        print(result[1])
else:
    print('No definition found')

conn.close()
