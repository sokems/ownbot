import pymysql
from config import host, user_name, password, db_name

def calc_sell(ul, user):
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
                cur.execute(f"SELECT id_ul FROM ul WHERE name_ul = '{ul}'")
                id_ul = cur.fetchone()['id_ul']
                cur.execute(f"SELECT count_sell_wb_30 FROM sell WHERE id_ul = '{id_ul}'")
                count_wb_30 = cur.fetchone()['count_sell_wb_30']
                cur.execute(f"SELECT count_sell_ozon_30 FROM sell WHERE id_ul = '{id_ul}'")
                count_ozon_30 = cur.fetchone()['count_sell_ozon_30']
                cur.execute(f"SELECT count_sell_wb_60 FROM sell WHERE id_ul = '{id_ul}'")
                count_wb_60 = cur.fetchone()['count_sell_wb_60']
                cur.execute(f"SELECT count_sell_ozon_60 FROM sell WHERE id_ul = '{id_ul}'")
                count_ozon_60 = cur.fetchone()['count_sell_ozon_60']
                cur.execute(f"SELECT count_sell_wb_120 FROM sell WHERE id_ul = '{id_ul}'")
                count_wb_120 = cur.fetchone()['count_sell_wb_120']
                cur.execute(f"SELECT count_sell_ozon_120 FROM sell WHERE id_ul = '{id_ul}'")
                count_ozon_120 = cur.fetchone()['count_sell_ozon_120']
                cur.execute(f"SELECT count_sell_wb_max FROM sell WHERE id_ul = '{id_ul}'")
                count_wb_max = cur.fetchone()['count_sell_wb_max']
                cur.execute(f"SELECT count_sell_ozon_max FROM sell WHERE id_ul = '{id_ul}'")
                count_ozon_max = cur.fetchone()['count_sell_ozon_max']
                cur.execute(f"SELECT back_fbs FROM sell WHERE id_ul = '{id_ul}'")
                back_fbs = cur.fetchone()['back_fbs']

                cur.execute(f"SELECT count_sell_ya_30 FROM sell WHERE id_ul = '{id_ul}'")
                count_ya_30 = cur.fetchone()['count_sell_ya_30']
                cur.execute(f"SELECT count_sell_ya_60 FROM sell WHERE id_ul = '{id_ul}'")
                count_ya_60 = cur.fetchone()['count_sell_ya_60']
                cur.execute(f"SELECT count_sell_ya_120 FROM sell WHERE id_ul = '{id_ul}'")
                count_ya_120 = cur.fetchone()['count_sell_ya_120']
                cur.execute(f"SELECT count_sell_ya_max FROM sell WHERE id_ul = '{id_ul}'")
                count_ya_max = cur.fetchone()['count_sell_ya_max']

                cur.execute(f"SELECT count_sell_cdek_30 FROM sell WHERE id_ul = '{id_ul}'")
                count_cdek_30 = cur.fetchone()['count_sell_cdek_30']
                cur.execute(f"SELECT count_sell_cdek_60 FROM sell WHERE id_ul = '{id_ul}'")
                count_cdek_60 = cur.fetchone()['count_sell_cdek_60']
                cur.execute(f"SELECT count_sell_cdek_120 FROM sell WHERE id_ul = '{id_ul}'")
                count_cdek_120 = cur.fetchone()['count_sell_cdek_120']
                cur.execute(f"SELECT count_sell_cdek_max FROM sell WHERE id_ul = '{id_ul}'")
                count_cdek_max = cur.fetchone()['count_sell_cdek_max']


                cur.execute(f"SELECT count_pack_fbs FROM sell WHERE id_ul = '{id_ul}'")
                count_pack_fbs = cur.fetchone()['count_pack_fbs']
                cur.execute(f"SELECT comment_pack_fbs FROM sell WHERE id_ul = '{id_ul}'")
                comment_pack_fbs = cur.fetchone()['comment_pack_fbs']
                cur.execute(f"SELECT count_pal_fbs FROM sell WHERE id_ul = '{id_ul}'")
                count_pal_fbs = cur.fetchone()['count_pal_fbs']

                sum_pay = (count_wb_30 * 30) + (count_wb_60 * 70) + (count_wb_120 * 150) + (count_wb_max * 300)\
                          + (count_ozon_30 * 45) + (count_ozon_60 * 85) + (count_ozon_120 * 165) + (count_ozon_max * 305)\
                          + (count_ya_30 * 50) + (count_ya_60 * 90) + (count_ya_120 * 170) + (count_ya_max * 300)\
                          + (count_cdek_30 * 50) + (count_cdek_60 * 100) + (count_cdek_120 * 200) + (count_cdek_max * 400)\
                          + (back_fbs * 15)

                res = 'Доброго времени суток!\n\n'

                if sum_pay < 900:
                    sum_pay = 900
                    res += 'Ваша сумма рассчитывается по минимальной оплате по FBS (900р. в месяц) + хранение и дополнительная упаковка (если имеется).\n' \
                           'Если Вы с нами меньше месяца, то минимальная оплата считается из расчета 30р. в сутки.\n\n'


                if comment_pack_fbs == '-':
                    comment_pack_fbs = 'не было доп. упаковки'


                res+= f'Расчет FBS по клиенту: *{ul}*\n' \
                      f'Сумма к оплате: *{sum_pay + count_pack_fbs + count_pal_fbs} руб.*\n\n' \
                      f'Огромная просьба произвести оплату *СЕГОДНЯ*!\n\n' \
                      f'Было обработано заказов WB до 30см: *{count_wb_30}шт. по 30руб.*\n' \
                      f'Было обработано заказов WB до 60см: *{count_wb_60}шт. по 70руб.*\n' \
                      f'Было обработано заказов WB до 120см: *{count_wb_120}шт. по 150руб.*\n' \
                      f'Было обработано заказов WB КГТ: *{count_wb_max}шт. по 300руб.*\n' \
                      f'Было обработано заказов Ozon до 30см: *{count_ozon_30}шт. по 45руб.*\n' \
                      f'Было обработано заказов Ozon до 60см: *{count_ozon_60}шт. по 85руб.*\n' \
                      f'Было обработано заказов Ozon до 120см: *{count_ozon_120}шт. по 165руб.*\n' \
                      f'Было обработано заказов Ozon КГТ: *{count_ozon_max}шт. по 305руб.*\n' \
                      f'Было обработано заказов ЯМ до 30см: *{count_ya_30}шт. по 50руб.*\n' \
                      f'Было обработано заказов ЯМ до 60см: *{count_ya_60}шт. по 90руб.*\n' \
                      f'Было обработано заказов ЯМ до 120см: *{count_ya_120}шт. по 170руб.*\n' \
                      f'Было обработано заказов ЯМ КГТ: *{count_ya_max}шт. по 300руб.*\n' \
                      f'Было обработано заказов CDEK до 30см: *{count_cdek_30}шт. по 50руб.*\n' \
                      f'Было обработано заказов CDEK до 60см: *{count_cdek_60}шт. по 100руб.*\n' \
                      f'Было обработано заказов CDEK до 120см: *{count_cdek_120}шт. по 200руб.*\n' \
                      f'Было обработано заказов CDEK КГТ: *{count_cdek_max}шт. по 400руб.*\n' \
                      f'Было обработано возвратов: *{back_fbs}шт. по 15руб.*\n' \
                      f'Доп. упаковка: *{count_pack_fbs}руб. ({comment_pack_fbs})*\n' \
                      f'Хранение: *{count_pal_fbs}руб.*\n\n' \
                      f'Оплату можете произвести онлайн по номеру *89677498817*, перевод *ИСКЛЮЧИТЕЛЬНО НА ОЗОН БАНК*, пожалуйста 🙏🏻\n\nЕсли через *_Сбербанк_* переводите: Оплатить или перевести - Другому человеку - В другой банк - По номеру телефона *_89677498817, Фархат И._*, и не забудьте выбрать банк ОЗОН. _Если переводите через сбер, можете через сбп перевести без комиссии._\n\nЕсли у Вас есть вопросы по расчёту или несогласия, напишите нам, пожалуйста🙏🏻\n\n Как произведете оплату, отправьте, пожалуйста, чек☺️🙏🏻'
                return res


        finally:
            connection.close()
    except Exception as ex:
        return f'Ошибка {ex}. Не продолжайте!\n\nПередайте руководителю и нажмите <b>ОТМЕНА</b>'

