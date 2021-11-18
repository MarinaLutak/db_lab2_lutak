import psycopg2

username = 'Lutak01'
password = '1111'
database = 'lutak_db_lab2'
host = 'localhost'
port = '5432'


query_1 = '''
select trim(name_footballer), age from footballer
'''
query_2 = '''
select trim(name_team), count(footballer.name_team) as pie_taem from football_team left join footballer using(name_team) group by name_team
'''
query_3 = '''
select number_of_players, trim(name_team) from football_team
'''

con = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)
print(type(con))

with con:

    print ("Database opened successfully")

    cur = con.cursor()

    cur.execute(query_1)
    for row in cur:
        print(row)

    cur.execute(query_2)
    for row in cur:
        print(row)

    cur.execute(query_3)
    for row in cur:
        print(row)