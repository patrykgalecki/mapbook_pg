
import psycopg2 as ps

db_params=ps.connect(user='aaaaaaa',password='aaaaaaa',database='aaaaaaa',
                     host='localhost',port='5434')





cursor=db_params.cursor()
query="SELECT name,surname,posts,location,st_astext(coordinates),id FROM public.users ORDER BY id ASC"
cursor.execute(query)
users=cursor.fetchall()
cursor.close()

# print(users)
for user in users:
    print(float(user[4][6:-1].split()[0]))
    print(float(user[4][6:-1].split()[1]))