def null_sell(ul, user):
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
                cur.execute(f"SELECT id_ul FROM ul WHERE name_ul = '{ul}'")
                id_ul = cur.fetchone()['id_ul']
                cur.execute(f"UPDATE sell SET count_sell_wb_30 = 0 WHERE id_ul = '{id_ul}'")
                connection.commit()
                cur.execute(f"UPDATE sell SET count_sell_ozon_30 = 0 WHERE id_ul = '{id_ul}'")
                connection.commit()
                cur.execute(f"UPDATE sell SET count_sell_wb_60 = 0 WHERE id_ul = '{id_ul}'")
                connection.commit()
                cur.execute(f"UPDATE sell SET count_sell_ozon_60 = 0 WHERE id_ul = '{id_ul}'")
                connection.commit()
                cur.execute(f"UPDATE sell SET count_sell_wb_120 = 0 WHERE id_ul = '{id_ul}'")
                connection.commit()
                cur.execute(f"UPDATE sell SET count_sell_ozon_120 = 0 WHERE id_ul = '{id_ul}'")
                connection.commit()
                cur.execute(f"UPDATE sell SET count_sell_wb_max = 0 WHERE id_ul = '{id_ul}'")
                connection.commit()
                cur.execute(f"UPDATE sell SET count_sell_ozon_max = 0 WHERE id_ul = '{id_ul}'")
                connection.commit()
                cur.execute(f"UPDATE sell SET back_fbs = 0 WHERE id_ul = '{id_ul}'")
                connection.commit()
                cur.execute(f"UPDATE sell SET count_pack_fbs = 0 WHERE id_ul = '{id_ul}'")
                connection.commit()
                cur.execute(f"UPDATE sell SET comment_pack_fbs = 'не было упаковки' WHERE id_ul = '{id_ul}'")
                connection.commit()
                cur.execute(f"UPDATE sell SET count_pal_fbs = 0 WHERE id_ul = '{id_ul}'")
                connection.commit()
                cur.execute(f"UPDATE sell SET count_sell_ya_30 = 0 WHERE id_ul = '{id_ul}'")
                connection.commit()
                cur.execute(f"UPDATE sell SET count_sell_ya_60 = 0 WHERE id_ul = '{id_ul}'")
                connection.commit()
                cur.execute(f"UPDATE sell SET count_sell_ya_120 = 0 WHERE id_ul = '{id_ul}'")
                connection.commit()
                cur.execute(f"UPDATE sell SET count_sell_ya_max = 0 WHERE id_ul = '{id_ul}'")
                connection.commit()
                cur.execute(f"UPDATE sell SET count_sell_cdek_30 = 0 WHERE id_ul = '{id_ul}'")
                connection.commit()
                cur.execute(f"UPDATE sell SET count_sell_cdek_60 = 0 WHERE id_ul = '{id_ul}'")
                connection.commit()
                cur.execute(f"UPDATE sell SET count_sell_cdek_120 = 0 WHERE id_ul = '{id_ul}'")
                connection.commit()
                cur.execute(f"UPDATE sell SET count_sell_cdek_max = 0 WHERE id_ul = '{id_ul}'")
                connection.commit()


        finally:
            connection.close()
    except Exception as ex:
        return f'Ошибка {ex}. Не продолжайте!\n\nПередайте руководителю и нажмите <b>ОТМЕНА</b>'
