from bs4 import BeautifulSoup as bs
import requests
import psycopg2 

conn = psycopg2.connect(
    dbname = 'itc',
    user = 'postgres',
    password = '0709045683kgg',
    host = 'localhost'
)
cursor = conn.cursor()
print('uve been successfully conected')

itc_page = requests.get(
    url = 'https://itc.kg/'
).text

data = bs(itc_page, 'html.parser')

section = data.find('section', attrs={'id': 'service'})
all_col_md_4 = section.find_all('div', class_='col-md-4')

for col in all_col_md_4:
    name = col.h2.get_text()

    definition = col.p.text.strip().split('\n')

    if definition[-1] == 'Подробнее':
        definition.pop(-1)
        
    

    descrtiption = ' '.join([i.strip() for i in definition])

    insert_q = f""" INSERT INTO services (name, definition) VALUES (\'{name}\');""" 
    record_q = (descrtiption)
    cursor.execute(insert_q, record_q)

    conn.commit()
    count = cursor.rowcount
    print (count, "Record inserted successfully into serv table")
  

   


