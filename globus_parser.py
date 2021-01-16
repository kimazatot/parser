from bs4 import BeautifulSoup as bs 
import requests
import psycopg2 

# connection = psycopg2.connect(
#     dbname = 'globus',
#     user = 'postgres',
#     password = '0709045683kgg',
#     host = 'localhost'
# )
# cursor = connection.cursor()

# create = '''CREATE TABLE meats (
#     user_id SERIAL PRIMARY KEY,
#     image_link VARCHAR(300) NOT NULL,
#     product_name VARCHAR(300) NOT NULL,
#     price VARCHAR(300) NOT NULL
# );'''
# # cursor.execute(create)
# # cursor.connection.commit()


# HOST = 'https://globus-online.kg/catalog/myaso_ptitsa_ryba/'
# HEADERS ={
#     'accept': '*/*',
#     'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
# }

# globus_page = requests.get(HOST,headers=HEADERS).text

# data = bs(globus_page,'html.parser')

# view_showcase = data.find('div', attrs={"id":"view-showcase"})

# all_cards = view_showcase.find_all('div', class_ = 'list-showcase__part-main')

# for card in all_cards:
#     image_link = card.find('div', class_='list-showcase__picture').a.img.get('src')
#     product_name = card.find('div', class_='list-showcase__name-rating').a.text
#     price = card.find('div', class_='list-showcase__prices').find('span', class_='c-prices__value js-prices_pdv_ГЛОБУС Розничная').text
   
#     a = f'''INSERT INTO meats (image_link, product_name, price)
#         VALUES (\'{image_link}\', \'{product_name}\', \'{price}\');'''
    
#     cursor.execute(a)
#     connection.commit()

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


HOST = 'https://globus-online.kg/catalog/ovoshchi_frukty_orekhi_zelen/'
HEADERS ={
    'accept': '*/*',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
}

globus_page = requests.get(HOST,headers=HEADERS).text

data = bs(globus_page,'html.parser')

view_showcase = data.find('div', attrs={"id":"view-showcase"})

all_cards = view_showcase.find_all('div', class_ = 'list-showcase__part-main')

for card in all_cards:
    image_link = card.find('div', class_='list-showcase__picture').a.img.get('src')
    product_name = card.find('div', class_='list-showcase__name-rating').a.text
    price = card.find('div', class_='list-showcase__prices').find('span', class_='c-prices__value js-prices_pdv_ГЛОБУС Розничная').text
    # print(image_link)
    a = f'''INSERT INTO vegetables (image_link, product_name, price)
        VALUES (\'{image_link}\', \'{product_name}\', \'{price}\');'''
    
    cursor.execute(a)
    connection.commit()