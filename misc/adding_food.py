from uuid import uuid4

import psycopg2

from misc import *


def add_food(filename):
    try:
        connection = psycopg2.connect(
            host='5.145.160.142',
            user='postgres',
            password='postgres',
        )
        with connection.cursor() as cursor:
            dishes = get_menu(filename)
            for i in dishes:
                cursor.execute(f"SELECT id FROM menus WHERE type = 'global'")
                menu_id = cursor.fetchone()[0]
                category_id = str(uuid4())
                cursor.execute(f"INSERT INTO categories(id, description, photo_id, title, menu_id) VALUES (%s, 'Описание', null, %s, %s)",
                               (category_id, i, menu_id))
                for j in dishes[i]:
                    title = j['name']
                    price = j['price'].split('/')[0]
                    dish_id = str(uuid4())
                    cursor.execute(
                        f"INSERT INTO dishes(id, title, price, category_id) VALUES (%s, %s, %s, %s)",
                        (dish_id, title, price, category_id))
            connection.commit()
        print('111')
    except Exception as _ex:
        print('[INFO] Error while working with PostgreSQL', _ex)