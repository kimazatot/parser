from bs4 import BeautifulSoup as bs
import requests
import psycopg2

globus_page = requests.get(
    url = 'https://globus-online.kg/catalog/ovoshchi_frukty_orekhi_zelen/'
).text

data = bs(globus_page, 'html.parser')

connection = psycopg2.connect(
    dbname = 'globus',
    user = 'postgres',
    password = '0709045683kgg',
    host = 'localhost'
)
cursor = connection.cursor()

# create = '''CREATE TABLE vegetables (
#     user_id SERIAL PRIMARY KEY,
#     image_link VARCHAR(300) NOT NULL,
#     product_name VARCHAR(300) NOT NULL,
#     price VARCHAR(300) NOT NULL
# );'''
# cursor.execute(create)
# cursor.connection.commit()


view_showcase = data.find('div', attrs={ 'id': 'view-showcase'})

all_card = view_showcase.find_all('div', class_= 'list-showcase__part-main')

for card in all_card:
    image = card.find('div', class_='list-showcase__picture').a.img.get('src')
    name_of_product = card.find('div', class_='list-showcase__name-rating').a.text
    price = card.find('div', class_='list-showcase__prices').find('span', class_='c-prices__value js-prices_pdv_ГЛОБУС Розничная').text
    print(name_of_product)


    a = f'''INSERT INTO vegetables (image_link, product_name, price)
        VALUES (\'{image}\', \'{name_of_product}\', \'{price}\');'''
    
    cursor.execute(a)
    connection.commit()