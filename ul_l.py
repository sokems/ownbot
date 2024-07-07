import pymysql
from config import host, user_name, password, db_name

def show_list_ul_all(user):
    try:
        connection = pymysql.connect(
            host=host,
            port=3306,
            user=user_name,
            password=password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )

        try:
            with connection.cursor() as cur:
                list_ul = []
                cur.execute(f"SELECT name_ul FROM ul WHERE name_mp = ' ' AND ff_city = 0")
                search = cur.fetchall()
                for i in search:
                    list_ul.append(i['name_ul'])
                return sorted(list_ul, key=lambda x: x[0])

        finally:
            connection.close()
    except Exception as ex:
        return f'Ошибка {ex}. Не продолжайте!\n\nПередайте руководителю и нажмите <b>ОТМЕНА</b>'

def show_list_ul(user):
    try:
        connection = pymysql.connect(
            host=host,
            port=3306,
            user=user_name,
            password=password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )

        try:
            with connection.cursor() as cur:
                list_ul = []
                cur.execute(f"SELECT * FROM ul WHERE name_mp = ' ' AND ff_city = 0")
                search = cur.fetchall()
                for i in search:
                    check = 0
                    id_ul = i['id_ul']
                    cur.execute(f"SELECT items_count FROM items WHERE id_ul = '{id_ul}'")
                    count_ul = cur.fetchall()
                    for c in count_ul:
                        if c['items_count'] > 0:
                            check = 1
                            break
                    if check == 1:
                        list_ul.append(i['name_ul'])
                return sorted(list_ul, key=lambda x: x[0])

        finally:
            connection.close()
    except Exception as ex:
        return f'Ошибка {ex}. Не продолжайте!\n\nПередайте руководителю и нажмите <b>ОТМЕНА</b>'

def show_list_ul_arch(user):
    try:
        connection = pymysql.connect(
            host=host,
            port=3306,
            user=user_name,
            password=password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )

        try:
            with connection.cursor() as cur:
                list_ul = []
                cur.execute(f"SELECT name_ul FROM ul WHERE name_mp = 1 AND ff_city = 0")
                search = cur.fetchall()
                for i in search:
                    list_ul.append(i['name_ul'])
                return sorted(list_ul, key=lambda x: x[0])

        finally:
            connection.close()
    except Exception as ex:
        return f'Ошибка {ex}. Не продолжайте!\n\nПередайте руководителю и нажмите <b>ОТМЕНА</b>'



