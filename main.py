from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import Message, LabeledPrice, PreCheckoutQuery
import markups
import texts
import time
import pymysql
from config import host, user_name, password, db_name
import re
from openpyxl import load_workbook
from fbo import excel
import ul_l
import calc
import gspread
import datetime
import sk
import json
import aiocron


TOKEN = ''

bot = Bot(TOKEN, parse_mode='html')
db = Dispatcher(bot)

gc = gspread.service_account(filename='retail-397705-2cb2125124db.json')
sh = gc.open_by_url("https://docs.google.com/spreadsheets/d/1c389riVHBioK2N9elinFl6iqxN_OFTo00EXaipvzN-w")


def update(text, user):
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
            with connection.cursor() as cursor:
                cursor.execute(text)
                connection.commit()
                return 0

        finally:
            connection.close()
    except Exception as ex:
        return f'Ошибка {ex}. Не продолжайте!\n\nПередайте руководителю и нажмите <b>ОТМЕНА</b>'

def create(text, user):
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
            with connection.cursor() as cursor:
                cursor.execute(text)
                connection.commit()
                return 0

        finally:
            connection.close()
    except Exception as ex:
        return f'Ошибка {ex}. Не продолжайте!\n\nПередайте руководителю и нажмите <b>ОТМЕНА</b>'

def selone(text, user):
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
            with connection.cursor() as cursor:
                cursor.execute(text)
                return cursor.fetchone()

        finally:
            connection.close()
    except Exception as ex:
        return f'Ошибка {ex}. Не продолжайте!\n\nПередайте руководителю и нажмите <b>ОТМЕНА</b>'

def selist(text, user):
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
            with connection.cursor() as cursor:
                cursor.execute(text)
                return cursor.fetchall()

        finally:
            connection.close()
    except Exception as ex:
        return f'Ошибка {ex}. Не продолжайте!\n\nПередайте руководителю и нажмите <b>ОТМЕНА</b>'

def defaul_values(id_user):
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
                cur.execute(f"UPDATE users SET word_5 = ' ', calc_box = 0, price = 0, height = 0, height_flag = 0, length1 = 0, "
                            f"length_flag = 0, width = 0, width_flag = 0, min_price = 0, minus_item2 = 0, "
                            f"xl_ul = 0, xl_ul_text = '', xl_tel = 0, xl_tel_text = 0, xl_type = 0, "
                            f"xl_type_text = '', xl_count_type = 0, xl_count_type_text = 0, xl_mark = 0, "
                            f"xl_mark_text = '', xl_pack = 0, xl_pack_text = '', xl_comment = 0, "
                            f"xl_comment_text = '', xl_city = 0, xl_city_text = '', xl_count_box = 0, "
                            f"xl_count_box_text = 0, xl_count_items = 0, xl_count_items_text = '', "
                            f"xl_comment_city = 0, xl_comment_city_text = '', xl_markbox = 0, xl_markbox_text = '', "
                            f"logistic = 0, ff = 0, new_id_user = 0, new_id_user_text = '', new_name_user = 0, "
                            f"remove_user = 0, fbo_15 = 0, new_car_city = 0, new_car_plan_start = 0, "
                            f"new_car_plan_end = 0, car_drive = 0, num_car = 0, drive_num = 0, gate = 0, "
                            f"find_car = 0, car_city = 0, chcar = 0, del_car = 0, find_zakaz = 0, sumpd = 0, "
                            f"countpd = 0, text_user = 0, id_fbo = 0, new_car_city_text = '', zak_day = 0, "
                            f"zak_mon = 0, zak_year = 0, ef_day = 0, ef_mon = 0, ef_year = 0, zabor = 0, "
                            f"ed_day = 0, ed_mon = 0, ed_year = 0, prib_day = 0, prib_mon = 0, prib_year = 0, "
                            f"fbo_16 = 0, chcar_2 = 0, remove_user_adm = 0, fbo_11 = 0, fbo_18 = 0, fbo_18_1 = 0, "
                            f"gate_2 = 0, find_car = 0, find_car_4 = 0, weight = 0, count_pal_flag = 0, "
                            f"max_id_item = 0, add_set_0 = 0, add_set_1 = 0, add_set_4 = 0, "
                            f"add_set_5 = 0, add_set_6 = 0, add_set_7 = 0, add_set_8 = 0, add_set_9 = 0, "
                            f"add_set_10 = 0, add_set_11 = 0, add_set_12 = 0, add_set_13 = 0, find_item = 0, "
                            f"what_in_box = 0, choose_ul = '', edit_item = 0, all_edit_item = 0, choose_id = '', "
                            f"choose_pr = '', edit_pr = 0, add_ul = 0, plus_new_sell = 0, plus_new_sell2 = 0, "
                            f"plus_new_sell3 = 0, count_wb = 0, count_ozon = 0, edit_box = 0, edit_box_item = 0, "
                            f"choose_box = '', edit_box_item_add = 0, find_item_id = 0, edit_ul_2 = 0, "
                            f"new_id_user = 0, new_id_user_text = '', new_name_user = 0, remove_user = 0, "
                            f"plus_new_sell4 = 0, text_user = 0, count_wb_60 = 0, count_ozon_60 = 0, "
                            f"count_wb_120 = 0, count_ozon_120 = 0, count_wb_max = 0, count_ozon_max = 0, "
                            f"plus_new_sell5 = 0, plus_new_sell6 = 0, plus_new_sell7 = 0, plus_new_sell8 = 0, "
                            f"plus_new_sell9 = 0, remove_user_adm = 0, find_item2 = 0, choose_ul_id = 0, act_sk = ' ', "
                            f"act_log = ' ', edit_log = ' ', act_retail = ' ', act_wood = ' ' WHERE id_user = '{id_user}'")
                connection.commit()
                return 0

        finally:
            connection.close()
    except Exception as ex:
        return f'Ошибка {ex}. Не продолжайте!\n\nПередайте руководителю и нажмите <b>ОТМЕНА</b>'

async def startup(_):
    print('Бот запущен')


@db.message_handler(commands='info')
async def info_command(message: types.Message):
    id_user_get = f'`{message.chat.id}`'
    await message.answer(text=id_user_get, parse_mode='Markdown')

@db.message_handler(commands='message')
async def info_command(message: types.Message):
    user = message.chat.id
    await message.answer(text=message, parse_mode='HTML')

@db.message_handler(commands='test1')
async def info_command(message: types.Message):
    delta_1 = datetime.timedelta(hours=5)
    now = datetime.datetime.now()

    name_list = f"График Март 2024"

    worksheet_2 = sh.worksheet(name_list)
    num_row = int(now.day) + 1

    workers = ['Айнур', 'Рома', 'Абубек']
    rast = 90
    mishk = 2
    razgr = 1

    mes = '✅ Производственная смена закрыта!\n\nРаботали: '

    for worker in workers:
        mes += f'*{worker} *'

    acp = f'A{num_row}'
    acd = f'B{num_row}'

    plan = worksheet_2.acell(acp).value
    dop = float(worksheet_2.acell(acd).value[2:].replace(',', '.'))

    chs = float(worksheet_2.acell('C34').value[2:].replace(',', '.'))
    chm = float(worksheet_2.acell('C35').value[2:].replace(',', '.'))
    zav = float(worksheet_2.acell('C36').value[2:].replace(',', '.'))
    nght = float(worksheet_2.acell('C37').value[2:].replace(',', '.'))
    razs = float(worksheet_2.acell('C38').value[2:].replace(',', '.'))

    mes += f'\n——————————————' \
           f'\n🐥 Сделано растущих: *{rast}*' \
           f'\n\nПлан: *{plan}*' \
           f'\nСумма за одно доп. изделие: *{dop} руб.*' \
           f'\nСумма за доп. изделия: *{(int(rast) - int(plan)) * dop} руб.*' \
           f'\n——————————————' \
           f'\n📦 Упаковано возвратов: *{mishk}*' \
           f'\n\nСумма за один возврат: *{zav} руб.*' \
           f'\nСумма за возвраты: *{int(mishk) * zav} руб.*' \
           f'\n——————————————' \
           f'\n🚚 Разгрузок: *{razgr}*' \
           f'\n\nСумма за одну разгрузку: *{razs} руб.*' \
           f'\nСумма за разгрузки: *{int(razgr) * razs} руб.*'


    await bot.send_message(chat_id=-1002146643966, text=mes, message_thread_id=2111, parse_mode='Markdown')


@db.message_handler(commands='start')
async def start_command(message: types.Message):
    user = message.chat.id
    if selone(f"SELECT id_user FROM users WHERE id_user = '{user}'", user) is None:
        await message.answer(text=texts.start_text)
    else:
        admin_list = selone(f"SELECT id_user FROM users WHERE id_user = '{user}'", user)
        if admin_list is not None:
            await message.answer(text=texts.menu_name, reply_markup=markups.menu_admin)


@db.message_handler(content_types=['photo'])
async def handle_docs_photo(message):
    user = message.chat.id
    if user == -1001933713976 or user == -984607796 or user == -1002146643966:
        pass
    elif 'brk_' in selone(f"SELECT act_sk FROM users WHERE id_user = '{user}'", user)['act_sk']:
        file_id = message.photo[-1].file_id

        object_name = selone(f"SELECT act_sk FROM users WHERE id_user = '{user}'", user)['act_sk'].split('_')[1]
        object_count = selone(f"SELECT act_sk FROM users WHERE id_user = '{user}'", user)['act_sk'].split('_')[2]
        update(f"UPDATE users SET act_sk = ' ' WHERE id_user = '{user}'", user)

        name_objects = selist(f"SELECT * FROM warehouse_c", user)
        count_obj = selone(f"SELECT count_item FROM warehouse_c WHERE name_item = '{object_name}'", user)['count_item']


        for o in name_objects:
            if o["name_item"] == object_name:
                update(f"UPDATE warehouse_c SET count_item = '{int(count_obj) - int(object_count)}' WHERE name_item = '{object_name}'", user)

        mes = f'Наименование: *{object_name}*\nКоличество: *{object_count}*'
        await bot.send_photo(chat_id=-1002146643966, photo=file_id, caption=mes, message_thread_id=1500, parse_mode='Markdown')

        if selone(f"SELECT count_retail FROM users WHERE id_user = '{user}'", user)['count_retail'] == 2:
            await message.answer(text='Остатки по складу в Цеху изменены!', reply_markup=markups.menu_count_retail_n)
        elif selone(f"SELECT count_retail FROM users WHERE id_user = '{user}'", user)['count_retail'] == 1:
            await message.answer(text='Остатки по складу в Цеху изменены!', reply_markup=markups.menu_count_retail_b)




    else:
        try:
            await message.answer(text=message, parse_mode='HTML')
        except Exception as e:
            await message.answer(text=e)

@db.message_handler(content_types=types.ContentType.CONTACT)
async def contacts(message: types.Message):
    user = message.chat.id
    await bot.send_contact(chat_id=user, phone_number='+79872560706', first_name='Роман')

@db.pre_checkout_query_handler()
async def pre_check(pcq: PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pcq.id, ok=True)
    mes = f'Спасибо за оплату {pcq.total_amount // 100} {pcq.currency}'
    user = pcq.from_user.id
    await bot.send_message(chat_id=user, text=pcq.invoice_payload)
    await bot.send_message(chat_id=user, text=mes)
    await bot.send_message(chat_id=user, text='Клиент оплатил')

@db.callback_query_handler()
async def action_callback(callback: types.CallbackQuery):
    user = callback.message.chat.id
    if callback.data == 'add_man':
        new_id_user_text = selone(f"SELECT new_id_user_text FROM users WHERE id_user = '{user}'", user)[
            'new_id_user_text']
        name_new_user = selone(f"SELECT name_new_user FROM users WHERE id_user = '{user}'", user)['name_new_user']
        create(f"REPLACE INTO users(id_user, name_user, company, notif) VALUES ('{new_id_user_text}', '{name_new_user}', 'ФФ', 'client fbs fbo')",
               user)
        await callback.message.answer(text=f'ID сотрудника: <b>{new_id_user_text}</b>\n'
                                           f'Фамилия и Имя: <b>{name_new_user}</b>\n'
                                           f'Должность: <b>Менеджер</b>\n')
        await callback.message.answer('Сотрудник записан!', reply_markup=markups.menu_ff)
        await callback.answer()
    elif callback.data == 'add_dr':
        new_id_user_text = selone(f"SELECT new_id_user_text FROM users WHERE id_user = '{user}'", user)[
            'new_id_user_text']
        name_new_user = selone(f"SELECT name_new_user FROM users WHERE id_user = '{user}'", user)['name_new_user']
        create(f"REPLACE INTO users(id_user, name_user, company, notif) VALUES ('{new_id_user_text}', '{name_new_user}', 'Водитель', 'log')",
               user)
        await callback.message.answer(text=f'ID сотрудника: <b>{new_id_user_text}</b>\n'
                                           f'Фамилия и Имя: <b>{name_new_user}</b>\n'
                                           f'Должность: <b>Менеджер</b>\n')
        await callback.message.answer('Сотрудник записан!', reply_markup=markups.menu_ff)
        await callback.answer()
    elif callback.data == 'add_adm':
        new_id_user_text = selone(f"SELECT new_id_user_text FROM users WHERE id_user = '{user}'", user)[
            'new_id_user_text']
        name_new_user = selone(f"SELECT name_new_user FROM users WHERE id_user = '{user}'", user)['name_new_user']
        create(f"REPLACE INTO users(id_user, name_user, company, notif) VALUES ('{new_id_user_text}', '{name_new_user}', 'ФФ Управление', 'client fbs fbo')",
               user)
        await callback.message.answer(text=f'ID сотрудника: <b>{new_id_user_text}</b>\n'
                                           f'Фамилия и Имя: <b>{name_new_user}</b>\n'
                                           f'Должность: <b>Управляющий</b>\n')
        await callback.message.answer('Сотрудник записан!', reply_markup=markups.menu_ff)
        await callback.answer()
    elif callback.data == 'add_count_mas':
        new_id_user_text = selone(f"SELECT new_id_user_text FROM users WHERE id_user = '{user}'", user)[
            'new_id_user_text']
        name_new_user = selone(f"SELECT name_new_user FROM users WHERE id_user = '{user}'", user)['name_new_user']

        if selone(f"SELECT count_retail FROM users WHERE id_user = '{user}'", user)['count_retail'] == 2:
            create(f"REPLACE INTO users(id_user, count_retail, name_user, company, notif) VALUES ('{new_id_user_text}', 2, '{name_new_user}', 'Мастер', 'skaz wood')", user)
        elif selone(f"SELECT count_retail FROM users WHERE id_user = '{user}'", user)['count_retail'] == 1:
            create(f"REPLACE INTO users(id_user, count_retail, name_user, company, notif) VALUES ('{new_id_user_text}', 1, '{name_new_user}', 'Мастер', 'skaz wood')", user)

        await callback.message.answer(text=f'ID сотрудника: <b>{new_id_user_text}</b>\n'
                                           f'Фамилия и Имя: <b>{name_new_user}</b>\n'
                                           f'Должность: <b>Мастер</b>\n')
        await callback.message.answer('Сотрудник записан!', reply_markup=markups.menu_count)
        await callback.answer()
    elif callback.data == 'add_count_sbor':
        new_id_user_text = selone(f"SELECT new_id_user_text FROM users WHERE id_user = '{user}'", user)[
            'new_id_user_text']
        name_new_user = selone(f"SELECT name_new_user FROM users WHERE id_user = '{user}'", user)['name_new_user']

        if selone(f"SELECT count_retail FROM users WHERE id_user = '{user}'", user)['count_retail'] == 2:
            create(
                f"REPLACE INTO users(id_user, count_retail, name_user, company) VALUES ('{new_id_user_text}', 2, '{name_new_user}', 'Сборщик')",
                user)
        elif selone(f"SELECT count_retail FROM users WHERE id_user = '{user}'", user)['count_retail'] == 1:
            create(
                f"REPLACE INTO users(id_user, count_retail, name_user, company) VALUES ('{new_id_user_text}', 1, '{name_new_user}', 'Сборщик')",
                user)

        await callback.message.answer(text=f'ID сотрудника: <b>{new_id_user_text}</b>\n'
                                           f'Фамилия и Имя: <b>{name_new_user}</b>\n'
                                           f'Должность: <b>Сборщик мебели</b>\n')
        await callback.message.answer('Сотрудник записан!', reply_markup=markups.menu_count)
        await callback.answer()
    elif 'del_arch_' in callback.data:
        car_id = callback.data[9:]
        update(f"UPDATE cars SET flag_arch = 0 WHERE car_id = '{car_id}'", user)
        await callback.message.edit_text(text=f'Машина с ID {car_id} убрана из архива')
        await callback.answer()
    elif 'del_zakarch_' in callback.data:
        fbo_id = callback.data[12:]
        update(f"UPDATE fbo SET flag_arch = 0 WHERE fbo_id = '{fbo_id}'", user)
        await callback.message.edit_text(text=f'Заказ с ID {fbo_id} убран из архива')
        await callback.answer()
    elif 'real_' in callback.data:
        list_ul = ul_l.show_list_ul_all(user)
        update(
            f"UPDATE users SET choose_ul = '{list_ul[int(callback.data[5:])]}' WHERE id_user = '{callback.message.chat.id}'",
            user)
        inline_wb = InlineKeyboardMarkup(row_width=1)
        inline_wb_b1 = InlineKeyboardButton(text='Да', callback_data='realwb')
        inline_wb_b2 = InlineKeyboardButton(text='Нет', callback_data='norealwb')
        inline_wb.add(inline_wb_b1, inline_wb_b2)
        await callback.message.answer(text=f'Вы выбрали: <b>{list_ul[int(callback.data[5:])]}</b>')
        await callback.message.answer(text='Есть отгрузки на WB?', reply_markup=inline_wb)
        await callback.answer()
    elif callback.data == 'realwb':
        update(f"UPDATE users SET plus_new_sell = 1 WHERE id_user = '{callback.message.chat.id}'", user)
        await callback.message.answer(text='Введите количество заказов на WB до 30см: ')
        await callback.answer()
    elif callback.data == 'norealwb':
        update(f"UPDATE users SET count_wb = 0 WHERE id_user = '{user}'", user)
        update(f"UPDATE users SET count_wb_120 = 0 WHERE id_user = '{user}'", user)
        update(f"UPDATE users SET count_wb_max = 0 WHERE id_user = '{user}'", user)
        update(f"UPDATE users SET count_wb_60 = 0 WHERE id_user = '{user}'", user)
        inline_ozon = InlineKeyboardMarkup(row_width=1)
        inline_ozon_b1 = InlineKeyboardButton(text='Да', callback_data='realozon')
        inline_ozon_b2 = InlineKeyboardButton(text='Нет', callback_data='norealozon')
        inline_ozon.add(inline_ozon_b1, inline_ozon_b2)
        await callback.message.answer(text='Есть отгрузки на OZON?', reply_markup=inline_ozon)
        await callback.answer()
    elif callback.data == 'realozon':
        update(f"UPDATE users SET plus_new_sell5 = 1 WHERE id_user = '{user}'", user)
        await callback.message.answer(text='Введите количество заказов на OZON до 30см: ')
        await callback.answer()
    elif callback.data == 'norealozon':
        update(f"UPDATE users SET count_ozon = 0 WHERE id_user = '{user}'", user)
        update(f"UPDATE users SET count_ozon_120 = 0 WHERE id_user = '{user}'", user)
        update(f"UPDATE users SET count_ozon_max = 0 WHERE id_user = '{user}'", user)
        update(f"UPDATE users SET count_ozon_60 = 0 WHERE id_user = '{user}'", user)
        inline_ya = InlineKeyboardMarkup(row_width=1)
        inline_ya_b1 = InlineKeyboardButton(text='Да', callback_data='realya')
        inline_ya_b2 = InlineKeyboardButton(text='Нет', callback_data='norealya')
        inline_ya.add(inline_ya_b1, inline_ya_b2)
        await callback.message.answer(text='Есть отгрузки на ЯМ?', reply_markup=inline_ya)
        await callback.answer()
    elif callback.data == 'realya':
        update(f"UPDATE users SET plus_new_sell8 = 101 WHERE id_user = '{user}'", user)
        await callback.message.answer(text='Введите количество заказов на ЯМ до 30см: ')
        await callback.answer()
    elif callback.data == 'norealya':
        update(f"UPDATE users SET count_ya = 0 WHERE id_user = '{user}'", user)
        update(f"UPDATE users SET count_ya_120 = 0 WHERE id_user = '{user}'", user)
        update(f"UPDATE users SET count_ya_max = 0 WHERE id_user = '{user}'", user)
        update(f"UPDATE users SET count_ya_60 = 0 WHERE id_user = '{user}'", user)
        inline_cdek = InlineKeyboardMarkup(row_width=1)
        inline_cdek_b1 = InlineKeyboardButton(text='Да', callback_data='realcdek')
        inline_cdek_b2 = InlineKeyboardButton(text='Нет', callback_data='norealcdek')
        inline_cdek.add(inline_cdek_b1, inline_cdek_b2)
        await callback.message.answer(text='Есть отгрузки на CDEK?', reply_markup=inline_cdek)
        await callback.answer()
    elif callback.data == 'realcdek':
        update(f"UPDATE users SET plus_new_sell8 = 105 WHERE id_user = '{user}'", user)
        await callback.message.answer(text='Введите количество заказов на CDEK до 30см: ')
        await callback.answer()
    elif callback.data == 'norealcdek':
        update(f"UPDATE users SET count_cdek = 0 WHERE id_user = '{user}'", user)
        update(f"UPDATE users SET count_cdek_120 = 0 WHERE id_user = '{user}'", user)
        update(f"UPDATE users SET count_cdek_max = 0 WHERE id_user = '{user}'", user)
        update(f"UPDATE users SET count_cdek_60 = 0 WHERE id_user = '{user}'", user)
        update(f"UPDATE users SET plus_new_sell8 = 2 WHERE id_user = '{user}'", user)
        await callback.message.answer(text='Введите сумму за упаковку: ')
        await callback.answer()
    elif 'calc_' in callback.data:
        list_ul = ul_l.show_list_ul_all(user)
        update(f"UPDATE users SET choose_ul = '{list_ul[int(callback.data[5:])]}' WHERE id_user = '{callback.message.chat.id}'", user)
        choose_ul = selone(f"SELECT choose_ul FROM users WHERE id_user = '{callback.message.chat.id}'", user)['choose_ul']
        await callback.message.answer(text=calc.calc_sell(choose_ul, user))
        keyboard2 = types.InlineKeyboardMarkup()
        keyboard2.row_width = 5
        keyboard2.add(types.InlineKeyboardButton(text='Обнулить', callback_data='nu'))
        await callback.message.answer(text="Отправьте клиенту сообщение выше.\n"
                                           "Если клиент расчитался, нажмите 'Обнулить'", reply_markup=keyboard2)
        await callback.answer()
    elif callback.data == 'nu':
        choose_ul = selone(f"SELECT choose_ul FROM users WHERE id_user = '{callback.message.chat.id}'", user)['choose_ul']
        calc.null_sell(choose_ul, user)
        await callback.message.edit_text(f'Данные клиента {choose_ul} обнулены!')
        await callback.message.answer(text=f'FBS', reply_markup=markups.menu_fbs)
        await callback.answer()
    elif 'unu_' in callback.data:
        choose_ul = callback.data[4:]
        calc.null_sell(choose_ul, user)
        await callback.message.edit_text(f'Данные клиента {choose_ul} обнулены!')
        await callback.message.answer(text=f'FBS', reply_markup=markups.menu_fbs)
        await callback.answer()

    # Расход Мебель
    elif callback.data == 'donepay_yes':
        update(f"UPDATE users SET word_8 = 'Оплачено' WHERE id_user = '{callback.message.chat.id}'", user)
        await callback.message.edit_text(text='Выберите категорию:', reply_markup=markups.inline_cat)
        await callback.answer()
    elif callback.data == 'donepay_no':
        update(f"UPDATE users SET word_8 = 'Не оплачено' WHERE id_user = '{callback.message.chat.id}'", user)
        await callback.message.edit_text(text='Выберите категорию:', reply_markup=markups.inline_cat)
        await callback.answer()
    elif callback.data == 'cat_arenda':
        update(f"UPDATE users SET word_1 = 'Аренда' WHERE id_user = '{callback.message.chat.id}'", user)
        values_list = selist(f"SELECT arenda FROM ras WHERE type_col = 'pred'", user)[0]['arenda'].split('&')

        inline_cat = InlineKeyboardMarkup(row_width=1)
        for value in range(len(values_list)):
            inline_cat_b = InlineKeyboardButton(text=values_list[value], callback_data=f'pred_arenda_{value}')
            inline_cat.add(inline_cat_b)
        await callback.message.edit_text(f'Выберите предмет расходов:', reply_markup=inline_cat)
        await callback.answer()
    elif callback.data == 'cat_fot':
        update(f"UPDATE users SET word_1 = 'ФОТ' WHERE id_user = '{callback.message.chat.id}'", user)
        values_list = selist(f"SELECT fot FROM ras WHERE type_col = 'pred'", user)[0]['fot'].split('&')
        inline_cat = InlineKeyboardMarkup(row_width=1)
        for value in range(len(values_list)):
            inline_cat_b = InlineKeyboardButton(text=values_list[value], callback_data=f'pred_fot_{value}')
            inline_cat.add(inline_cat_b)
        await callback.message.edit_text(f'Выберите предмет расходов:', reply_markup=inline_cat)
        await callback.answer()
    elif callback.data == 'cat_rash':
        update(f"UPDATE users SET word_1 = 'Расходники' WHERE id_user = '{callback.message.chat.id}'", user)
        values_list = selist(f"SELECT rashod FROM ras WHERE type_col = 'pred'", user)[0]['rashod'].split('&')
        inline_cat = InlineKeyboardMarkup(row_width=1)
        for value in range(len(values_list)):
            inline_cat_b = InlineKeyboardButton(text=values_list[value], callback_data=f'pred_rash_{value}')
            inline_cat.add(inline_cat_b)
        await callback.message.edit_text(f'Выберите расходник:', reply_markup=inline_cat)
        await callback.answer()
    elif callback.data == 'cat_logist':
        update(f"UPDATE users SET word_1 = 'Логистика' WHERE id_user = '{callback.message.chat.id}'", user)
        values_list = selist(f"SELECT log FROM ras WHERE type_col = 'pred'", user)[0]['log'].split('&')
        inline_cat = InlineKeyboardMarkup(row_width=1)
        for value in range(len(values_list)):
            inline_cat_b = InlineKeyboardButton(text=values_list[value], callback_data=f'pred_logist_{value}')
            inline_cat.add(inline_cat_b)
        await callback.message.edit_text(f'Выберите предмет расходов:', reply_markup=inline_cat)
        await callback.answer()
    elif callback.data == 'cat_outs':
        update(f"UPDATE users SET word_1 = 'Аутсорс' WHERE id_user = '{callback.message.chat.id}'", user)
        values_list = selist(f"SELECT auts FROM ras WHERE type_col = 'pred'", user)[0]['auts'].split('&')
        inline_cat = InlineKeyboardMarkup(row_width=1)
        for value in range(len(values_list)):
            inline_cat_b = InlineKeyboardButton(text=values_list[value], callback_data=f'pred_outs_{value}')
            inline_cat.add(inline_cat_b)
        await callback.message.edit_text(f'Выберите предмет расходов:', reply_markup=inline_cat)
        await callback.answer()
    elif callback.data == 'cat_instr':
        update(f"UPDATE users SET word_1 = 'Инструменты' WHERE id_user = '{callback.message.chat.id}'", user)
        values_list = selist(f"SELECT instr FROM ras WHERE type_col = 'pred'", user)[0]['instr'].split('&')
        inline_cat = InlineKeyboardMarkup(row_width=1)
        for value in range(len(values_list)):
            inline_cat_b = InlineKeyboardButton(text=values_list[value], callback_data=f'pred_instr_{value}')
            inline_cat.add(inline_cat_b)
        await callback.message.edit_text(f'Выберите предмет расходов:', reply_markup=inline_cat)
        await callback.answer()
    elif callback.data == 'cat_other':
        update(f"UPDATE users SET word_1 = 'Прочее' WHERE id_user = '{callback.message.chat.id}'", user)
        values_list = selist(f"SELECT proch FROM ras WHERE type_col = 'pred'", user)[0]['proch'].split('&')
        inline_cat = InlineKeyboardMarkup(row_width=1)
        for value in range(len(values_list)):
            inline_cat_b = InlineKeyboardButton(text=values_list[value], callback_data=f'pred_other_{value}')
            inline_cat.add(inline_cat_b)
        await callback.message.edit_text(f'Выберите предмет расходов:', reply_markup=inline_cat)
        await callback.answer()
    elif 'pred_arenda_' in callback.data:
        id_pred = int(callback.data.split('_')[2])
        pred_list = selist(f"SELECT arenda FROM ras WHERE type_col = 'pred'", user)[0]['arenda'].split('&')
        pred = pred_list[id_pred]

        values_list = selist(f"SELECT arenda FROM ras WHERE type_col = 'kontr'", user)[0]['arenda'].split('&')
        update(f"UPDATE users SET word_2 = '{pred}' WHERE id_user = '{callback.message.chat.id}'", user)

        inline_contr = InlineKeyboardMarkup(row_width=1)
        for value in range(len(values_list)):
            inline_contr_b = InlineKeyboardButton(text=values_list[value], callback_data=f'kontr_arenda_{value}')
            inline_contr.add(inline_contr_b)
        await callback.message.edit_text(f'Выберите контрагента:', reply_markup=inline_contr)
        await callback.answer()
    elif 'pred_fot_' in callback.data:
        id_pred = int(callback.data.split('_')[2])
        pred_list = selist(f"SELECT fot FROM ras WHERE type_col = 'pred'", user)[0]['fot'].split('&')
        pred = pred_list[id_pred]

        values_list = selist(f"SELECT fot FROM ras WHERE type_col = 'kontr'", user)[0]['fot'].split('&')
        update(f"UPDATE users SET word_2 = '{pred}' WHERE id_user = '{callback.message.chat.id}'", user)

        inline_contr = InlineKeyboardMarkup(row_width=1)
        for value in range(len(values_list)):
            inline_contr_b = InlineKeyboardButton(text=values_list[value], callback_data=f'kontr_fot_{value}')
            inline_contr.add(inline_contr_b)
        await callback.message.edit_text(f'Выберите контрагента:', reply_markup=inline_contr)
        await callback.answer()
    elif 'pred_rash_' in callback.data:
        id_pred = int(callback.data.split('_')[2])
        pred_list = selist(f"SELECT rashod FROM ras WHERE type_col = 'pred'", user)[0]['rashod'].split('&')
        pred = pred_list[id_pred]

        values_list = selist(f"SELECT rashod FROM ras WHERE type_col = 'kontr'", user)[0]['rashod'].split('&')
        update(f"UPDATE users SET word_2 = '{pred}' WHERE id_user = '{callback.message.chat.id}'", user)

        inline_contr = InlineKeyboardMarkup(row_width=1)
        for value in range(len(values_list)):
            inline_contr_b = InlineKeyboardButton(text=values_list[value], callback_data=f'kontr_rash_{value}')
            inline_contr.add(inline_contr_b)
        await callback.message.edit_text(f'Выберите контрагента:', reply_markup=inline_contr)
        await callback.answer()
    elif 'pred_logist_' in callback.data:
        id_pred = int(callback.data.split('_')[2])
        pred_list = selist(f"SELECT log FROM ras WHERE type_col = 'pred'", user)[0]['log'].split('&')
        pred = pred_list[id_pred]

        values_list = selist(f"SELECT log FROM ras WHERE type_col = 'kontr'", user)[0]['log'].split('&')
        update(f"UPDATE users SET word_2 = '{pred}' WHERE id_user = '{callback.message.chat.id}'", user)

        inline_contr = InlineKeyboardMarkup(row_width=1)
        for value in range(len(values_list)):
            inline_contr_b = InlineKeyboardButton(text=values_list[value], callback_data=f'kontr_logist_{value}')
            inline_contr.add(inline_contr_b)
        await callback.message.edit_text(f'Выберите контрагента:', reply_markup=inline_contr)
        await callback.answer()
    elif 'pred_outs_' in callback.data:
        id_pred = int(callback.data.split('_')[2])
        pred_list = selist(f"SELECT auts FROM ras WHERE type_col = 'pred'", user)[0]['auts'].split('&')
        pred = pred_list[id_pred]

        values_list = selist(f"SELECT auts FROM ras WHERE type_col = 'kontr'", user)[0]['auts'].split('&')
        update(f"UPDATE users SET word_2 = '{pred}' WHERE id_user = '{callback.message.chat.id}'", user)

        inline_contr = InlineKeyboardMarkup(row_width=1)
        for value in range(len(values_list)):
            inline_contr_b = InlineKeyboardButton(text=values_list[value], callback_data=f'kontr_outs_{value}')
            inline_contr.add(inline_contr_b)
        await callback.message.edit_text(f'Выберите контрагента:', reply_markup=inline_contr)
        await callback.answer()
    elif 'pred_instr_' in callback.data:
        id_pred = int(callback.data.split('_')[2])
        pred_list = selist(f"SELECT instr FROM ras WHERE type_col = 'pred'", user)[0]['instr'].split('&')
        pred = pred_list[id_pred]

        values_list = selist(f"SELECT instr FROM ras WHERE type_col = 'kontr'", user)[0]['instr'].split('&')
        update(f"UPDATE users SET word_2 = '{pred}' WHERE id_user = '{callback.message.chat.id}'", user)

        inline_contr = InlineKeyboardMarkup(row_width=1)
        for value in range(len(values_list)):
            inline_contr_b = InlineKeyboardButton(text=values_list[value], callback_data=f'kontr_instr_{value}')
            inline_contr.add(inline_contr_b)
        await callback.message.edit_text(f'Выберите контрагента:', reply_markup=inline_contr)
        await callback.answer()
    elif 'pred_other_' in callback.data:
        id_pred = int(callback.data.split('_')[2])
        pred_list = selist(f"SELECT proch FROM ras WHERE type_col = 'pred'", user)[0]['proch'].split('&')
        pred = pred_list[id_pred]

        values_list = selist(f"SELECT proch FROM ras WHERE type_col = 'kontr'", user)[0]['proch'].split('&')
        update(f"UPDATE users SET word_2 = '{pred}' WHERE id_user = '{callback.message.chat.id}'", user)

        inline_contr = InlineKeyboardMarkup(row_width=1)
        for value in range(len(values_list)):
            inline_contr_b = InlineKeyboardButton(text=values_list[value], callback_data=f'kontr_other_{value}')
            inline_contr.add(inline_contr_b)
        await callback.message.edit_text(f'Выберите контрагента:', reply_markup=inline_contr)
        await callback.answer()
    elif 'kontr_arenda_' in callback.data:
        id_kontr = int(callback.data.split('_')[2])
        values_list = selist(f"SELECT arenda FROM ras WHERE type_col = 'kontr'", user)[0]['arenda'].split('&')
        kontr = values_list[int(id_kontr)]
        update(f"UPDATE users SET word_3 = '{kontr}' WHERE id_user = '{callback.message.chat.id}'", user)
        update(f"UPDATE users SET act_retail = 1 WHERE id_user = '{callback.message.chat.id}'", user)
        await callback.message.edit_text(f'Введите сумму:')
        await callback.answer()
    elif 'kontr_fot_' in callback.data:
        id_kontr = int(callback.data.split('_')[2])
        values_list = selist(f"SELECT fot FROM ras WHERE type_col = 'kontr'", user)[0]['fot'].split('&')
        kontr = values_list[int(id_kontr)]
        update(f"UPDATE users SET word_3 = '{kontr}' WHERE id_user = '{callback.message.chat.id}'", user)
        update(f"UPDATE users SET act_retail = 1 WHERE id_user = '{callback.message.chat.id}'", user)
        await callback.message.edit_text(f'Введите сумму:')
        await callback.answer()
    elif 'kontr_rash_' in callback.data:
        id_kontr = int(callback.data.split('_')[2])
        values_list = selist(f"SELECT rashod FROM ras WHERE type_col = 'kontr'", user)[0]['rashod'].split('&')
        kontr = values_list[int(id_kontr)]
        update(f"UPDATE users SET word_3 = '{kontr}' WHERE id_user = '{callback.message.chat.id}'", user)
        update(f"UPDATE users SET act_retail = 1 WHERE id_user = '{callback.message.chat.id}'", user)
        await callback.message.edit_text(f'Введите сумму:')
        await callback.answer()
    elif 'kontr_logist_' in callback.data:
        id_kontr = int(callback.data.split('_')[2])
        values_list = selist(f"SELECT log FROM ras WHERE type_col = 'kontr'", user)[0]['log'].split('&')
        kontr = values_list[int(id_kontr)]
        update(f"UPDATE users SET word_3 = '{kontr}' WHERE id_user = '{callback.message.chat.id}'", user)
        update(f"UPDATE users SET act_retail = 1 WHERE id_user = '{callback.message.chat.id}'", user)
        await callback.message.edit_text(f'Введите сумму:')
        await callback.answer()
    elif 'kontr_outs_' in callback.data:
        id_kontr = int(callback.data.split('_')[2])
        values_list = selist(f"SELECT auts FROM ras WHERE type_col = 'kontr'", user)[0]['auts'].split('&')
        kontr = values_list[int(id_kontr)]
        update(f"UPDATE users SET word_3 = '{kontr}' WHERE id_user = '{callback.message.chat.id}'", user)
        update(f"UPDATE users SET act_retail = 1 WHERE id_user = '{callback.message.chat.id}'", user)
        await callback.message.edit_text(f'Введите сумму:')
        await callback.answer()
    elif 'kontr_instr_' in callback.data:
        id_kontr = int(callback.data.split('_')[2])
        values_list = selist(f"SELECT instr FROM ras WHERE type_col = 'kontr'", user)[0]['instr'].split('&')
        kontr = values_list[int(id_kontr)]
        update(f"UPDATE users SET word_3 = '{kontr}' WHERE id_user = '{callback.message.chat.id}'", user)
        update(f"UPDATE users SET act_retail = 1 WHERE id_user = '{callback.message.chat.id}'", user)
        await callback.message.edit_text(f'Введите сумму:')
        await callback.answer()
    elif 'kontr_other_' in callback.data:
        id_kontr = int(callback.data.split('_')[2])
        values_list = selist(f"SELECT proch FROM ras WHERE type_col = 'kontr'", user)[0]['proch'].split('&')
        kontr = values_list[int(id_kontr)]
        update(f"UPDATE users SET word_3 = '{kontr}' WHERE id_user = '{callback.message.chat.id}'", user)
        update(f"UPDATE users SET act_retail = 1 WHERE id_user = '{callback.message.chat.id}'", user)
        await callback.message.edit_text(f'Введите сумму:')
        await callback.answer()
    elif 'pay_fara' in callback.data:
        await callback.answer()
        await callback.message.edit_text('🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥\n`определение даты`', parse_mode='Markdown')
        delta_1 = datetime.timedelta(hours=5)
        now = datetime.datetime.now() + delta_1
        if int(now.day) < 10:
            day_edit = '0' + str(now.day)
        else:
            day_edit = now.day

        if int(now.month) < 10:
            month_edit = '0' + str(now.month)
        else:
            month_edit = now.month
        date_create = f'{day_edit}.{month_edit}.{now.year}'
        await callback.message.edit_text('🟥🟥🟥🟥🟥🟧🟨🟩🟩🟩\n`подключение к таблице`', parse_mode='Markdown')
        name_list = f"Расход {now.year}"

        worksheet = sh.worksheet(name_list)
        await callback.message.edit_text('🟥🟥🟥🟧🟨🟩🟩🟩🟩🟩\n`определение номера строки`', parse_mode='Markdown')
        values_list = worksheet.col_values(1)
        num_row = len(values_list) + 1
        await callback.message.edit_text('🟥🟧🟨🟩🟩🟩🟩🟩🟩🟩\n`заполнение данных`', parse_mode='Markdown')
        worksheet.update(f'A{num_row}:D{num_row}', [[selone(f"SELECT word_1 FROM users WHERE id_user = '{user}'", user)['word_1'],
                                                     date_create,
                                                     selone(f"SELECT word_2 FROM users WHERE id_user = '{user}'", user)['word_2'],
                                                     selone(f"SELECT word_3 FROM users WHERE id_user = '{user}'", user)['word_3']]])

        await callback.message.edit_text('🟧🟨🟩🟩🟩🟩🟩🟩🟩🟩\n`заполнение данных`', parse_mode='Markdown')
        worksheet.update(f'F{num_row}:J{num_row}', [[selone(f"SELECT word_6 FROM users WHERE id_user = '{user}'", user)['word_6'],
                                                     selone(f"SELECT word_5 FROM users WHERE id_user = '{user}'", user)['word_5'],
                                                     selone(f"SELECT word_4 FROM users WHERE id_user = '{user}'", user)['word_4'],
                                                     'Карта Фархат',
                                                     selone(f"SELECT word_8 FROM users WHERE id_user = '{user}'", user)['word_8']]])

        await callback.message.edit_text('✅ Записано! ✅', parse_mode='Markdown')
        await callback.message.answer('Главное меню:', reply_markup=markups.menu_retail)
    elif 'pay_kay' in callback.data:
        await callback.answer()
        await callback.message.edit_text('🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥\n`определение даты`', parse_mode='Markdown')
        delta_1 = datetime.timedelta(hours=5)
        now = datetime.datetime.now() + delta_1
        if int(now.day) < 10:
            day_edit = '0' + str(now.day)
        else:
            day_edit = now.day

        if int(now.month) < 10:
            month_edit = '0' + str(now.month)
        else:
            month_edit = now.month
        date_create = f'{day_edit}.{month_edit}.{now.year}'
        await callback.message.edit_text('🟥🟥🟥🟥🟥🟧🟨🟩🟩🟩\n`подключение к таблице`', parse_mode='Markdown')
        name_list = f"Расход {now.year}"

        worksheet = sh.worksheet(name_list)
        await callback.message.edit_text('🟥🟥🟥🟧🟨🟩🟩🟩🟩🟩\n`определение номера строки`', parse_mode='Markdown')
        values_list = worksheet.col_values(1)
        num_row = len(values_list) + 1
        await callback.message.edit_text('🟥🟧🟨🟩🟩🟩🟩🟩🟩🟩\n`заполнение данных`', parse_mode='Markdown')
        worksheet.update(f'A{num_row}:D{num_row}', [[selone(f"SELECT word_1 FROM users WHERE id_user = '{user}'", user)['word_1'],
                                                     date_create,
                                                     selone(f"SELECT word_2 FROM users WHERE id_user = '{user}'", user)['word_2'],
                                                     selone(f"SELECT word_3 FROM users WHERE id_user = '{user}'", user)['word_3']]])

        await callback.message.edit_text('🟧🟨🟩🟩🟩🟩🟩🟩🟩🟩\n`заполнение данных`', parse_mode='Markdown')
        worksheet.update(f'F{num_row}:J{num_row}', [[selone(f"SELECT word_6 FROM users WHERE id_user = '{user}'", user)['word_6'],
                                                     selone(f"SELECT word_5 FROM users WHERE id_user = '{user}'", user)['word_5'],
                                                     selone(f"SELECT word_4 FROM users WHERE id_user = '{user}'", user)['word_4'],
                                                     'p/c ООО (Альфа банк)',
                                                     selone(f"SELECT word_8 FROM users WHERE id_user = '{user}'", user)['word_8']]])

        await callback.message.edit_text('✅ Записано! ✅', parse_mode='Markdown')
        await callback.message.answer('Главное меню:', reply_markup=markups.menu_retail)
    elif 'pay_ooo' in callback.data:
        await callback.answer()
        await callback.message.edit_text('🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥\n`определение даты`', parse_mode='Markdown')
        delta_1 = datetime.timedelta(hours=5)
        now = datetime.datetime.now() + delta_1
        if int(now.day) < 10:
            day_edit = '0' + str(now.day)
        else:
            day_edit = now.day

        if int(now.month) < 10:
            month_edit = '0' + str(now.month)
        else:
            month_edit = now.month
        date_create = f'{day_edit}.{month_edit}.{now.year}'
        await callback.message.edit_text('🟥🟥🟥🟥🟥🟧🟨🟩🟩🟩\n`подключение к таблице`', parse_mode='Markdown')
        name_list = f"Расход {now.year}"

        worksheet = sh.worksheet(name_list)
        await callback.message.edit_text('🟥🟥🟥🟧🟨🟩🟩🟩🟩🟩\n`определение номера строки`', parse_mode='Markdown')
        values_list = worksheet.col_values(1)
        num_row = len(values_list) + 1
        await callback.message.edit_text('🟥🟧🟨🟩🟩🟩🟩🟩🟩🟩\n`заполнение данных`', parse_mode='Markdown')
        worksheet.update(f'A{num_row}:D{num_row}', [[selone(f"SELECT word_1 FROM users WHERE id_user = '{user}'", user)['word_1'],
                                                     date_create,
                                                     selone(f"SELECT word_2 FROM users WHERE id_user = '{user}'", user)['word_2'],
                                                     selone(f"SELECT word_3 FROM users WHERE id_user = '{user}'", user)['word_3']]])

        await callback.message.edit_text('🟧🟨🟩🟩🟩🟩🟩🟩🟩🟩\n`заполнение данных`', parse_mode='Markdown')
        worksheet.update(f'F{num_row}:J{num_row}', [[selone(f"SELECT word_6 FROM users WHERE id_user = '{user}'", user)['word_6'],
                                                     selone(f"SELECT word_5 FROM users WHERE id_user = '{user}'", user)['word_5'],
                                                     selone(f"SELECT word_4 FROM users WHERE id_user = '{user}'", user)['word_4'],
                                                     'p/c ООО (Тинькофф)',
                                                     selone(f"SELECT word_8 FROM users WHERE id_user = '{user}'", user)['word_8']]])

        await callback.message.edit_text('✅ Записано! ✅', parse_mode='Markdown')

        await callback.message.answer('Главное меню:', reply_markup=markups.menu_retail)
    elif 'pay_ozooo' in callback.data:
        await callback.answer()
        await callback.message.edit_text('🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥\n`определение даты`', parse_mode='Markdown')
        delta_1 = datetime.timedelta(hours=5)
        now = datetime.datetime.now() + delta_1
        if int(now.day) < 10:
            day_edit = '0' + str(now.day)
        else:
            day_edit = now.day

        if int(now.month) < 10:
            month_edit = '0' + str(now.month)
        else:
            month_edit = now.month
        date_create = f'{day_edit}.{month_edit}.{now.year}'
        await callback.message.edit_text('🟥🟥🟥🟥🟥🟧🟨🟩🟩🟩\n`подключение к таблице`', parse_mode='Markdown')
        name_list = f"Расход {now.year}"

        worksheet = sh.worksheet(name_list)
        await callback.message.edit_text('🟥🟥🟥🟧🟨🟩🟩🟩🟩🟩\n`определение номера строки`', parse_mode='Markdown')
        values_list = worksheet.col_values(1)
        num_row = len(values_list) + 1
        await callback.message.edit_text('🟥🟧🟨🟩🟩🟩🟩🟩🟩🟩\n`заполнение данных`', parse_mode='Markdown')
        worksheet.update(f'A{num_row}:D{num_row}', [[selone(f"SELECT word_1 FROM users WHERE id_user = '{user}'", user)['word_1'],
                                                     date_create,
                                                     selone(f"SELECT word_2 FROM users WHERE id_user = '{user}'", user)['word_2'],
                                                     selone(f"SELECT word_3 FROM users WHERE id_user = '{user}'", user)['word_3']]])

        await callback.message.edit_text('🟧🟨🟩🟩🟩🟩🟩🟩🟩🟩\n`заполнение данных`', parse_mode='Markdown')
        worksheet.update(f'F{num_row}:J{num_row}', [[selone(f"SELECT word_6 FROM users WHERE id_user = '{user}'", user)['word_6'],
                                                     selone(f"SELECT word_5 FROM users WHERE id_user = '{user}'", user)['word_5'],
                                                     selone(f"SELECT word_4 FROM users WHERE id_user = '{user}'", user)['word_4'],
                                                     'р/с ООО (Ozon)',
                                                     selone(f"SELECT word_8 FROM users WHERE id_user = '{user}'", user)['word_8']]])

        await callback.message.edit_text('✅ Записано! ✅', parse_mode='Markdown')

        await callback.message.answer('Главное меню:', reply_markup=markups.menu_retail)
    elif 'pay_ozok' in callback.data:
        await callback.answer()
        await callback.message.edit_text('🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥\n`определение даты`', parse_mode='Markdown')
        delta_1 = datetime.timedelta(hours=5)
        now = datetime.datetime.now() + delta_1
        if int(now.day) < 10:
            day_edit = '0' + str(now.day)
        else:
            day_edit = now.day

        if int(now.month) < 10:
            month_edit = '0' + str(now.month)
        else:
            month_edit = now.month
        date_create = f'{day_edit}.{month_edit}.{now.year}'
        await callback.message.edit_text('🟥🟥🟥🟥🟥🟧🟨🟩🟩🟩\n`подключение к таблице`', parse_mode='Markdown')
        name_list = f"Расход {now.year}"

        worksheet = sh.worksheet(name_list)
        await callback.message.edit_text('🟥🟥🟥🟧🟨🟩🟩🟩🟩🟩\n`определение номера строки`', parse_mode='Markdown')
        values_list = worksheet.col_values(1)
        num_row = len(values_list) + 1
        await callback.message.edit_text('🟥🟧🟨🟩🟩🟩🟩🟩🟩🟩\n`заполнение данных`', parse_mode='Markdown')
        worksheet.update(f'A{num_row}:D{num_row}', [[selone(f"SELECT word_1 FROM users WHERE id_user = '{user}'", user)['word_1'],
                                                     date_create,
                                                     selone(f"SELECT word_2 FROM users WHERE id_user = '{user}'", user)['word_2'],
                                                     selone(f"SELECT word_3 FROM users WHERE id_user = '{user}'", user)['word_3']]])

        await callback.message.edit_text('🟧🟨🟩🟩🟩🟩🟩🟩🟩🟩\n`заполнение данных`', parse_mode='Markdown')
        worksheet.update(f'F{num_row}:J{num_row}', [[selone(f"SELECT word_6 FROM users WHERE id_user = '{user}'", user)['word_6'],
                                                     selone(f"SELECT word_5 FROM users WHERE id_user = '{user}'", user)['word_5'],
                                                     selone(f"SELECT word_4 FROM users WHERE id_user = '{user}'", user)['word_4'],
                                                     'р/с ИП Калимуллин (Ozon)',
                                                     selone(f"SELECT word_8 FROM users WHERE id_user = '{user}'", user)['word_8']]])

        await callback.message.edit_text('✅ Записано! ✅', parse_mode='Markdown')

        await callback.message.answer('Главное меню:', reply_markup=markups.menu_retail)
    elif 'pay_ipfara' in callback.data:
        await callback.answer()
        await callback.message.edit_text('🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥\n`определение даты`', parse_mode='Markdown')
        delta_1 = datetime.timedelta(hours=5)
        now = datetime.datetime.now() + delta_1
        if int(now.day) < 10:
            day_edit = '0' + str(now.day)
        else:
            day_edit = now.day

        if int(now.month) < 10:
            month_edit = '0' + str(now.month)
        else:
            month_edit = now.month
        date_create = f'{day_edit}.{month_edit}.{now.year}'
        await callback.message.edit_text('🟥🟥🟥🟥🟥🟧🟨🟩🟩🟩\n`подключение к таблице`', parse_mode='Markdown')
        name_list = f"Расход {now.year}"

        worksheet = sh.worksheet(name_list)
        await callback.message.edit_text('🟥🟥🟥🟧🟨🟩🟩🟩🟩🟩\n`определение номера строки`', parse_mode='Markdown')
        values_list = worksheet.col_values(1)
        num_row = len(values_list) + 1
        await callback.message.edit_text('🟥🟧🟨🟩🟩🟩🟩🟩🟩🟩\n`заполнение данных`', parse_mode='Markdown')
        worksheet.update(f'A{num_row}:D{num_row}', [[selone(f"SELECT word_1 FROM users WHERE id_user = '{user}'", user)['word_1'],
                                                     date_create,
                                                     selone(f"SELECT word_2 FROM users WHERE id_user = '{user}'", user)['word_2'],
                                                     selone(f"SELECT word_3 FROM users WHERE id_user = '{user}'", user)['word_3']]])

        await callback.message.edit_text('🟧🟨🟩🟩🟩🟩🟩🟩🟩🟩\n`заполнение данных`', parse_mode='Markdown')
        worksheet.update(f'F{num_row}:J{num_row}', [[selone(f"SELECT word_6 FROM users WHERE id_user = '{user}'", user)['word_6'],
                                                     selone(f"SELECT word_5 FROM users WHERE id_user = '{user}'", user)['word_5'],
                                                     selone(f"SELECT word_4 FROM users WHERE id_user = '{user}'", user)['word_4'],
                                                     'р/с ИП Истяков (Тинькофф)',
                                                     selone(f"SELECT word_8 FROM users WHERE id_user = '{user}'", user)['word_8']]])

        await callback.message.edit_text('✅ Записано! ✅', parse_mode='Markdown')

        await callback.message.answer('Главное меню:', reply_markup=markups.menu_retail)
    elif 'pay_ipkay' in callback.data:
        await callback.answer()
        await callback.message.edit_text('🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥\n`определение даты`', parse_mode='Markdown')
        delta_1 = datetime.timedelta(hours=5)
        now = datetime.datetime.now() + delta_1
        if int(now.day) < 10:
            day_edit = '0' + str(now.day)
        else:
            day_edit = now.day

        if int(now.month) < 10:
            month_edit = '0' + str(now.month)
        else:
            month_edit = now.month
        date_create = f'{day_edit}.{month_edit}.{now.year}'
        await callback.message.edit_text('🟥🟥🟥🟥🟥🟧🟨🟩🟩🟩\n`подключение к таблице`', parse_mode='Markdown')
        name_list = f"Расход {now.year}"

        worksheet = sh.worksheet(name_list)
        await callback.message.edit_text('🟥🟥🟥🟧🟨🟩🟩🟩🟩🟩\n`определение номера строки`', parse_mode='Markdown')
        values_list = worksheet.col_values(1)
        num_row = len(values_list) + 1
        await callback.message.edit_text('🟥🟧🟨🟩🟩🟩🟩🟩🟩🟩\n`заполнение данных`', parse_mode='Markdown')
        worksheet.update(f'A{num_row}:D{num_row}', [[selone(f"SELECT word_1 FROM users WHERE id_user = '{user}'", user)['word_1'],
                                                     date_create,
                                                     selone(f"SELECT word_2 FROM users WHERE id_user = '{user}'", user)['word_2'],
                                                     selone(f"SELECT word_3 FROM users WHERE id_user = '{user}'", user)['word_3']]])

        await callback.message.edit_text('🟧🟨🟩🟩🟩🟩🟩🟩🟩🟩\n`заполнение данных`', parse_mode='Markdown')
        worksheet.update(f'F{num_row}:J{num_row}', [[selone(f"SELECT word_6 FROM users WHERE id_user = '{user}'", user)['word_6'],
                                                     selone(f"SELECT word_5 FROM users WHERE id_user = '{user}'", user)['word_5'],
                                                     selone(f"SELECT word_4 FROM users WHERE id_user = '{user}'", user)['word_4'],
                                                     'р/с ИП Калимуллин (Тинькофф)',
                                                     selone(f"SELECT word_8 FROM users WHERE id_user = '{user}'", user)['word_8']]])

        await callback.message.edit_text('✅ Записано! ✅', parse_mode='Markdown')

        await callback.message.answer('Главное меню:', reply_markup=markups.menu_retail)
    elif 'pay_rn' in callback.data:
        await callback.answer()
        await callback.message.edit_text('🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥\n`определение даты`', parse_mode='Markdown')
        delta_1 = datetime.timedelta(hours=5)
        now = datetime.datetime.now() + delta_1
        if int(now.day) < 10:
            day_edit = '0' + str(now.day)
        else:
            day_edit = now.day

        if int(now.month) < 10:
            month_edit = '0' + str(now.month)
        else:
            month_edit = now.month
        date_create = f'{day_edit}.{month_edit}.{now.year}'
        await callback.message.edit_text('🟥🟥🟥🟥🟥🟧🟨🟩🟩🟩\n`подключение к таблице`', parse_mode='Markdown')
        name_list = f"Расход {now.year}"

        worksheet = sh.worksheet(name_list)
        await callback.message.edit_text('🟥🟥🟥🟧🟨🟩🟩🟩🟩🟩\n`определение номера строки`', parse_mode='Markdown')
        values_list = worksheet.col_values(1)
        num_row = len(values_list) + 1
        await callback.message.edit_text('🟥🟧🟨🟩🟩🟩🟩🟩🟩🟩\n`заполнение данных`', parse_mode='Markdown')
        worksheet.update(f'A{num_row}:D{num_row}', [[selone(f"SELECT word_1 FROM users WHERE id_user = '{user}'", user)['word_1'],
                                                     date_create,
                                                     selone(f"SELECT word_2 FROM users WHERE id_user = '{user}'", user)['word_2'],
                                                     selone(f"SELECT word_3 FROM users WHERE id_user = '{user}'", user)['word_3']]])

        await callback.message.edit_text('🟧🟨🟩🟩🟩🟩🟩🟩🟩🟩\n`заполнение данных`', parse_mode='Markdown')
        worksheet.update(f'F{num_row}:J{num_row}', [[selone(f"SELECT word_6 FROM users WHERE id_user = '{user}'", user)['word_6'],
                                                     selone(f"SELECT word_5 FROM users WHERE id_user = '{user}'", user)['word_5'],
                                                     selone(f"SELECT word_4 FROM users WHERE id_user = '{user}'", user)['word_4'],
                                                     'РН-Карт',
                                                     selone(f"SELECT word_8 FROM users WHERE id_user = '{user}'", user)['word_8']]])

        await callback.message.edit_text('✅ Записано! ✅', parse_mode='Markdown')

        await callback.message.answer('Главное меню:', reply_markup=markups.menu_retail)
    elif 'pay_avito' in callback.data:
        await callback.answer()
        await callback.message.edit_text('🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥\n`определение даты`', parse_mode='Markdown')
        delta_1 = datetime.timedelta(hours=5)
        now = datetime.datetime.now() + delta_1
        if int(now.day) < 10:
            day_edit = '0' + str(now.day)
        else:
            day_edit = now.day

        if int(now.month) < 10:
            month_edit = '0' + str(now.month)
        else:
            month_edit = now.month
        date_create = f'{day_edit}.{month_edit}.{now.year}'
        await callback.message.edit_text('🟥🟥🟥🟥🟥🟧🟨🟩🟩🟩\n`подключение к таблице`', parse_mode='Markdown')
        name_list = f"Расход {now.year}"

        worksheet = sh.worksheet(name_list)
        await callback.message.edit_text('🟥🟥🟥🟧🟨🟩🟩🟩🟩🟩\n`определение номера строки`', parse_mode='Markdown')
        values_list = worksheet.col_values(1)
        num_row = len(values_list) + 1
        await callback.message.edit_text('🟥🟧🟨🟩🟩🟩🟩🟩🟩🟩\n`заполнение данных`', parse_mode='Markdown')
        worksheet.update(f'A{num_row}:D{num_row}', [[selone(f"SELECT word_1 FROM users WHERE id_user = '{user}'", user)['word_1'],
                                                     date_create,
                                                     selone(f"SELECT word_2 FROM users WHERE id_user = '{user}'", user)['word_2'],
                                                     selone(f"SELECT word_3 FROM users WHERE id_user = '{user}'", user)['word_3']]])

        await callback.message.edit_text('🟧🟨🟩🟩🟩🟩🟩🟩🟩🟩\n`заполнение данных`', parse_mode='Markdown')
        worksheet.update(f'F{num_row}:J{num_row}', [[selone(f"SELECT word_6 FROM users WHERE id_user = '{user}'", user)['word_6'],
                                                     selone(f"SELECT word_5 FROM users WHERE id_user = '{user}'", user)['word_5'],
                                                     selone(f"SELECT word_4 FROM users WHERE id_user = '{user}'", user)['word_4'],
                                                     'Авито',
                                                     selone(f"SELECT word_8 FROM users WHERE id_user = '{user}'", user)['word_8']]])

        await callback.message.edit_text('✅ Записано! ✅', parse_mode='Markdown')

        await callback.message.answer('Главное меню:', reply_markup=markups.menu_retail)
    elif 'pay_modbank' in callback.data:
        await callback.answer()
        await callback.message.edit_text('🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥\n`определение даты`', parse_mode='Markdown')
        delta_1 = datetime.timedelta(hours=5)
        now = datetime.datetime.now() + delta_1
        if int(now.day) < 10:
            day_edit = '0' + str(now.day)
        else:
            day_edit = now.day

        if int(now.month) < 10:
            month_edit = '0' + str(now.month)
        else:
            month_edit = now.month
        date_create = f'{day_edit}.{month_edit}.{now.year}'
        await callback.message.edit_text('🟥🟥🟥🟥🟥🟧🟨🟩🟩🟩\n`подключение к таблице`', parse_mode='Markdown')
        name_list = f"Расход {now.year}"

        worksheet = sh.worksheet(name_list)
        await callback.message.edit_text('🟥🟥🟥🟧🟨🟩🟩🟩🟩🟩\n`определение номера строки`', parse_mode='Markdown')
        values_list = worksheet.col_values(1)
        num_row = len(values_list) + 1
        await callback.message.edit_text('🟥🟧🟨🟩🟩🟩🟩🟩🟩🟩\n`заполнение данных`', parse_mode='Markdown')
        worksheet.update(f'A{num_row}:D{num_row}', [[selone(f"SELECT word_1 FROM users WHERE id_user = '{user}'", user)['word_1'],
                                                     date_create,
                                                     selone(f"SELECT word_2 FROM users WHERE id_user = '{user}'", user)['word_2'],
                                                     selone(f"SELECT word_3 FROM users WHERE id_user = '{user}'", user)['word_3']]])

        await callback.message.edit_text('🟧🟨🟩🟩🟩🟩🟩🟩🟩🟩\n`заполнение данных`', parse_mode='Markdown')
        worksheet.update(f'F{num_row}:J{num_row}', [[selone(f"SELECT word_6 FROM users WHERE id_user = '{user}'", user)['word_6'],
                                                     selone(f"SELECT word_5 FROM users WHERE id_user = '{user}'", user)['word_5'],
                                                     selone(f"SELECT word_4 FROM users WHERE id_user = '{user}'", user)['word_4'],
                                                     'Модуль Банк',
                                                     selone(f"SELECT word_8 FROM users WHERE id_user = '{user}'", user)['word_8']]])

        await callback.message.edit_text('✅ Записано! ✅', parse_mode='Markdown')

        await callback.message.answer('Главное меню:', reply_markup=markups.menu_retail)
    elif 'pay_nonepay' in callback.data:
        await callback.answer()
        await callback.message.edit_text('🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥\n`определение даты`', parse_mode='Markdown')
        delta_1 = datetime.timedelta(hours=5)
        now = datetime.datetime.now() + delta_1
        if int(now.day) < 10:
            day_edit = '0' + str(now.day)
        else:
            day_edit = now.day

        if int(now.month) < 10:
            month_edit = '0' + str(now.month)
        else:
            month_edit = now.month
        date_create = f'{day_edit}.{month_edit}.{now.year}'
        await callback.message.edit_text('🟥🟥🟥🟥🟥🟧🟨🟩🟩🟩\n`подключение к таблице`', parse_mode='Markdown')
        name_list = f"Расход {now.year}"

        worksheet = sh.worksheet(name_list)
        await callback.message.edit_text('🟥🟥🟥🟧🟨🟩🟩🟩🟩🟩\n`определение номера строки`', parse_mode='Markdown')
        values_list = worksheet.col_values(1)
        num_row = len(values_list) + 1
        await callback.message.edit_text('🟥🟧🟨🟩🟩🟩🟩🟩🟩🟩\n`заполнение данных`', parse_mode='Markdown')
        worksheet.update(f'A{num_row}:D{num_row}', [[selone(f"SELECT word_1 FROM users WHERE id_user = '{user}'", user)['word_1'],
                                                     date_create,
                                                     selone(f"SELECT word_2 FROM users WHERE id_user = '{user}'", user)['word_2'],
                                                     selone(f"SELECT word_3 FROM users WHERE id_user = '{user}'", user)['word_3']]])

        await callback.message.edit_text('🟧🟨🟩🟩🟩🟩🟩🟩🟩🟩\n`заполнение данных`', parse_mode='Markdown')
        worksheet.update(f'F{num_row}:H{num_row}', [[selone(f"SELECT word_6 FROM users WHERE id_user = '{user}'", user)['word_6'],
                                                     selone(f"SELECT word_5 FROM users WHERE id_user = '{user}'", user)['word_5'],
                                                     selone(f"SELECT word_4 FROM users WHERE id_user = '{user}'", user)['word_4']]])

        worksheet.update(f'J{num_row}', [[selone(f"SELECT word_8 FROM users WHERE id_user = '{user}'", user)['word_8']]])

        await callback.message.edit_text('✅ Записано! ✅', parse_mode='Markdown')
        await callback.message.answer('Главное меню:', reply_markup=markups.menu_retail)

    # Подтвердить расход
    elif 'rshod_' in callback.data:
        await callback.answer()
        num_row = callback.data.split('_')[1]
        year = callback.data.split('_')[2]

        inline_pay_2 = InlineKeyboardMarkup(row_width=1)
        inline_pay_2_b1 = InlineKeyboardButton(text='Карта Фархат', callback_data=f'pay2_fara_{num_row}_{year}')
        inline_pay_2_b2 = InlineKeyboardButton(text='p/c ООО (Альфа банк)', callback_data=f'pay2_kay_{num_row}_{year}')
        inline_pay_2_b3 = InlineKeyboardButton(text='p/c ООО (Тинькофф)', callback_data=f'pay2_ooo_{num_row}_{year}')
        inline_pay_2_b4 = InlineKeyboardButton(text='р/с ИП Истяков (Тинькофф)', callback_data=f'pay2_ipfara_{num_row}_{year}')
        inline_pay_2_b5 = InlineKeyboardButton(text='р/с ИП Калимуллин (Тинькофф)', callback_data=f'pay2_ipkay_{num_row}_{year}')
        inline_pay_2_b6 = InlineKeyboardButton(text='р/с ИП Калимуллин (Ozon)', callback_data=f'pay2_ozok_{num_row}_{year}')
        inline_pay_2_b7 = InlineKeyboardButton(text='р/с ООО (Ozon)', callback_data=f'pay2_ozooo_{num_row}_{year}')
        inline_pay_2_b8 = InlineKeyboardButton(text='РН-Карт', callback_data=f'pay2_rn_{num_row}_{year}')
        inline_pay_2_b9 = InlineKeyboardButton(text='Авито', callback_data=f'pay2_avito_{num_row}_{year}')
        inline_pay_2_b10 = InlineKeyboardButton(text='Модуль Банк', callback_data=f'pay2_modbank_{num_row}_{year}')
        inline_pay_2.add(inline_pay_2_b1).add(inline_pay_2_b2).add(inline_pay_2_b3).add(inline_pay_2_b4).add(inline_pay_2_b5).add(inline_pay_2_b6).add(inline_pay_2_b7).add(inline_pay_2_b8).add(inline_pay_2_b9).add(inline_pay_2_b10)

        await callback.message.edit_text(text=f'C какого счета была оплата?', reply_markup=inline_pay_2)
    elif 'pay2_' in callback.data:
        await callback.answer()
        await callback.message.edit_text('🟥🟥🟥🟥🟥🟥🟥🟥🟥\n`выделение переменных`', parse_mode='Markdown')
        type_pay = callback.data.split('_')[1]
        num_row = callback.data.split('_')[2]
        year = callback.data.split('_')[3]

        if type_pay == 'fara':
            name_pay = 'Карта Фархат'
        elif type_pay == 'kay':
            name_pay = 'p/c ООО (Альфа банк)'
        elif type_pay == 'ooo':
            name_pay = 'p/c ООО (Тинькофф)'
        elif type_pay == 'ipfara':
            name_pay = 'р/с ИП Истяков (Тинькофф)'
        elif type_pay == 'ozok':
            name_pay = 'р/с ИП Калимуллин (Ozon)'
        elif type_pay == 'ozooo':
            name_pay = 'р/с ООО (Ozon)'
        elif type_pay == 'rn':
            name_pay = 'РН-Карт'
        elif type_pay == 'avito':
            name_pay = 'Авито'
        elif type_pay == 'modbank':
            name_pay = 'Модуль Банк'
        elif type_pay == 'ipkay':
            name_pay = 'р/с ИП Калимуллин (Тинькофф)'
        await callback.message.edit_text('🟥🟥🟥🟥🟥🟥🟧🟧🟨\n`подключение к таблице`', parse_mode='Markdown')
        name_list = f"Расход {year}"
        worksheet = sh.worksheet(name_list)
        await callback.message.edit_text('🟥🟧🟧🟧🟨🟨🟨🟩🟩\n`заполнение счета оплаты`', parse_mode='Markdown')
        worksheet.update_cell(num_row, 9, name_pay)
        await callback.message.edit_text('🟧🟨🟨🟩🟩🟩🟩🟩🟩\n`заполнение факта оплаты`', parse_mode='Markdown')
        worksheet.update_cell(num_row, 10, 'Оплачено')

        await callback.message.edit_text(text=f'✅ Счет на сумму <b>{worksheet.cell(num_row, 8).value}</b> оплачен ✅')
        await callback.message.answer('Главное меню:', reply_markup=markups.menu_retail)

    # Прибыло Склад Мебель
    elif 'pribmeb_' in callback.data:
        object_name = callback.data.split('_')[1]
        ed = selone(f"SELECT ed_2 FROM warehouse_c WHERE name_item = '{object_name}'", user)['ed_2']

        update(f"UPDATE users SET act_sk = '{callback.data}_no' WHERE id_user = '{user}'", user)
        await callback.message.edit_text(text=f'Сколько <b>{ed}</b> прибыло позиции <b>«{object_name}»</b>?')

        await callback.answer()

    # Уехало Мебель
    elif 'uemeb_' in callback.data:
        object_name = callback.data.split('_')[1]
        ed = selone(f"SELECT ed_2 FROM warehouse_c WHERE name_item = '{object_name}'", user)['ed_2']
        update(f"UPDATE users SET act_sk = '{callback.data}' WHERE id_user = '{user}'", user)
        await callback.message.edit_text(text=f'Сколько <b>{ed}</b> уехало позиции <b>«{object_name}»</b>?')
        await callback.answer()

    # Брак
    elif 'brk_' in callback.data:
        await callback.message.delete()

        update(f"UPDATE users SET act_sk = '{callback.data}' WHERE id_user = '{user}'", user)
        await callback.message.answer(text=f'Сколько штук брака позиции <b>«{callback.data[4:]}»</b>?', reply_markup=markups.back_count_retail, parse_mode='HTML')
        await callback.answer()

    # Закрыть смену
    elif 'work_' in callback.data:
        name_worker = callback.data.split('_')[1]

        count_workers = int(selone(f"SELECT act_sk FROM users WHERE id_user = '{user}'", user)['act_sk'].split('_')[1]) - 1

        res = f'count_{count_workers}'
        update(f"UPDATE users SET act_sk = '{res}' WHERE id_user = '{user}'", user)

        with open('user', 'r', encoding='utf-8') as outfile:
            name_objects = json.load(outfile)

        for i in range(len(name_objects[0])):
            if name_objects[0][i] == name_worker:
                del name_objects[0][i]
                break

        name_objects[1][name_worker] = []

        with open('user', 'w', encoding='utf-8') as outfile:
            json.dump(name_objects, outfile, ensure_ascii=False)

        inline_time = InlineKeyboardMarkup(row_width=3)
        inline_time_b1 = InlineKeyboardButton(text='9:00', callback_data=f'timebegin_9:00_{name_worker}')
        inline_time_b2 = InlineKeyboardButton(text='9:20', callback_data=f'timebegin_9:20_{name_worker}')
        inline_time_b3 = InlineKeyboardButton(text='9:40', callback_data=f'timebegin_9:40_{name_worker}')
        inline_time_b4 = InlineKeyboardButton(text='10:00', callback_data=f'timebegin_10:00_{name_worker}')
        inline_time_b5 = InlineKeyboardButton(text='10:20', callback_data=f'timebegin_10:20_{name_worker}')
        inline_time_b6 = InlineKeyboardButton(text='10:40', callback_data=f'timebegin_10:40_{name_worker}')
        inline_time_b7 = InlineKeyboardButton(text='11:00', callback_data=f'timebegin_11:00_{name_worker}')
        inline_time_b8 = InlineKeyboardButton(text='11:20', callback_data=f'timebegin_11:20_{name_worker}')
        inline_time_b9 = InlineKeyboardButton(text='11:40', callback_data=f'timebegin_11:40_{name_worker}')
        inline_time_b10 = InlineKeyboardButton(text='12:00', callback_data=f'timebegin_12:00_{name_worker}')
        inline_time_b11 = InlineKeyboardButton(text='12:20', callback_data=f'timebegin_12:20_{name_worker}')
        inline_time_b12 = InlineKeyboardButton(text='12:40', callback_data=f'timebegin_12:40_{name_worker}')
        inline_time_b13 = InlineKeyboardButton(text='13:00', callback_data=f'timebegin_13:00_{name_worker}')
        inline_time_b14 = InlineKeyboardButton(text='13:20', callback_data=f'timebegin_13:20_{name_worker}')
        inline_time_b15 = InlineKeyboardButton(text='13:40', callback_data=f'timebegin_13:40_{name_worker}')
        inline_time_b16 = InlineKeyboardButton(text='14:00', callback_data=f'timebegin_14:00_{name_worker}')
        inline_time_b17 = InlineKeyboardButton(text='14:20', callback_data=f'timebegin_14:20_{name_worker}')
        inline_time_b18 = InlineKeyboardButton(text='14:40', callback_data=f'timebegin_14:40_{name_worker}')
        inline_time_b19 = InlineKeyboardButton(text='15:00', callback_data=f'timebegin_15:00_{name_worker}')
        inline_time_b20 = InlineKeyboardButton(text='15:20', callback_data=f'timebegin_15:20_{name_worker}')
        inline_time_b21 = InlineKeyboardButton(text='15:40', callback_data=f'timebegin_15:40_{name_worker}')
        inline_time_b22 = InlineKeyboardButton(text='16:00', callback_data=f'timebegin_16:00_{name_worker}')
        inline_time_b23 = InlineKeyboardButton(text='16:20', callback_data=f'timebegin_16:20_{name_worker}')
        inline_time_b24 = InlineKeyboardButton(text='16:40', callback_data=f'timebegin_16:40_{name_worker}')
        inline_time.add(inline_time_b1, inline_time_b2, inline_time_b3).add(inline_time_b4, inline_time_b5, inline_time_b6)\
            .add(inline_time_b7, inline_time_b8, inline_time_b9).add(inline_time_b10, inline_time_b11, inline_time_b12)\
            .add(inline_time_b13, inline_time_b14, inline_time_b15).add(inline_time_b16, inline_time_b17, inline_time_b18)\
            .add(inline_time_b19, inline_time_b20, inline_time_b21).add(inline_time_b22, inline_time_b23, inline_time_b24)

        await callback.message.edit_text(text=f'Во сколько начал работу {name_worker}:', reply_markup=inline_time)
        await callback.answer()
    elif 'timebegin_' in callback.data:

        name_worker = callback.data.split('_')[2]
        time_begin = callback.data.split('_')[1]
        inline_time = InlineKeyboardMarkup(row_width=3)
        inline_time_b1 = InlineKeyboardButton(text='14:00', callback_data=f'timeend_{time_begin}_14:00_{name_worker}')
        inline_time_b2 = InlineKeyboardButton(text='14:20', callback_data=f'timeend_{time_begin}_14:20_{name_worker}')
        inline_time_b3 = InlineKeyboardButton(text='14:40', callback_data=f'timeend_{time_begin}_14:40_{name_worker}')
        inline_time_b4 = InlineKeyboardButton(text='15:00', callback_data=f'timeend_{time_begin}_15:00_{name_worker}')
        inline_time_b5 = InlineKeyboardButton(text='15:20', callback_data=f'timeend_{time_begin}_15:20_{name_worker}')
        inline_time_b6 = InlineKeyboardButton(text='15:40', callback_data=f'timeend_{time_begin}_15:40_{name_worker}')
        inline_time_b7 = InlineKeyboardButton(text='16:00', callback_data=f'timeend_{time_begin}_16:00_{name_worker}')
        inline_time_b8 = InlineKeyboardButton(text='16:20', callback_data=f'timeend_{time_begin}_16:20_{name_worker}')
        inline_time_b9 = InlineKeyboardButton(text='16:40', callback_data=f'timeend_{time_begin}_16:40_{name_worker}')
        inline_time_b10 = InlineKeyboardButton(text='17:00', callback_data=f'timeend_{time_begin}_17:00_{name_worker}')
        inline_time_b11 = InlineKeyboardButton(text='17:20', callback_data=f'timeend_{time_begin}_17:20_{name_worker}')
        inline_time_b12 = InlineKeyboardButton(text='17:40', callback_data=f'timeend_{time_begin}_17:40_{name_worker}')
        inline_time_b13 = InlineKeyboardButton(text='18:00', callback_data=f'timeend_{time_begin}_18:00_{name_worker}')
        inline_time_b14 = InlineKeyboardButton(text='18:20', callback_data=f'timeend_{time_begin}_18:20_{name_worker}')
        inline_time_b15 = InlineKeyboardButton(text='18:40', callback_data=f'timeend_{time_begin}_18:40_{name_worker}')
        inline_time_b16 = InlineKeyboardButton(text='19:00', callback_data=f'timeend_{time_begin}_19:00_{name_worker}')
        inline_time_b17 = InlineKeyboardButton(text='19:20', callback_data=f'timeend_{time_begin}_19:20_{name_worker}')
        inline_time_b18 = InlineKeyboardButton(text='19:40', callback_data=f'timeend_{time_begin}_19:40_{name_worker}')
        inline_time_b19 = InlineKeyboardButton(text='20:00', callback_data=f'timeend_{time_begin}_20:00_{name_worker}')
        inline_time_b20 = InlineKeyboardButton(text='20:20', callback_data=f'timeend_{time_begin}_20:20_{name_worker}')
        inline_time_b21 = InlineKeyboardButton(text='20:40', callback_data=f'timeend_{time_begin}_20:40_{name_worker}')
        inline_time_b22 = InlineKeyboardButton(text='21:00', callback_data=f'timeend_{time_begin}_21:00_{name_worker}')
        inline_time_b23 = InlineKeyboardButton(text='21:20', callback_data=f'timeend_{time_begin}_21:20_{name_worker}')
        inline_time_b24 = InlineKeyboardButton(text='21:40', callback_data=f'timeend_{time_begin}_21:40_{name_worker}')
        inline_time.add(inline_time_b1, inline_time_b2, inline_time_b3).add(inline_time_b4, inline_time_b5, inline_time_b6)\
            .add(inline_time_b7, inline_time_b8, inline_time_b9).add(inline_time_b10, inline_time_b11, inline_time_b12)\
            .add(inline_time_b13, inline_time_b14, inline_time_b15).add(inline_time_b16, inline_time_b17, inline_time_b18)\
            .add(inline_time_b19, inline_time_b20, inline_time_b21).add(inline_time_b22, inline_time_b23, inline_time_b24)

        await callback.message.edit_text(text=f'Во сколько закончил работу {name_worker}:', reply_markup=inline_time)
        await callback.answer()
    elif 'timeend_' in callback.data:

        name_worker = callback.data.split('_')[3]
        time_begin = callback.data.split('_')[1]
        time_end = callback.data.split('_')[2]

        count_workers = int(selone(f"SELECT act_sk FROM users WHERE id_user = '{user}'", user)['act_sk'].split('_')[1])

        with open('user', 'r', encoding='utf-8') as outfile:
            name_objects = json.load(outfile)

        name_objects[1][name_worker] = [time_begin, time_end]

        with open('user', 'w', encoding='utf-8') as outfile:
            json.dump(name_objects, outfile, ensure_ascii=False)

        if count_workers > 0:
            inline_workers = InlineKeyboardMarkup(row_width=1)
            for w in name_objects[0]:
                inline_workers_b = InlineKeyboardButton(text=w, callback_data=f'work_{w}')
                inline_workers.add(inline_workers_b)

            await callback.message.edit_text(text='Выберите следующего сотрудника:', reply_markup=inline_workers)
        else:
            res = 'rastysh1_'
            update(f"UPDATE users SET act_sk = '{res}' WHERE id_user = '{user}'", user)
            await callback.message.edit_text('Сколько сегодня произведено Растущих 1?')
        await callback.answer()

    # Ночная смена
    elif 'works_' in callback.data:
        name_worker = callback.data.split('_')[1]

        count_workers = int(selone(f"SELECT act_sk FROM users WHERE id_user = '{user}'", user)['act_sk'].split('_')[1]) - 1

        res = f'counts_{count_workers}'
        update(f"UPDATE users SET act_sk = '{res}' WHERE id_user = '{user}'", user)

        with open('user', 'r', encoding='utf-8') as outfile:
            name_objects = json.load(outfile)

        for i in range(len(name_objects[0])):
            if name_objects[0][i] == name_worker:
                del name_objects[0][i]
                break

        name_objects[1][name_worker] = []

        with open('user', 'w', encoding='utf-8') as outfile:
            json.dump(name_objects, outfile, ensure_ascii=False)

        name_worker = callback.data.split('_')[1]
        time_begin = 0
        time_end = 0

        count_workers = int(selone(f"SELECT act_sk FROM users WHERE id_user = '{user}'", user)['act_sk'].split('_')[1])

        with open('user', 'r', encoding='utf-8') as outfile:
            name_objects = json.load(outfile)

        name_objects[1][name_worker] = [time_begin, time_end]

        with open('user', 'w', encoding='utf-8') as outfile:
            json.dump(name_objects, outfile, ensure_ascii=False)

        if count_workers > 0:
            inline_workers = InlineKeyboardMarkup(row_width=1)
            for w in name_objects[0]:
                inline_workers_b = InlineKeyboardButton(text=w, callback_data=f'works_{w}')
                inline_workers.add(inline_workers_b)

            await callback.message.edit_text(text='Выберите следующего сотрудника:', reply_markup=inline_workers)
        else:
            res = 'rastyshs1_'
            update(f"UPDATE users SET act_sk = '{res}' WHERE id_user = '{user}'", user)
            await callback.message.edit_text('Сколько произведено Растущих 1?')
        await callback.answer()

    # Логистика
    elif 'logis_' in callback.data:
        await callback.message.delete()
        list_call = callback.data.split('_')
        date_ship = list_call[1]
        id_ship = list_call[2]
        num_ship = int(selone(f"SELECT act_log FROM users WHERE id_user = '{user}'", user)['act_log'])
        count_logis = int(selone(f"SELECT count_logis FROM users WHERE id_user = '{user}'", user)['count_logis']) + 1
        new_num = num_ship + 100
        update(f"UPDATE shipping SET num_ship = '{num_ship}' WHERE id_ship = '{id_ship}'", user)
        if count_logis != len(selist(f"SELECT * FROM shipping WHERE date_ship = '{date_ship}' AND status_ship = 'В очереди'", user)):
            update(f"UPDATE users SET act_log = '{new_num}' WHERE id_user = '{user}'", user)
            update(f"UPDATE users SET count_logis = '{count_logis}' WHERE id_user = '{user}'", user)
        else:
            update(f"UPDATE users SET act_log = ' ' WHERE id_user = '{user}'", user)
            update(f"UPDATE users SET count_logis = 0 WHERE id_user = '{user}'", user)
            create(f"REPLACE INTO work_ship(date_work) VALUES ('{date_ship}')", user)
            await callback.message.answer('Маршрутный лист сформирован!')
            await callback.message.answer(text=f'Меню логистики', reply_markup=markups.menu_logistic)
        await callback.answer()
    elif 'logisno_' in callback.data:
        list_call = callback.data.split('_')
        id_ship = list_call[1]

        inline_m = InlineKeyboardMarkup(row_width=2)
        inline_m_b1 = InlineKeyboardButton(text='Отменить', callback_data=f'logisnoyes_{id_ship}')
        inline_m_b2 = InlineKeyboardButton(text='Нет', callback_data=f'logisnono_{id_ship}')
        inline_m.add(inline_m_b1, inline_m_b2)

        l = selist(f"SELECT * FROM shipping WHERE id_ship = '{id_ship}'", user)[0]
        await callback.message.edit_text(text=f'ID: *{l["id_ship"]}*\n'
                                  f'Тип: *{l["type_ship"]}*\n'
                                  f'Дата: *{l["date_ship"]}*\n'
                                  f'Время: *{l["time_ship"]}*\n'
                                  f'Предмет: *{l["item_ship"]}*\n'
                                  f'Количество: *{l["count_item_ship"]}*\n'
                                  f'Вес: *{l["w_ship"]}*\n\n'
                                  f'Адрес загрузки: `{l["adress_begin"]}`\n'
                                  f'Адрес разгрузки: `{l["adress_end"]}`\n'
                                  f'Комментарий: *{l["comment_ship"]}*\n\n'
                                  f'Вы действительно хотите отменить заявку?', parse_mode='Markdown',
                             reply_markup=inline_m)
        await callback.answer()
    elif 'logisnoyes_' in callback.data:
        await callback.message.delete()
        list_call = callback.data.split('_')
        id_ship = list_call[1]
        update(f"UPDATE shipping SET status_ship = 'Отменен' WHERE id_ship = '{id_ship}'", user)
        nons = selone(f"SELECT nons FROM shipping WHERE id_ship = '{id_ship}'", user)['nons']
        update(f"UPDATE new_fbo SET status_zakaz = 100 WHERE nons = '{nons}'", user)

        l = selist(f"SELECT * FROM shipping WHERE id_ship = '{id_ship}'", user)[0]

        list_all_users = selist(f"SELECT * FROM users", user)
        list_users = []
        for us in list_all_users:
            if 'log' in us['notif']:
                list_users.append(us)
        for user1 in list_users:
            try:
                chat_id = str(user1["id_user"])
                destination_bot = Bot(token='6490496152:AAHnBwfDRlUTyTFMOMGGCK6Eu3WejYpesIE')
                await destination_bot.send_message(chat_id, f'*Заявка отменена!*\n\n'
                                                            f'ID: *{l["id_ship"]}*\n'
                                              f'Тип: *{l["type_ship"]}*\n'
                                              f'Дата: *{l["date_ship"]}*\n'
                                              f'Время: *{l["time_ship"]}*\n'
                                              f'Предмет: *{l["item_ship"]}*\n'
                                              f'Количество: *{l["count_item_ship"]}*\n'
                                              f'Вес: *{l["w_ship"]}*\n\n'
                                              f'Адрес загрузки: `{l["adress_begin"]}`\n'
                                              f'Адрес разгрузки: `{l["adress_end"]}`\n'
                                              f'Комментарий: *{l["comment_ship"]}*\n\n',
                                                   parse_mode='Markdown')
            except:
                pass

        await callback.answer()
    elif 'logisnono_' in callback.data:
        list_call = callback.data.split('_')
        id_ship = list_call[1]
        l = selist(f"SELECT * FROM shipping WHERE id_ship = '{id_ship}'", user)[0]

        inline_m = InlineKeyboardMarkup(row_width=2)
        inline_m_b1 = InlineKeyboardButton(text='В очередь', callback_data=f'logis_{l["date_ship"]}_{l["id_ship"]}')
        inline_m_b2 = InlineKeyboardButton(text='Отменить', callback_data=f'logisno_{l["id_ship"]}')
        inline_m_b3 = InlineKeyboardButton(text='Редактировать', callback_data=f'logisedit_{l["id_ship"]}')
        inline_m.add(inline_m_b1, inline_m_b2).add(inline_m_b3)


        await callback.message.edit_text(text=f'ID: *{l["id_ship"]}*\n'
                                  f'Тип: *{l["type_ship"]}*\n'
                                  f'Дата: *{l["date_ship"]}*\n'
                                  f'Время: *{l["time_ship"]}*\n'
                                  f'Предмет: *{l["item_ship"]}*\n'
                                  f'Количество: *{l["count_item_ship"]}*\n'
                                  f'Вес: *{l["w_ship"]}*\n\n'
                                  f'Адрес загрузки: `{l["adress_begin"]}`\n'
                                  f'Адрес разгрузки: `{l["adress_end"]}`\n'
                                  f'Комментарий: *{l["comment_ship"]}*\n\n'
                                  f'Вы действительно хотите отменить заявку?', parse_mode='Markdown',
                             reply_markup=inline_m)
        await callback.answer()
    elif 'logisedit_' in callback.data:
        update(f"UPDATE users SET edit_log = ' ' WHERE id_user = '{user}'", user)
        list_call = callback.data.split('_')
        id_ship = list_call[1]
        l = selist(f"SELECT * FROM shipping WHERE id_ship = '{id_ship}'", user)[0]

        inline_m = InlineKeyboardMarkup(row_width=2)
        inline_m_b1 = InlineKeyboardButton(text='Дата', callback_data=f'logised_дата_{l["id_ship"]}')
        inline_m_b2 = InlineKeyboardButton(text='Время', callback_data=f'logised_время_{l["id_ship"]}')
        inline_m_b3 = InlineKeyboardButton(text='Количество', callback_data=f'logised_количество_{l["id_ship"]}')
        inline_m_b4 = InlineKeyboardButton(text='Вес', callback_data=f'logised_вес_{l["id_ship"]}')
        inline_m_b5 = InlineKeyboardButton(text='Адрес загрузки', callback_data=f'logised_адресз_{l["id_ship"]}')
        inline_m_b6 = InlineKeyboardButton(text='Адрес разгрузки', callback_data=f'logised_адреср_{l["id_ship"]}')
        inline_m_b7 = InlineKeyboardButton(text='Комментарий', callback_data=f'logised_коммент_{l["id_ship"]}')
        inline_m_b8 = InlineKeyboardButton(text='⬅️ Назад', callback_data=f'logisnono_{l["id_ship"]}')
        inline_m.add(inline_m_b1, inline_m_b2).add(inline_m_b3, inline_m_b4).add(inline_m_b5, inline_m_b6).add(inline_m_b7).add(inline_m_b8)


        await callback.message.edit_text(text=f'ID: *{l["id_ship"]}*\n'
                                  f'Тип: *{l["type_ship"]}*\n'
                                  f'Дата: *{l["date_ship"]}*\n'
                                  f'Время: *{l["time_ship"]}*\n'
                                  f'Предмет: *{l["item_ship"]}*\n'
                                  f'Количество: *{l["count_item_ship"]}*\n'
                                  f'Вес: *{l["w_ship"]}*\n\n'
                                  f'Адрес загрузки: `{l["adress_begin"]}`\n'
                                  f'Адрес разгрузки: `{l["adress_end"]}`\n'
                                  f'Комментарий: *{l["comment_ship"]}*\n\n'
                                  f'Что хотите отредактировать?', parse_mode='Markdown',
                             reply_markup=inline_m)
        await callback.answer()
    elif 'logised_' in callback.data:
        update(f"UPDATE users SET edit_log = '{callback.data}' WHERE id_user = '{user}'", user)
        list_call = callback.data.split('_')
        val_edit = list_call[1]
        id_ship = list_call[2]

        if val_edit == 'дата':
            val = '«Дата»'
        elif val_edit == 'время':
            val = '«Время»'
        elif val_edit == 'количество':
            val = '«Количество»'
        elif val_edit == 'вес':
            val = '«Вес»'
        elif val_edit == 'адресз':
            val = '«Адрес загрузки»'
        elif val_edit == 'адреср':
            val = '«Адрес разгрузки»'
        elif val_edit == 'коммент':
            val = '«Комментарий»'
        else:
            val = 'Не указано'

        l = selist(f"SELECT * FROM shipping WHERE id_ship = '{id_ship}'", user)[0]

        inline_m = InlineKeyboardMarkup(row_width=2)
        inline_m_b8 = InlineKeyboardButton(text='⬅️ Назад', callback_data=f'logisedit_{l["id_ship"]}')
        inline_m.add(inline_m_b8)


        await callback.message.edit_text(text=f'ID: *{l["id_ship"]}*\n'
                                  f'Тип: *{l["type_ship"]}*\n'
                                  f'Дата: *{l["date_ship"]}*\n'
                                  f'Время: *{l["time_ship"]}*\n'
                                  f'Предмет: *{l["item_ship"]}*\n'
                                  f'Количество: *{l["count_item_ship"]}*\n'
                                  f'Вес: *{l["w_ship"]}*\n\n'
                                  f'Адрес загрузки: `{l["adress_begin"]}`\n'
                                  f'Адрес разгрузки: `{l["adress_end"]}`\n'
                                  f'Комментарий: *{l["comment_ship"]}*', parse_mode='Markdown', reply_markup=inline_m)
        await callback.message.answer(text=f'Введите новое значение параметра {val}')

        await callback.answer()
    elif 'edite_' in callback.data:
        id_ship = callback.data.split('_')[1]
        new_res = 'edite_' + id_ship
        update(f"UPDATE users SET act_log = '{new_res}' WHERE id_user = '{user}'", user)
        await callback.message.edit_text(text='Введите новую дату в формате 21.12.2012:')
        await callback.answer()

    elif 'notif_' in callback.data:
        num_notif = callback.data.split('_')[1]

        old_list_users = selone(f"SELECT notif FROM users WHERE id_user = '{user}'", user)['notif']
        list_users = old_list_users.split(' ')

        if int(num_notif) == 1:
            if 'skaz' in old_list_users:
                for i in range(len(list_users)):
                    if list_users[i] == 'skaz':
                        del list_users[i]
                        break
            else:
                list_users.append('skaz')

        elif int(num_notif) == 2:
            if 'log' in old_list_users:
                for i in range(len(list_users)):
                    if list_users[i] == 'log':
                        del list_users[i]
                        break
            else:
                list_users.append('log')

        elif int(num_notif) == 3:
            if 'client' in old_list_users:
                for i in range(len(list_users)):
                    if list_users[i] == 'client':
                        del list_users[i]
                        break
            else:
                list_users.append('client')

        elif int(num_notif) == 4:
            if 'fbs' in old_list_users:
                for i in range(len(list_users)):
                    if list_users[i] == 'fbs':
                        del list_users[i]
                        break
            else:
                list_users.append('fbs')

        elif int(num_notif) == 5:
            if 'fbo' in old_list_users:
                for i in range(len(list_users)):
                    if list_users[i] == 'fbo':
                        del list_users[i]
                        break
            else:
                list_users.append('fbo')

        elif int(num_notif) == 6:
            if 'ypak' in old_list_users:
                for i in range(len(list_users)):
                    if list_users[i] == 'ypak':
                        del list_users[i]
                        break
            else:
                list_users.append('ypak')

        elif int(num_notif) == 7:
            if 'wood' in old_list_users:
                for i in range(len(list_users)):
                    if list_users[i] == 'wood':
                        del list_users[i]
                        break
            else:
                list_users.append('wood')

        elif int(num_notif) == 8:
            if 'admin' in old_list_users:
                for i in range(len(list_users)):
                    if list_users[i] == 'admin':
                        del list_users[i]
                        break
            else:
                list_users.append('admin')

        elif int(num_notif) == 9:
            if 'men' in old_list_users:
                for i in range(len(list_users)):
                    if list_users[i] == 'men':
                        del list_users[i]
                        break
            else:
                list_users.append('men')


        new_list = " ".join(list_users)
        update(f"UPDATE users SET notif = '{new_list}' WHERE id_user = '{user}'", user)


        list_user = selone(f"SELECT notif FROM users WHERE id_user = '{user}'", user)['notif']

        mes1 = 'Цех ❌'
        mes2 = 'Логистика ❌'
        mes3 = 'Клиентский ФФ ❌'
        mes4 = 'FBS ❌'
        mes5 = 'FBO ❌'
        mes6 = 'Склад упаковки ❌'
        mes7 = 'Склад цеха ❌'
        mes8 = 'Важные ❌'
        mes9 = 'Менеджмент ❌'

        if 'skaz' in list_user:
            mes1 = 'Цех ✅'

        if 'log' in list_user:
            mes2 = 'Логистика ✅'

        if 'client' in list_user:
            mes3 = 'Клиентский ФФ ✅'

        if 'fbs' in list_user:
            mes4 = 'FBS ✅'

        if 'fbo' in list_user:
            mes5 = 'FBO ✅'

        if 'ypak' in list_user:
            mes6 = 'Склад упаковки ✅'

        if 'wood' in list_user:
            mes7 = 'Склад цеха ✅'

        if 'admin' in list_user:
            mes8 = 'Важные ✅'

        if 'men' in list_user:
            mes9 = 'Менеджмент ✅'

        inline_notif = InlineKeyboardMarkup(row_width=1)
        inline_notif_b1 = InlineKeyboardButton(text=mes1, callback_data='notif_1')
        inline_notif_b2 = InlineKeyboardButton(text=mes2, callback_data='notif_2')
        inline_notif_b3 = InlineKeyboardButton(text=mes3, callback_data='notif_3')
        inline_notif_b4 = InlineKeyboardButton(text=mes4, callback_data='notif_4')
        inline_notif_b5 = InlineKeyboardButton(text=mes5, callback_data='notif_5')
        inline_notif_b6 = InlineKeyboardButton(text=mes6, callback_data='notif_6')
        inline_notif_b7 = InlineKeyboardButton(text=mes7, callback_data='notif_7')
        inline_notif_b8 = InlineKeyboardButton(text=mes8, callback_data='notif_8')
        inline_notif_b9 = InlineKeyboardButton(text=mes9, callback_data='notif_9')
        inline_notif.add(inline_notif_b8).add(inline_notif_b1).add(inline_notif_b2).add(inline_notif_b3).add(
            inline_notif_b4).add(inline_notif_b5).add(inline_notif_b6).add(inline_notif_b7).add(inline_notif_b9)

        await callback.message.edit_text(text='Настройки уведомлений', reply_markup=inline_notif)
        await callback.answer()

    # Реквизиты
    elif 'reqv_' in callback.data:
        id_user = callback.data.split('_')[1]

        list_values = selist(f"SELECT name_user, sbp_num, card_num FROM users WHERE id_user = '{id_user}'", user)[0]


        name_user = list_values['name_user']
        sbp_num = list_values['sbp_num'][:11]
        sbp_name = list_values['sbp_num'][11:]
        card_num = list_values['card_num']

        await callback.message.edit_text(text=f'Сотрудник: *{name_user}*\n\nСБП: `{sbp_num}`*{sbp_name}*\n\nНомер карты: `{card_num}`', parse_mode='Markdown')
        await callback.answer()

    # Отправки
    elif 'upnaqr_' in callback.data:
        id_sup = callback.data.split('_')[1]
        update(f"UPDATE wood SET status_ship = 'Обработано, ждет отправки' WHERE id_sup = '{id_sup}'", user)
        await callback.message.edit_text(text=f'Не забудьте утром загрузить в машину!')
        await callback.answer()
    elif 'otprav_' in callback.data:
        id_sup = callback.data.split('_')[1]
        update(f"UPDATE wood SET status_ship = 'Отправлено' WHERE id_sup = '{id_sup}'", user)

        chat_id = selone(f"SELECT id_work FROM wood WHERE id_sup = '{id_sup}'", user)['id_work']

        destination_bot = Bot(token='6629342340:AAG_DI1HQprpkkA5Ruwfd3E6kLO4tmdbXfw')
        await destination_bot.send_message(chat_id, f'✅ Детали запроса с *ID {id_sup} отправлены клиенту*', parse_mode='Markdown')

        await callback.message.edit_text(text=f'Запрос выполнен!')
        await callback.answer()
    elif 'sync_' in callback.data:
        type_sync = callback.data.split('_')[1]
        await callback.answer()
        if type_sync == 'ras':
            await callback.message.edit_text(text='Синхронизация...\n🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥')

            # обновляем контрагентов
            worksheet = sh.worksheet('Расход Контрагенты')

            await callback.message.edit_text(text='Синхронизация...\n🟩🟥🟥🟥🟥🟥🟥🟥🟥🟥')

            # контрагенты аренда
            list_value_arenda = worksheet.col_values(2)
            list_items_arenda = []

            for val in list_value_arenda:
                if len(val) == 0 or val == 'Аренда':
                    pass
                else:
                    list_items_arenda.append(val)

            items_arenda = '&'.join(list_items_arenda)

            # контрагенты фот
            list_value_fot = worksheet.col_values(3)
            list_items_fot = []

            for val in list_value_fot:
                if len(val) == 0 or val == 'ФОТ':
                    pass
                else:
                    list_items_fot.append(val)

            items_fot = '&'.join(list_items_fot)

            await callback.message.edit_text(text='Синхронизация...\n🟩🟩🟥🟥🟥🟥🟥🟥🟥🟥')

            # контрагенты Расходники
            list_value_rashod = worksheet.col_values(4)
            list_items_rashod = []

            for val in list_value_rashod:
                if len(val) == 0 or val == 'Расходники':
                    pass
                else:
                    list_items_rashod.append(val)

            items_rashod = '&'.join(list_items_rashod)

            # контрагенты Инструменты
            list_value_instr = worksheet.col_values(5)
            list_items_instr = []

            for val in list_value_instr:
                if len(val) == 0 or val == 'Инструменты':
                    pass
                else:
                    list_items_instr.append(val)

            items_instr = '&'.join(list_items_instr)

            await callback.message.edit_text(text='Синхронизация...\n🟩🟩🟩🟥🟥🟥🟥🟥🟥🟥')

            # контрагенты Логистика
            list_value_log = worksheet.col_values(6)
            list_items_log = []

            for val in list_value_log:
                if len(val) == 0 or val == 'Логистика':
                    pass
                else:
                    list_items_log.append(val)

            items_log = '&'.join(list_items_log)

            # контрагенты Прочее
            list_value_proch = worksheet.col_values(7)
            list_items_proch = []

            for val in list_value_proch:
                if len(val) == 0 or val == 'Прочее':
                    pass
                else:
                    list_items_proch.append(val)

            items_proch = '&'.join(list_items_proch)

            await callback.message.edit_text(text='Синхронизация...\n🟩🟩🟩🟩🟥🟥🟥🟥🟥🟥')

            # контрагенты Аутсорс
            list_value_auts = worksheet.col_values(8)
            list_items_auts = []

            for val in list_value_auts:
                if len(val) == 0 or val == 'Аутсорс':
                    pass
                else:
                    list_items_auts.append(val)

            items_auts = '&'.join(list_items_auts)

            create(f"REPLACE INTO ras(type_col, arenda, fot, rashod, instr, log, proch, auts) VALUES ('kontr', '{items_arenda}', '{items_fot}', '{items_rashod}', '{items_instr}', '{items_log}', '{items_proch}', '{items_auts}')", user)

            await callback.message.edit_text(text='Синхронизация...\n🟩🟩🟩🟩🟩🟥🟥🟥🟥🟥')

            # обновляем предметы
            worksheet_2 = sh.worksheet('Расход Предметы')

            await callback.message.edit_text(text='Синхронизация...\n🟩🟩🟩🟩🟩🟩🟥🟥🟥🟥')

            # предметы аренда
            list_value_arenda = worksheet_2.col_values(2)
            list_items_arenda = []

            for val in list_value_arenda:
                if len(val) == 0 or val == 'Аренда':
                    pass
                else:
                    list_items_arenda.append(val)

            items_arenda = '&'.join(list_items_arenda)

            # предметы фот
            list_value_fot = worksheet_2.col_values(3)
            list_items_fot = []

            for val in list_value_fot:
                if len(val) == 0 or val == 'ФОТ':
                    pass
                else:
                    list_items_fot.append(val)

            items_fot = '&'.join(list_items_fot)

            await callback.message.edit_text(text='Синхронизация...\n🟩🟩🟩🟩🟩🟩🟩🟥🟥🟥')

            # предметы Расходники
            list_value_rashod = worksheet_2.col_values(4)
            list_items_rashod = []

            for val in list_value_rashod:
                if len(val) == 0 or val == 'Расходники':
                    pass
                else:
                    list_items_rashod.append(val)

            items_rashod = '&'.join(list_items_rashod)

            # предметы Инструменты
            list_value_instr = worksheet_2.col_values(5)
            list_items_instr = []

            for val in list_value_instr:
                if len(val) == 0 or val == 'Инструменты':
                    pass
                else:
                    list_items_instr.append(val)

            items_instr = '&'.join(list_items_instr)

            await callback.message.edit_text(text='Синхронизация...\n🟩🟩🟩🟩🟩🟩🟩🟩🟥🟥')

            # предметы Логистика
            list_value_log = worksheet_2.col_values(6)
            list_items_log = []

            for val in list_value_log:
                if len(val) == 0 or val == 'Логистика':
                    pass
                else:
                    list_items_log.append(val)

            items_log = '&'.join(list_items_log)

            # предметы Прочее
            list_value_proch = worksheet_2.col_values(7)
            list_items_proch = []

            for val in list_value_proch:
                if len(val) == 0 or val == 'Прочее':
                    pass
                else:
                    list_items_proch.append(val)

            items_proch = '&'.join(list_items_proch)

            await callback.message.edit_text(text='Синхронизация...\n🟩🟩🟩🟩🟩🟩🟩🟩🟩🟥')

            # предметы Аутсорс
            list_value_auts = worksheet_2.col_values(8)
            list_items_auts = []

            for val in list_value_auts:
                if len(val) == 0 or val == 'Аутсорс':
                    pass
                else:
                    list_items_auts.append(val)

            items_auts = '&'.join(list_items_auts)

            create(f"REPLACE INTO ras(type_col, arenda, fot, rashod, instr, log, proch, auts) VALUES ('pred', '{items_arenda}', '{items_fot}', '{items_rashod}', '{items_instr}', '{items_log}', '{items_proch}', '{items_auts}')", user)


            await callback.message.edit_text(text='✅ Синхронизация успешна!')
        elif type_sync == 'req':
            # обновляем реквизиты
            await callback.message.edit_text(text='Синхронизация...\n🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥')
            worksheet_2 = sh.worksheet('Сотрудники')
            await callback.message.edit_text(text='Синхронизация...\n🟩🟩🟩🟥🟥🟥🟥🟥🟥🟥')
            list_value_id = worksheet_2.col_values(3)
            await callback.message.edit_text(text='Синхронизация...\n🟩🟩🟩🟩🟩🟥🟥🟥🟥🟥')
            list_value_sbp = worksheet_2.col_values(4)
            await callback.message.edit_text(text='Синхронизация...\n🟩🟩🟩🟩🟩🟩🟩🟥🟥🟥')
            list_value_card = worksheet_2.col_values(5)
            await callback.message.edit_text(text='Синхронизация...\n🟩🟩🟩🟩🟩🟩🟩🟩🟩🟥')

            for i in range(len(list_value_id)):
                if len(list_value_id[i]) == 0 or i == 0 or selone(f"SELECT id_user FROM users WHERE id_user = '{list_value_id[i]}'", user) is None:
                    pass
                else:
                    update(f"UPDATE users SET sbp_num = '{list_value_sbp[i]}' WHERE id_user = '{list_value_id[i]}'", user)
                    update(f"UPDATE users SET card_num = '{list_value_card[i]}' WHERE id_user = '{list_value_id[i]}'", user)
            await callback.message.edit_text(text='✅ Синхронизация успешна!')
    elif 'crm' == callback.data.split('_')[0]:
        await callback.answer()
        inline_key = InlineKeyboardMarkup(row_width=1)
        inline_key_b1 = InlineKeyboardButton(text='...ждите...', callback_data='...')
        inline_key.add(inline_key_b1)
        await callback.message.edit_reply_markup(inline_key)

        type_crm = callback.data.split('_')[1]
        num_row = int(callback.data.split('_')[2]) + 1

        if type_crm == 'done':
            sh.worksheet('CRM').update(f'D{num_row}', 'Готово')
            await callback.message.edit_text(text=f'✅ Задача выполнена!')
        elif type_crm == 'prin':
            values_list = sh.worksheet('CRM').row_values(num_row)
            sh.worksheet('CRM').update(f'D{num_row}', 'В процессе')

            inline_key=InlineKeyboardMarkup(row_width=1)
            inline_key_b1 = InlineKeyboardButton(text='✅ Закончить ✅', callback_data=f'crm_done_{num_row - 1}')
            inline_key.add(inline_key_b1)
            await callback.message.edit_text(text=f'Задача с номером <b>{num_row}</b>:\n'
                                                  f'<b>{values_list[1]}</b>\n\n'
                                                  f'Дедлайн: <b>{values_list[2]}</b>\n'
                                                  f'Статус: <b>🛠 В процессе</b>', reply_markup=inline_key)
    elif 'zd' == callback.data.split('_')[0]:
        await callback.answer()
        if callback.data.split('_')[1] == 'korrast':
            update(f"UPDATE users SET act_sk = 'zd_korrast_' WHERE id_user = '{user}'", user)
            await callback.message.edit_text(text=f'Сколько коробок для растущих?')
        elif callback.data.split('_')[1] == 'raz1rast':
            update(f"UPDATE users SET act_sk = 'zd_raz1rast_' WHERE id_user = '{user}'", user)
            await callback.message.edit_text(text=f'Сколько раздаток 1 для растущих?')
        elif callback.data.split('_')[1] == 'raz2rast':
            update(f"UPDATE users SET act_sk = 'zd_raz2rast_' WHERE id_user = '{user}'", user)
            await callback.message.edit_text(text=f'Сколько раздаток 2 для растущих?')
        elif callback.data.split('_')[1] == 'furrast':
            update(f"UPDATE users SET act_sk = 'zd_furrast_' WHERE id_user = '{user}'", user)
            await callback.message.edit_text(text=f'Сколько фурнитур для растущих?')
    elif callback.data == '...':
        await callback.answer()



@db.message_handler()
async def send_text(message: types.Message):
    user = message.chat.id

    list_ff = selist(f"SELECT * FROM warehouse_ff WHERE min_count <> -1", user)
    for item in list_ff:
        if item['count_item'] < item['min_count']:
            delta_1 = datetime.timedelta(hours=5)
            now = datetime.datetime.now() + delta_1
            if int(now.day) < 10:
                day_edit = '0' + str(now.day)
            else:
                day_edit = now.day

            if int(now.month) < 10:
                month_edit = '0' + str(now.month)
            else:
                month_edit = now.month
            date_create = f'{day_edit}.{month_edit}.{now.year}'
            if item['date_say'] != date_create:
                name_item = item['name_item']
                update(f"UPDATE warehouse_ff SET date_say = '{date_create}' WHERE name_item = '{name_item}'", user)
                list_all_users = selist(f"SELECT * FROM users", user)
                list_user = []
                for us in list_all_users:
                    if 'ypak' in us['notif']:
                        list_user.append(us)

                for user1 in list_user:
                    try:
                        chat_id = str(user1["id_user"])
                        await bot.send_message(chat_id, text=f'🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦\n\n'
                                                             f'Критическое количество позиции <b>{item["name_item"]}</b> на Упаковке: <b>{item["count_item"]}</b>\n\n'
                                                             f'Должно быть не менее <b>{item["min_count"]}</b>\n\n'
                                                             f'🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦')
                    except:
                        pass

    list_c = selist(f"SELECT * FROM warehouse_c WHERE min_count <> -1", user)
    for item in list_c:
        if item['count_item'] < 0 and selone(f"SELECT count_retail FROM users WHERE id_user = '{user}'", user)['count_retail'] == 2:
            list_all_users = selist(f"SELECT * FROM users", user)
            list_user = []
            for us in list_all_users:
                if 'wood' in us['notif']:
                    list_user.append(us)

            for user1 in list_user:
                try:
                    chat_id = str(user1["id_user"])
                    await bot.send_message(chat_id, text=f'🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧\n\n'
                                                         f'Отрицательное количество позиции <b>{item["name_item"]}</b> в цеху!\n'
                                                         f'Единица измерения: <b>{item["ed"]}</b>\n\n'
                                                         f'<b>НЕОБХОДИМО СДЕЛАТЬ ПЕРЕСЧЕТ!</b>\n\n'
                                                         f'🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧')
                except:
                    pass
        elif item['count_item'] < item['min_count']:
            delta_1 = datetime.timedelta(hours=5)
            now = datetime.datetime.now() + delta_1
            if int(now.day) < 10:
                day_edit = '0' + str(now.day)
            else:
                day_edit = now.day

            if int(now.month) < 10:
                month_edit = '0' + str(now.month)
            else:
                month_edit = now.month
            date_create = f'{day_edit}.{month_edit}.{now.year}'
            if item['date_say'] != date_create:
                name_item = item['name_item']
                update(f"UPDATE warehouse_c SET date_say = '{date_create}' WHERE name_item = '{name_item}'", user)
                list_all_users = selist(f"SELECT * FROM users", user)
                list_user = []
                for us in list_all_users:
                    if 'wood' in us['notif']:
                        list_user.append(us)

                for user1 in list_user:
                    try:
                        chat_id = str(user1["id_user"])
                        await bot.send_message(chat_id, text=f'🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥\n\n'
                                                             f'Критическое количество позиции <b>{item["name_item"]}</b> в цеху: <b>{item["count_item"]}</b>\n'
                                                             f'Единица измерения: <b>{item["ed"]}</b>\n\n'
                                                             f'Должно быть не менее <b>{item["min_count"]}</b>\n\n'
                                                             f'🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥')
                    except:
                        pass

    datework = str(datetime.datetime.now())[:10]

    delta_1 = datetime.timedelta(hours=5)
    now = datetime.datetime.now() + delta_1
    if selone(f"SELECT count_retail FROM users WHERE id_user = 395784406", user)['count_retail'] == 2:
        if int(now.hour) >= 22:
            list_all_users = selist(f"SELECT * FROM users", user)
            list_user = []
            for us in list_all_users:
                if 'skaz' in us['notif']:
                    list_user.append(us)

            for user1 in list_user:
                try:
                    chat_id = str(user1["id_user"])
                    destination_bot = Bot(token='6682205213:AAFFV1avM8cVCZhgv-K8pzKeJ_c20Wle_P4')
                    await destination_bot.send_message(chat_id, '🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥'
                                                                '\nСмена в Цеху не закрыта! Закрой смену!'
                                                                '\n🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥')
                except:
                    pass

    delta_1 = datetime.timedelta(hours=5)
    now = datetime.datetime.now() + delta_1
    if selone(f"SELECT driver FROM users WHERE id_user = 395784406", user)['driver'] == 2:
        if int(now.hour) >= 21:
            list_all_users = selist(f"SELECT * FROM users", user)
            list_user = []
            for us in list_all_users:
                if 'log' in us['notif']:
                    list_user.append(us)

            for user1 in list_user:
                try:
                    chat_id = str(user1["id_user"])
                    destination_bot = Bot(token='6490496152:AAHnBwfDRlUTyTFMOMGGCK6Eu3WejYpesIE')
                    await destination_bot.send_message(chat_id, '🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩'
                                                                '\nСмена логистики не закрыта! Закрой смену!'
                                                                '\n🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩')
                except:
                    pass

    if user == -1001933713976 or user == -984607796 or user == -1002146643966:
        pass

    elif selone(f"SELECT id_user FROM users WHERE id_user = '{user}'", user) is None:
        await message.answer(text=texts.start_text)

    else:
        if '*' in message.text or '_' in message.text:
            await message.answer(text='Сообщения не должно содержать * или _')

        else:
            # Главное меню
            if message.text == markups.menu_main:
                defaul_values(user)
                await message.answer(text=texts.menu_name, reply_markup=markups.menu_admin)

            # Отмена главное
            elif message.text == markups.menu_back_main:
                defaul_values(user)
                await message.answer(text=texts.menu_name, reply_markup=markups.menu_admin)

            # Меню Мебель
            elif message.text == markups.menu_admin_b2:
                if selone(f"SELECT company FROM users WHERE id_user = '{user}'", user)['company'] == 'Босс':
                    await message.answer(text=texts.menu_retail, reply_markup=markups.menu_retail)
                else:
                    await message.answer(text='У вас нет доступа!')

            # Меню Настройки
            elif message.text == markups.menu_admin_b5:
                if selone(f"SELECT company FROM users WHERE id_user = '{user}'", user)['company'] == 'Босс':
                    await message.answer(text='Меню настроек', reply_markup=markups.menu_set_admin)
                else:
                    await message.answer(text='У вас нет доступа!')

            # Обновить базу данных
            elif message.text == markups.menu_set_admin_b2:
                inline_key = InlineKeyboardMarkup(row_width=1)
                inline_key_b1 = InlineKeyboardButton(text='Расход', callback_data=f'sync_ras')
                inline_key_b2 = InlineKeyboardButton(text='Реквизиты', callback_data=f'sync_req')
                inline_key.add(inline_key_b1).add(inline_key_b2)
                await message.answer(text='Выберите категорию:', reply_markup=inline_key)

            # Уведомления
            elif message.text == markups.menu_set_admin_b1:
                list_user = selone(f"SELECT notif FROM users WHERE id_user = '{user}'", user)['notif']

                mes1 = 'Цех ❌'
                mes2 = 'Логистика ❌'
                mes3 = 'Клиентский ФФ ❌'
                mes4 = 'FBS ❌'
                mes5 = 'FBO ❌'
                mes6 = 'Склад упаковки ❌'
                mes7 = 'Склад цеха ❌'
                mes8 = 'Важные ❌'
                mes9 = 'Менеджмент ❌'


                if 'skaz' in list_user:
                    mes1 = 'Цех ✅'

                if 'log' in list_user:
                    mes2 = 'Логистика ✅'

                if 'client' in list_user:
                    mes3 = 'Клиентский ФФ ✅'

                if 'fbs' in list_user:
                    mes4 = 'FBS ✅'

                if 'fbo' in list_user:
                    mes5 = 'FBO ✅'

                if 'ypak' in list_user:
                    mes6 = 'Склад упаковки ✅'

                if 'wood' in list_user:
                    mes7 = 'Склад цеха ✅'

                if 'admin' in list_user:
                    mes8 = 'Важные ✅'

                if 'men' in list_user:
                    mes9 = 'Менеджмент ✅'

                inline_notif = InlineKeyboardMarkup(row_width=1)
                inline_notif_b1 = InlineKeyboardButton(text=mes1, callback_data='notif_1')
                inline_notif_b2 = InlineKeyboardButton(text=mes2, callback_data='notif_2')
                inline_notif_b3 = InlineKeyboardButton(text=mes3, callback_data='notif_3')
                inline_notif_b4 = InlineKeyboardButton(text=mes4, callback_data='notif_4')
                inline_notif_b5 = InlineKeyboardButton(text=mes5, callback_data='notif_5')
                inline_notif_b6 = InlineKeyboardButton(text=mes6, callback_data='notif_6')
                inline_notif_b7 = InlineKeyboardButton(text=mes7, callback_data='notif_7')
                inline_notif_b8 = InlineKeyboardButton(text=mes8, callback_data='notif_8')
                inline_notif_b9 = InlineKeyboardButton(text=mes9, callback_data='notif_9')
                inline_notif.add(inline_notif_b8).add(inline_notif_b1).add(inline_notif_b2).add(inline_notif_b3).add(inline_notif_b4).add(inline_notif_b5).add(inline_notif_b6).add(inline_notif_b7).add(inline_notif_b9)

                await message.answer(text='Настройки уведомлений', reply_markup=inline_notif)
                await message.answer(text=f'Для возврата нажмите {markups.menu_back_set}', reply_markup=markups.back_set)

            # Отмена Мебель
            elif message.text == markups.menu_back_set:
                defaul_values(user)
                await message.answer(text='Меню настроек', reply_markup=markups.menu_set_admin)

            # Отмена Мебель
            elif message.text == markups.menu_back_retail:
                defaul_values(user)
                if selone(f"SELECT company FROM users WHERE id_user = '{user}'", user)['company'] == 'Босс':
                    await message.answer(text=texts.menu_retail, reply_markup=markups.menu_retail)
                else:
                    await message.answer(text='У вас нет доступа!')

            # Подтвердить расход
            elif message.text == markups.menu_retail_b8:
                delta_1 = datetime.timedelta(hours=5)
                now = datetime.datetime.now() + delta_1
                inline_main = InlineKeyboardMarkup(row_width=1)
                await message.answer(f'Минуточку...')
                check = 0

                for i in range(2023, int(now.year) + 1):
                    try:
                        num_row = 1
                        worksheet = sh.worksheet(f"Расход {i}")
                        values_list = worksheet.col_values(2)
                        pay_list = worksheet.col_values(10)
                        inline_main = InlineKeyboardMarkup(row_width=1)
                        for value in range(1, len(values_list)):
                            if pay_list[value] == 'Не оплачено':
                                check = 1
                                name_value = ' «' + worksheet.row_values(num_row + 1)[2] + '» ' + worksheet.row_values(num_row + 1)[3] + \
                                             ' — ' + worksheet.row_values(num_row + 1)[7]

                                inline_main_b = InlineKeyboardButton(text=name_value, callback_data=f'rshod_{num_row + 1}_{i}')
                                inline_main.add(inline_main_b)
                            num_row += 1
                    except Exception as error:
                        await message.answer(error)

                if check == 1:
                    await message.answer(f'Что оплачено?', reply_markup=inline_main)
                    await message.answer(f'Дл возврата нажмите Отмена', reply_markup=markups.back_retail)
                else:
                    await message.answer('Неоплаченных счетов нет!')

            # Сменить план
            elif message.text == markups.menu_retail_b4:
                res = 'plan'
                update(f"UPDATE users SET act_log = '{res}' WHERE id_user = '{user}'", user)
                inline_date = ReplyKeyboardMarkup(resize_keyboard=True)
                inline_date_b0 = f'{sk.date_yes_create()}'
                inline_date_b1 = f'{sk.date_create()}'
                inline_date_b2 = f'{sk.date_tomorrow_create()}'
                menu_back = 'Отмена 🛑'
                inline_date.add(inline_date_b0, inline_date_b1, inline_date_b2).add(menu_back)
                await message.answer(text='Введите дату когда нужно сменить план <i>(в формате 01.11.2023)</i>', reply_markup=inline_date)
            elif selone(f"SELECT act_log FROM users WHERE id_user = '{user}'", user)['act_log'] == 'plan':
                if len(message.text) == 10 and len(message.text.split('.')) == 3 and message.text.split('.')[0].isdigit() and message.text.split('.')[1].isdigit() and message.text.split('.')[2].isdigit():
                    try:
                        await message.answer(text=f'Минуточку...', reply_markup=markups.back_retail)
                        daynow = message.text.split('.')[0]
                        monthnow = message.text.split('.')[1]
                        yearnow = message.text.split('.')[2]

                        if now.month == 1:
                            name_list = f"График Январь {now.year}"
                        elif now.month == 2:
                            name_list = f"График Февраль {now.year}"
                        elif now.month == 3:
                            name_list = f"График Март {now.year}"
                        elif now.month == 4:
                            name_list = f"График Апрель {now.year}"
                        elif now.month == 5:
                            name_list = f"График Май {now.year}"
                        elif now.month == 6:
                            name_list = f"График Июнь {now.year}"
                        elif now.month == 7:
                            name_list = f"График Июль {now.year}"
                        elif now.month == 8:
                            name_list = f"График Август {now.year}"
                        elif now.month == 9:
                            name_list = f"График Сентябрь {now.year}"
                        elif now.month == 10:
                            name_list = f"График Октябрь {now.year}"
                        elif now.month == 11:
                            name_list = f"График Ноябрь {now.year}"
                        elif now.month == 12:
                            name_list = f"График Декабрь {now.year}"

                        worksheet_2 = sh.worksheet(name_list)
                        num_row = int(daynow) + 1
                        cel = f'A{num_row}'
                        plan = worksheet_2.acell(cel).value

                        res = f'planznach_{message.text}'
                        update(f"UPDATE users SET act_log = '{res}' WHERE id_user = '{user}'", user)

                        await message.answer(text=f'В этот день план стоит <b>{plan} шт.</b>')
                        await message.answer(text=f'Введите новое значение:')

                    except Exception as ex:
                        await message.answer(text=f'Ошибка {ex}! Нажмите отмена и повторите действие.', reply_markup=markups.back_retail)
                else:
                    await message.answer(text='Введите дату в формате 01.11.2023!')
            elif selone(f"SELECT act_log FROM users WHERE id_user = '{user}'", user)['act_log'].split('_')[0] == 'planznach':
                if message.text.isdigit():
                    try:
                        await message.answer(text=f'Минуточку...', reply_markup=markups.back_retail)
                        daynow = selone(f"SELECT act_log FROM users WHERE id_user = '{user}'", user)['act_log'].split('_')[1].split('.')[0]
                        monthnow = selone(f"SELECT act_log FROM users WHERE id_user = '{user}'", user)['act_log'].split('_')[1].split('.')[1]
                        yearnow = selone(f"SELECT act_log FROM users WHERE id_user = '{user}'", user)['act_log'].split('_')[1].split('.')[2]

                        if now.month == 1:
                            name_list = f"График Январь {now.year}"
                        elif now.month == 2:
                            name_list = f"График Февраль {now.year}"
                        elif now.month == 3:
                            name_list = f"График Март {now.year}"
                        elif now.month == 4:
                            name_list = f"График Апрель {now.year}"
                        elif now.month == 5:
                            name_list = f"График Май {now.year}"
                        elif now.month == 6:
                            name_list = f"График Июнь {now.year}"
                        elif now.month == 7:
                            name_list = f"График Июль {now.year}"
                        elif now.month == 8:
                            name_list = f"График Август {now.year}"
                        elif now.month == 9:
                            name_list = f"График Сентябрь {now.year}"
                        elif now.month == 10:
                            name_list = f"График Октябрь {now.year}"
                        elif now.month == 11:
                            name_list = f"График Ноябрь {now.year}"
                        elif now.month == 12:
                            name_list = f"График Декабрь {now.year}"

                        worksheet_2 = sh.worksheet(name_list)
                        num_row = int(daynow) + 1
                        cel = f'A{num_row}'

                        plan = worksheet_2.update(cel, int(message.text))

                        update(f"UPDATE users SET act_log = ' ' WHERE id_user = '{user}'", user)

                        await message.answer(text=f'План изменен!', reply_markup=markups.menu_retail)

                    except Exception as ex:
                        await message.answer(text=f'Ошибка {ex}! Нажмите отмена и повторите действие.', reply_markup=markups.back_retail)
                else:
                    await message.answer(text='Введите число!')

            # Расход Мебель
            elif selone(f"SELECT act_retail FROM users WHERE id_user = '{user}'", user)['act_retail'] == 3:
                if message.text.isdigit():
                    update(f"UPDATE users SET word_6 = '{message.text}' WHERE id_user = '{user}'", user)
                    if selone(f"SELECT word_1 FROM users WHERE id_user = '{user}'", user)['word_1'] == 'Расходники':
                        update(f"UPDATE users SET act_retail = 0 WHERE id_user = '{user}'", user)
                        if selone(f"SELECT word_8 FROM users WHERE id_user = '{user}'", user)['word_8'] == "Оплачено":
                            await message.answer(text="С какого счета была оплата?", reply_markup=markups.inline_pay)
                        else:
                            await message.answer(text="Почти закончили)", reply_markup=markups.inline_pay_3)
                    if selone(f"SELECT word_1 FROM users WHERE id_user = '{user}'", user)['word_1'] == 'Аутсорс':
                        update(f"UPDATE users SET act_retail = 0 WHERE id_user = '{user}'", user)
                        if selone(f"SELECT word_8 FROM users WHERE id_user = '{user}'", user)['word_8'] == "Оплачено":
                            await message.answer(text="С какого счета была оплата?", reply_markup=markups.inline_pay)
                        else:
                            await message.answer(text="Почти закончили)", reply_markup=markups.inline_pay_3)
                else:
                    await message.answer(text="Введите количество числом:")
            elif selone(f"SELECT act_retail FROM users WHERE id_user = '{user}'", user)['act_retail'] == 2:
                update(f"UPDATE users SET word_5 = '{message.text}' WHERE id_user = '{user}'", user)
                if selone(f"SELECT word_1 FROM users WHERE id_user = '{user}'", user)['word_1'] == 'ФОТ':
                    update(f"UPDATE users SET act_retail = 0 WHERE id_user = '{user}'", user)
                    if selone(f"SELECT word_8 FROM users WHERE id_user = '{user}'", user)['word_8'] == "Оплачено":
                        await message.answer(text="С какого счета была оплата?", reply_markup=markups.inline_pay)
                    else:
                        await message.answer(text="Почти закончили)", reply_markup=markups.inline_pay_3)
                elif selone(f"SELECT word_1 FROM users WHERE id_user = '{user}'", user)['word_1'] == 'Инструменты':
                    update(f"UPDATE users SET act_retail = 0 WHERE id_user = '{user}'", user)
                    if selone(f"SELECT word_8 FROM users WHERE id_user = '{user}'", user)['word_8'] == "Оплачено":
                        await message.answer(text="С какого счета была оплата?", reply_markup=markups.inline_pay)
                    else:
                        await message.answer(text="Почти закончили)", reply_markup=markups.inline_pay_3)
                else:
                    update(f"UPDATE users SET act_retail = 0 WHERE id_user = '{user}'", user)
                    if selone(f"SELECT word_8 FROM users WHERE id_user = '{user}'", user)['word_8'] == "Оплачено":
                        await message.answer(text="С какого счета была оплата?", reply_markup=markups.inline_pay)
                    else:
                        await message.answer(text="Почти закончили)", reply_markup=markups.inline_pay_3)
            elif selone(f"SELECT act_retail FROM users WHERE id_user = '{user}'", user)['act_retail'] == 1:
                if message.text.isdigit() or "," in message.text:
                    update(f"UPDATE users SET word_4 = '{message.text}' WHERE id_user = '{user}'", user)
                    if selone(f"SELECT word_1 FROM users WHERE id_user = '{user}'", user)['word_1'] == 'Аренда':
                        update(f"UPDATE users SET word_5 = ' ' WHERE id_user = '{user}'", user)
                        update(f"UPDATE users SET word_6 = ' ' WHERE id_user = '{user}'", user)
                        update(f"UPDATE users SET act_retail = 0 WHERE id_user = '{user}'", user)
                        if selone(f"SELECT word_8 FROM users WHERE id_user = '{user}'", user)['word_8'] == "Оплачено":
                            await message.answer(text="С какого счета была оплата?", reply_markup=markups.inline_pay)
                        else:
                            await message.answer(text="Почти закончили)", reply_markup=markups.inline_pay_3)

                    elif selone(f"SELECT word_1 FROM users WHERE id_user = '{user}'", user)['word_1'] == 'ФОТ':
                        update(f"UPDATE users SET act_retail = 2 WHERE id_user = '{user}'", user)
                        update(f"UPDATE users SET word_6 = ' ' WHERE id_user = '{user}'", user)
                        await message.answer(text="Введите примечание:")
                    elif selone(f"SELECT word_1 FROM users WHERE id_user = '{user}'", user)['word_1'] == 'Расходники':
                        update(f"UPDATE users SET act_retail = 3 WHERE id_user = '{user}'", user)
                        update(f"UPDATE users SET word_5 = ' ' WHERE id_user = '{user}'", user)
                        await message.answer(text="Введите количество:")
                    elif selone(f"SELECT word_1 FROM users WHERE id_user = '{user}'", user)['word_1'] == 'Логистика':
                        update(f"UPDATE users SET act_retail = 2 WHERE id_user = '{user}'", user)
                        update(f"UPDATE users SET word_6 = ' ' WHERE id_user = '{user}'", user)
                        await message.answer(text="Введите примечание:")
                    elif selone(f"SELECT word_1 FROM users WHERE id_user = '{user}'", user)['word_1'] == 'Инструменты':
                        update(f"UPDATE users SET act_retail = 2 WHERE id_user = '{user}'", user)
                        update(f"UPDATE users SET word_6 = ' ' WHERE id_user = '{user}'", user)
                        await message.answer(text="Введите примечание:")
                    elif selone(f"SELECT word_1 FROM users WHERE id_user = '{user}'", user)['word_1'] == 'Прочее':
                        update(f"UPDATE users SET act_retail = 2 WHERE id_user = '{user}'", user)
                        update(f"UPDATE users SET word_6 = ' ' WHERE id_user = '{user}'", user)
                        await message.answer(text="Введите примечание:")
                    elif selone(f"SELECT word_1 FROM users WHERE id_user = '{user}'", user)['word_1'] == 'Аутсорс':
                        update(f"UPDATE users SET act_retail = 3 WHERE id_user = '{user}'", user)
                        update(f"UPDATE users SET word_5 = ' ' WHERE id_user = '{user}'", user)
                        await message.answer(text="Введите количество:")
                else:
                    await message.answer(f'Введите сумму числом!:')
            elif message.text == markups.menu_retail_b2:
                await message.answer(text='Оплачено?', reply_markup=markups.inline_done)
                await message.answer(text="Для возврата нажмите 'Отмена'", reply_markup=markups.back_retail)

            # Реквизиты
            elif message.text == markups.menu_retail_b3:
                inline_key = InlineKeyboardMarkup(row_width=1)
                list_values = selist(f"SELECT id_user, name_user, sbp_num, card_num FROM users", user)

                for val in list_values:
                    id_user = val['id_user']
                    if len(selone(f"SELECT sbp_num FROM users WHERE id_user = '{id_user}'", user)['sbp_num']) > 3:
                        name_user = val['name_user']
                        inline_key_b = InlineKeyboardButton(text=name_user, callback_data=f'reqv_{id_user}')
                        inline_key.add(inline_key_b)

                await message.answer(text='Выберите сотрудника:', reply_markup=inline_key)

            # CRM
            elif message.text == markups.menu_retail_b6:
                await message.answer(text='🔁 Подключаюсь к таблице...', reply_markup=markups.back_retail)
                worksheet = sh.worksheet('CRM')
                list_of_lists = worksheet.get_all_values()

                if user == 395784406:
                    name_user = 'Рома'
                elif user == 422836180:
                    name_user = 'Айнур К.'
                elif user == 279718355:
                    name_user = 'Айнур Х.'
                elif user == 1794088530:
                    name_user = 'Фархат'
                else:
                    name_user = ''

                if name_user != '':
                    check = 0
                    await message.answer(text='Список незаконченных задач:')
                    for l in range(len(list_of_lists)):
                        if list_of_lists[l][0] == name_user:
                            if list_of_lists[l][3] == 'Не начал':
                                inline_key = InlineKeyboardMarkup(row_width=1)
                                inline_key_b1 = InlineKeyboardButton(text='🛠 Начать задачу 🛠', callback_data=f'crm_prin_{l}')
                                inline_key.add(inline_key_b1)
                                check = 1
                                await message.answer(text=f'Задача с номером <b>{l + 1}</b>:\n'
                                                          f'<b>{list_of_lists[l][1]}</b>\n\n'
                                                          f'Дедлайн: <b>{list_of_lists[l][2]}</b>\n'
                                                          f'Статус: <b>⭕️ Не начал</b>', reply_markup=inline_key)
                            elif list_of_lists[l][3] == 'В процессе':
                                inline_key = InlineKeyboardMarkup(row_width=1)
                                inline_key_b1 = InlineKeyboardButton(text='✅ Закончить ✅', callback_data=f'crm_done_{l}')
                                inline_key.add(inline_key_b1)
                                check = 1
                                await message.answer(text=f'Задача с номером <b>{l + 1}</b>:\n'
                                                          f'<b>{list_of_lists[l][1]}</b>\n\n'
                                                          f'Дедлайн: <b>{list_of_lists[l][2]}</b>\n'
                                                          f'Статус: <b>🛠 В процессе</b>', reply_markup=inline_key)

                    if check == 0:
                        await message.answer(text='❌ Список пуст')
                else:
                    await message.answer(text='Вас нет в списке CRM')

            # Возвраты
            elif message.text == markups.menu_retail_b9:
                values_list = selist(f"SELECT * FROM warehouse_refunds", user)
                res = ''

                for val in values_list:
                    res += f'<b>{val["name_item"]}</b>: {val["count_item"]}\n'

                await message.answer(text=res)

            # Меню Склад
            elif message.text == markups.menu_main_count:
                if selone(f"SELECT company FROM users WHERE id_user = '{user}'", user)['company'] == 'Мастер' or selone(f"SELECT company FROM users WHERE id_user = '{user}'", user)['company'] == 'Босс':
                    await message.answer(text=texts.menu_count, reply_markup=markups.menu_count)
                else:
                    await message.answer(text='У вас нет доступа!')
            elif message.text == markups.menu_admin_b3:
                if selone(f"SELECT company FROM users WHERE id_user = '{user}'", user)['company'] == 'Мастер' or selone(f"SELECT company FROM users WHERE id_user = '{user}'", user)['company'] == 'Босс' or selone(f"SELECT company FROM users WHERE id_user = '{user}'", user)['company'] == 'Упаковка':
                    await message.answer(text=texts.menu_count, reply_markup=markups.menu_count)
                else:
                    await message.answer(text='У вас нет доступа!')

            # Отмена Склад
            elif message.text == markups.menu_back_count:
                defaul_values(user)
                await message.answer(text=texts.menu_retail, reply_markup=markups.menu_count)

            # Отмена Склад Мебель
            elif message.text == markups.menu_back_count_retail:
                defaul_values(user)
                await message.answer(text=texts.menu_count_retail, reply_markup=markups.menu_count)

            # Добавить сотрудника Склад
            elif selone(f"SELECT new_name_user FROM users WHERE id_user = '{user}'", user)['new_name_user'] == 3:
                update(f"UPDATE users SET new_name_user = 0 WHERE id_user = '{user}'", user)
                update(f"UPDATE users SET name_new_user = '{message.text}' WHERE id_user = '{user}'", user)
                await message.answer(text='Выберите должность сотрудника:', reply_markup=markups.inline_add_user_count)
            elif selone(f"SELECT new_id_user FROM users WHERE id_user = '{user}'", user)['new_id_user'] == 3:
                if message.text.isdigit():
                    update(f"UPDATE users SET new_id_user = 0 WHERE id_user = '{user}'", user)
                    update(f"UPDATE users SET new_id_user_text = '{message.text}' WHERE id_user = '{user}'", user)
                    update(f"UPDATE users SET new_name_user = 3 WHERE id_user = '{user}'", user)
                    await message.answer("Введите Фамилию и Имя сотрудника")
                else:
                    await message.answer(text='Пришлите <b>id</b> сотрудника числом:')
            elif message.text == markups.menu_count_b1:
                if selone(f"SELECT company FROM users WHERE id_user = '{user}'", user)['company'] == 'Босс':
                    update(f"UPDATE users SET new_id_user = 3 WHERE id_user = '{user}'", user)
                    await message.answer(
                        "Пришлите <b>id</b> сотрудника <i>(для того, чтобы узнать его, сотрудник должен написать боту команду /info)</i>", )
                    await message.answer(text="Для возврата нажмите 'Отмена'", reply_markup=markups.back_count)
                else:
                    await message.answer(text='У вас нет доступа!')

            # Написать сообщение сотрудникам цеха
            elif selone(f"SELECT act_wood FROM users WHERE id_user = '{user}'", user)['act_wood'] == 'mes':
                list_users = selist(f"SELECT id_user FROM users WHERE company = 'Сборщик' OR company = 'Мастер'", user)
                for user1 in list_users:
                    try:
                        chat_id = str(user1["id_user"])
                        destination_bot = Bot(token='6629342340:AAG_DI1HQprpkkA5Ruwfd3E6kLO4tmdbXfw')
                        await destination_bot.send_message(chat_id, message.text, parse_mode='HTML')
                    except:
                        pass
                await message.answer(
                    text='✅ Сообщение отправлено!\n\nВы можете еще ввести сообщение:\n\nДля выхода нажмите Отмена',
                    reply_markup=markups.back_count)
            elif message.text == markups.menu_count_b6:
                if selone(f"SELECT company FROM users WHERE id_user = '{user}'", user)['company'] == 'Босс':
                    update(f"UPDATE users SET act_wood = 'mes' WHERE id_user = '{user}'", user)
                    await message.answer("Напишите сообщение, которое хотите отправить сотрудникам:")
                    await message.answer(text="Для возврата нажмите 'Отмена'", reply_markup=markups.back_count)
                else:
                    await message.answer(text='У вас нет доступа!')

            # Удалить сотрудника Склад
            elif selone(f"SELECT remove_user FROM users WHERE id_user = '{user}'", user)['remove_user'] == 300:
                if message.text.isdigit():
                    check = 0
                    search = selist(f"SELECT id_user, name_user FROM users WHERE company = 'Мастер' OR company = 'Сборщик'", user)
                    for i in search:
                        if int(message.text) == int(i['id_user']):
                            check = 1
                    if check == 1:
                        update(f"UPDATE users SET remove_user = 0 WHERE id_user = '{user}'", user)
                        update(f"DELETE FROM users WHERE id_user = '{message.text}'", user)
                        await message.answer("Сотрудник удален")
                    else:
                        await message.answer(
                            text='Сотрудник с таким ID не найден!\nПришлите корректный <b>id</b> сотрудника:')
                else:
                    await message.answer(text='Пришлите <b>id</b> сотрудника числом:')
            elif message.text == markups.menu_count_b2:
                if selone(f"SELECT company FROM users WHERE id_user = '{user}'", user)['company'] == 'Босс':
                    update(f"UPDATE users SET remove_user = 300 WHERE id_user = '{user}'", user)
                    search = selist(
                        f"SELECT id_user, name_user, company FROM users WHERE company = 'Мастер' OR company = 'Сборщик'",
                        user)
                    res = ''
                    for i in search:
                        res += str(i['id_user']) + " - "
                        res += i['name_user'] + "\n"
                    await message.answer(res)
                    await message.answer('Введите ID сотрудника, которого хотите удалить')
                    await message.answer(text="Для возврата нажмите 'Отмена'", reply_markup=markups.back_count)
                else:
                    await message.answer(text='У вас нет доступа!')

            # Список сотрудников Склад
            elif message.text == markups.menu_count_b3:
                admins = selist(f"SELECT id_user, name_user, company FROM users WHERE company = 'Мастер' OR company = 'Сборщик'", user)
                res = ''
                for adm in admins:
                    name_user = adm['name_user']
                    res += str(adm['id_user']) + " - "
                    res += f"<b>{name_user}</b>" + f" <i>{adm['company']}</i>\n"

                await message.answer(res)

            # Меню Склад Мебель
            elif message.text == markups.menu_count_b5:
                if selone(f"SELECT company FROM users WHERE id_user = '{user}'", user)['company'] == 'Мастер':
                    if selone(f"SELECT count_retail FROM users WHERE id_user = '{user}'", user)['count_retail'] == 2:
                        await message.answer(text=texts.menu_count_retail, reply_markup=markups.menu_count_retail_n)
                    elif selone(f"SELECT count_retail FROM users WHERE id_user = '{user}'", user)['count_retail'] == 1:
                        await message.answer(text=texts.menu_count_retail, reply_markup=markups.menu_count_retail_b)
                elif selone(f"SELECT company FROM users WHERE id_user = '{user}'", user)['company'] == 'Босс':
                    if selone(f"SELECT count_retail FROM users WHERE id_user = '{user}'", user)['count_retail'] == 2:
                        await message.answer(text=texts.menu_count_retail, reply_markup=markups.menu_count_retail_n)
                    elif selone(f"SELECT count_retail FROM users WHERE id_user = '{user}'", user)['count_retail'] == 1:
                        await message.answer(text=texts.menu_count_retail, reply_markup=markups.menu_count_retail)
                else:
                    await message.answer(text='У вас нет доступа!')

            # Отмена Склад Мебель
            elif message.text == markups.menu_back_count_retail:
                defaul_values(user)
                if selone(f"SELECT company FROM users WHERE id_user = '{user}'", user)['company'] == 'Босс' or \
                        selone(f"SELECT company FROM users WHERE id_user = '{user}'", user)['company'] == 'Мастер':
                    if selone(f"SELECT count_retail FROM users WHERE id_user = '{user}'", user)['count_retail'] == 2:
                        await message.answer(text=texts.menu_count_retail, reply_markup=markups.menu_count_retail_n)
                    elif selone(f"SELECT count_retail FROM users WHERE id_user = '{user}'", user)['count_retail'] == 1:
                        await message.answer(text=texts.menu_count_retail, reply_markup=markups.menu_count_retail_b)
                else:
                    await message.answer(text='У вас нет доступа!')

            # Остаток Склад Мебель
            elif message.text == markups.menu_count_retail_b1:
                values_list = selist(f"SELECT * FROM warehouse_c WHERE min_count <> -1", user)
                res = ''

                for val in values_list:
                    if len(str(val["count_item"])) >= 2 and str(val["count_item"])[-2] == '1':
                        res += f'<b>{val["name_item"]}</b>: {val["count_item"]} {val["ed_2"]}\n'
                    elif str(val["count_item"])[-1] == '1':
                        res += f'<b>{val["name_item"]}</b>: {val["count_item"]} {val["ed"]}\n'
                    elif str(val["count_item"])[-1] == '2' or str(val["count_item"])[-1] == '3' or str(val["count_item"])[-1] == '4':
                        res += f'<b>{val["name_item"]}</b>: {val["count_item"]} {val["ed_1"]}\n'
                    else:
                        res += f'<b>{val["name_item"]}</b>: {val["count_item"]} {val["ed_2"]}\n'

                await message.answer(text=res)

                ldsp_per = selone(f"SELECT count_item FROM warehouse_c WHERE name_item = 'ЛДСП (перемычка)'", user)['count_item']
                ldsp_sid = selone(f"SELECT count_item FROM warehouse_c WHERE name_item = 'ЛДСП (сидушка)'", user)['count_item']
                ldsp_spin = selone(f"SELECT count_item FROM warehouse_c WHERE name_item = 'ЛДСП (спинка)'", user)['count_item']
                ldsp_stol = selone(f"SELECT count_item FROM warehouse_c WHERE name_item = 'ЛДСП (столешка)'", user)['count_item']

                max_item = max(ldsp_per, ldsp_sid, ldsp_spin, ldsp_stol)

                await message.answer(text=f'❗️ Для того, чтобы выровнять позиции ЛДСП, нужно сделать:\n\n'
                                          f'<i>Перемычка:</i> <b>{max_item - ldsp_per}</b>\n'
                                          f'<i>Сидушка:</i> <b>{max_item - ldsp_sid}</b>\n'
                                          f'<i>Спинка:</i> <b>{max_item - ldsp_spin}</b>\n'
                                          f'<i>Столешка:</i> <b>{max_item - ldsp_stol}</b>\n\n'
                                          f'📦 Будет комплектов: <b>{max_item}</b>')

            # Прибыло Склад Мебель
            elif message.text == markups.menu_count_retail_b2:
                name_objects = selist(f"SELECT name_item FROM warehouse_c WHERE min_count <> -1", user)
                inline_obj = InlineKeyboardMarkup(row_width=1)

                for o in name_objects:
                    inline_obj_b = InlineKeyboardButton(text=o["name_item"], callback_data=f'pribmeb_{o["name_item"]}')
                    inline_obj.add(inline_obj_b)

                await message.answer(text='Что прибыло?', reply_markup=inline_obj)
                await message.answer(text='Для возврата нажмите Отмена', reply_markup=markups.back_count)
            elif 'pribmeb' in selone(f"SELECT act_sk FROM users WHERE id_user = '{user}'", user)['act_sk']:
                if message.text.isdigit():
                    object_name = selone(f"SELECT act_sk FROM users WHERE id_user = '{user}'", user)['act_sk'].split('_')[1]
                    check_up = selone(f"SELECT act_sk FROM users WHERE id_user = '{user}'", user)['act_sk'].split('_')[2]
                    object_count = message.text
                    update(f"UPDATE users SET act_sk = ' ' WHERE id_user = '{user}'", user)

                    name_objects = selist(f"SELECT * FROM warehouse_c", user)
                    count_obj = selone(f"SELECT count_item FROM warehouse_c WHERE name_item = '{object_name}'", user)['count_item']

                    res_ost = 'Остаток на складе:\n'

                    if check_up == 'yes':
                        count_ff = selone(f"SELECT count_item FROM warehouse_ff WHERE name_item = '{object_name}'", user)['count_item']
                        update(f"UPDATE warehouse_ff SET count_item = '{int(count_ff) - int(object_count)}' WHERE name_item = '{object_name}'", user)

                    update(f"UPDATE warehouse_c SET count_item = '{int(count_obj) + int(object_count)}' WHERE name_item = '{object_name}'", user)
                    res_ost += f'<b>{object_name}</b>: {int(count_obj) + int(object_count)}\n'


                    if selone(f"SELECT count_retail FROM users WHERE id_user = '{user}'", user)['count_retail'] == 2:
                        await message.answer(text='Остатки по складу в Цеху изменены!',
                                             reply_markup=markups.menu_count_retail_n)
                    elif selone(f"SELECT count_retail FROM users WHERE id_user = '{user}'", user)['count_retail'] == 1:
                        await message.answer(text='Остатки по складу в Цеху изменены!',
                                             reply_markup=markups.menu_count_retail_b)

                    await message.answer(text=res_ost)

                else:
                    await message.answer(text='Введите количество числом!')

            # Отправки
            elif message.text == markups.menu_count_retail_b7:
                sup_list = selist(f"SELECT * FROM wood WHERE status_ship = 'Обрабатывается в цеху' OR status_ship = 'Обработано, ждет отправки'", user)

                if len(sup_list) > 0:
                    for sup in sup_list:
                        list_det = sup['list_det'].split(' ')
                        det = ''
                        for d in list_det:
                            if d == '1':
                                det += '\nНожка стула'
                            elif d == '2':
                                det += '\nНожка стола'
                            elif d == '3':
                                det += '\nСпинка стула'
                            elif d == '4':
                                det += '\nСидение стула'
                            elif d == '5':
                                det += '\nБоковая планка стула'
                            elif d == '6':
                                det += '\nПеремычка стола'
                            elif d == '7':
                                det += '\nСтолешница в сборе'
                            elif d == '8':
                                det += '\nБоковая планка стола'
                            elif d == '9':
                                det += '\nСтолешница'
                            elif d == '10':
                                det += '\nФурнитура'

                        mess = f'*{det}*'

                        inline_key = InlineKeyboardMarkup(row_width=1)
                        if sup["status_ship"] == 'Обрабатывается в цеху':
                            inline_key_b1 = InlineKeyboardButton(text='Упаковал и наклеил QR', callback_data=f'upnaqr_{sup["id_sup"]}')
                            inline_key.add(inline_key_b1)
                            await message.answer(f'ID: {sup["id_sup"]}'
                                                 f'\n📦 Подготовить детали:'
                                                 f'{mess}', reply_markup=inline_key, parse_mode='Markdown')
                        else:
                            inline_key_b1 = InlineKeyboardButton(text='Отправил', callback_data=f'otprav_{sup["id_sup"]}')
                            inline_key.add(inline_key_b1)
                            await message.answer(f'ID: {sup["id_sup"]}'
                                                 f'\n🚚 Отправить заказ с деталями:'
                                                 f'{mess}', reply_markup=inline_key, parse_mode='Markdown')

                else:
                    await message.answer('Отправок нет!')

            # Сделано
            elif message.text == markups.menu_count_retail_b6:
                inline_item = InlineKeyboardMarkup(row_width=1)
                inline_item_b1 = InlineKeyboardButton(text='Коробка Растущий', callback_data=f'zd_korrast')
                inline_item_b2 = InlineKeyboardButton(text='Раздатка растущий 1', callback_data=f'zd_raz1rast')
                inline_item_b3 = InlineKeyboardButton(text='Раздатка растущий 2', callback_data=f'zd_raz2rast')
                inline_item_b4 = InlineKeyboardButton(text='Фурнитуры Растущий', callback_data=f'zd_furrast')
                inline_item.add(inline_item_b1).add(inline_item_b2).add(inline_item_b3).add(inline_item_b4)
                await message.answer(f'Что сделано:', reply_markup=inline_item)
            elif 'zd_raz1rast_' in selone(f"SELECT act_sk FROM users WHERE id_user = '{user}'", user)['act_sk']:
                if message.text.isdigit():
                    count_i = selone(f"SELECT count_item FROM warehouse_c WHERE name_item = 'Раздатка растущий 1'", user)['count_item']
                    update(f"UPDATE warehouse_c SET count_item = '{int(count_i) + int(message.text)}' WHERE name_item = 'Раздатка растущий 1'", user)

                    count_i = selone(f"SELECT count_item FROM warehouse_c WHERE name_item = 'Инструкция Растущий 1'", user)['count_item']
                    update(f"UPDATE warehouse_c SET count_item = '{int(count_i) - int(message.text)}' WHERE name_item = 'Инструкция Растущий 1'", user)

                    count_i = selone(f"SELECT count_item FROM warehouse_c WHERE name_item = 'Файл'", user)['count_item']
                    update(f"UPDATE warehouse_c SET count_item = '{int(count_i) - int(message.text)}' WHERE name_item = 'Файл'", user)

                    count_i = selone(f"SELECT count_item FROM warehouse_c WHERE name_item = 'Карандаши'", user)['count_item']
                    update(f"UPDATE warehouse_c SET count_item = '{int(count_i) - int(message.text)}' WHERE name_item = 'Карандаши'", user)

                    update(f"UPDATE users SET act_sk = ' ' WHERE id_user = '{user}'", user)
                    await message.answer(text='Записано!')
                else:
                    await message.answer(text='Введите числом!')
            elif 'zd_raz2rast_' in selone(f"SELECT act_sk FROM users WHERE id_user = '{user}'", user)['act_sk']:
                if message.text.isdigit():
                    count_i = selone(f"SELECT count_item FROM warehouse_c WHERE name_item = 'Раздатка растущий 2'", user)['count_item']
                    update(f"UPDATE warehouse_c SET count_item = '{int(count_i) + int(message.text)}' WHERE name_item = 'Раздатка растущий 2'", user)

                    count_i = selone(f"SELECT count_item FROM warehouse_c WHERE name_item = 'Инструкция Растущий 2'", user)['count_item']
                    update(f"UPDATE warehouse_c SET count_item = '{int(count_i) - int(message.text)}' WHERE name_item = 'Инструкция Растущий 2'", user)

                    count_i = selone(f"SELECT count_item FROM warehouse_c WHERE name_item = 'Файл'", user)['count_item']
                    update(f"UPDATE warehouse_c SET count_item = '{int(count_i) - int(message.text)}' WHERE name_item = 'Файл'", user)

                    count_i = selone(f"SELECT count_item FROM warehouse_c WHERE name_item = 'Карандаши'", user)['count_item']
                    update(f"UPDATE warehouse_c SET count_item = '{int(count_i) - int(message.text)}' WHERE name_item = 'Карандаши'", user)

                    update(f"UPDATE users SET act_sk = ' ' WHERE id_user = '{user}'", user)
                    await message.answer(text='Записано!')
                else:
                    await message.answer(text='Введите числом!')
            elif 'zd_furrast_' in selone(f"SELECT act_sk FROM users WHERE id_user = '{user}'", user)['act_sk']:
                if message.text.isdigit():
                    count_i = selone(f"SELECT count_item FROM warehouse_c WHERE name_item = 'Фурнитуры Растущий'", user)['count_item']
                    update(f"UPDATE warehouse_c SET count_item = '{int(count_i) + int(message.text)}' WHERE name_item = 'Фурнитуры Растущий'", user)

                    count_i = selone(f"SELECT count_item FROM warehouse_c WHERE name_item = 'Винт мебельный 20'", user)['count_item']
                    update(f"UPDATE warehouse_c SET count_item = '{int(count_i) - (int(message.text) * 8)}' WHERE name_item = 'Винт мебельный 20'", user)

                    count_i = selone(f"SELECT count_item FROM warehouse_c WHERE name_item = 'Гайка Эриксона'", user)['count_item']
                    update(f"UPDATE warehouse_c SET count_item = '{int(count_i) - (int(message.text) * 8)}' WHERE name_item = 'Гайка Эриксона'", user)

                    count_i = selone(f"SELECT count_item FROM warehouse_c WHERE name_item = 'Заглушка беж'", user)['count_item']
                    update(f"UPDATE warehouse_c SET count_item = '{int(count_i) - (int(message.text) * 12)}' WHERE name_item = 'Заглушка беж'", user)

                    count_i = selone(f"SELECT count_item FROM warehouse_c WHERE name_item = 'Зажим для бумаги'", user)['count_item']
                    update(f"UPDATE warehouse_c SET count_item = '{int(count_i) - int(message.text)}' WHERE name_item = 'Зажим для бумаги'", user)

                    count_i = selone(f"SELECT count_item FROM warehouse_c WHERE name_item = 'Зип пакеты 80х120'", user)['count_item']
                    update(f"UPDATE warehouse_c SET count_item = '{int(count_i) - int(message.text)}' WHERE name_item = 'Зип пакеты 80х120'", user)

                    count_i = selone(f"SELECT count_item FROM warehouse_c WHERE name_item = 'Конфирмат 7х50'", user)['count_item']
                    update(f"UPDATE warehouse_c SET count_item = '{int(count_i) - (int(message.text) * 12)}' WHERE name_item = 'Конфирмат 7х50'", user)

                    count_i = selone(f"SELECT count_item FROM warehouse_c WHERE name_item = 'Шестигранник'", user)['count_item']
                    update(f"UPDATE warehouse_c SET count_item = '{int(count_i) - (int(message.text) * 2)}' WHERE name_item = 'Шестигранник'", user)

                    update(f"UPDATE users SET act_sk = ' ' WHERE id_user = '{user}'", user)
                    await message.answer(text='Записано!')
                else:
                    await message.answer(text='Введите числом!')
            elif 'zd_korrast_' in selone(f"SELECT act_sk FROM users WHERE id_user = '{user}'", user)['act_sk']:
                if message.text.isdigit():
                    count_i = selone(f"SELECT count_item FROM warehouse_c WHERE name_item = 'Коробка Растущий'", user)['count_item']
                    update(f"UPDATE warehouse_c SET count_item = '{int(count_i) + int(message.text)}' WHERE name_item = 'Коробка Растущий'", user)

                    count_i = selone(f"SELECT count_item FROM warehouse_c WHERE name_item = 'Картон'", user)['count_item']
                    update(f"UPDATE warehouse_c SET count_item = '{int(count_i) - int(message.text)}' WHERE name_item = 'Картон'", user)

                    count_i = selone(f"SELECT count_item FROM warehouse_c WHERE name_item = 'Термоклей'", user)['count_item']
                    update(f"UPDATE warehouse_c SET count_item = '{int(count_i) - int(int(message.text) / 3)}' WHERE name_item = 'Термоклей'", user)

                    update(f"UPDATE users SET act_sk = ' ' WHERE id_user = '{user}'", user)
                    await message.answer(text='Записано!')
                else:
                    await message.answer(text='Введите числом!')

            # Брак
            elif message.text == markups.menu_count_retail_b8:
                name_objects = selist(f"SELECT name_item FROM warehouse_c WHERE brak <> -1", user)
                inline_obj = InlineKeyboardMarkup(row_width=1)

                for o in name_objects:
                    inline_obj_b = InlineKeyboardButton(text=o["name_item"], callback_data=f'brk_{o["name_item"]}')
                    inline_obj.add(inline_obj_b)

                await message.answer(text='Выберите позицию:', reply_markup=inline_obj)
            elif 'brk_' in selone(f"SELECT act_sk FROM users WHERE id_user = '{user}'", user)['act_sk']:
                if message.text.isdigit():
                    res = selone(f"SELECT act_sk FROM users WHERE id_user = '{user}'", user)['act_sk'] + '_' + message.text
                    update(f"UPDATE users SET act_sk = '{res}' WHERE id_user = '{user}'", user)
                    await message.answer(text='Пришлите *ОДНО ФОТО* этого брака:', parse_mode='Markdown')
                else:
                    await message.answer(text='Введите количество числом:')

            # Уехало Склад Мебель
            elif message.text == markups.menu_count_retail_b3:
                name_objects = selist(f"SELECT name_item FROM warehouse_c WHERE min_count <> -1", user)
                inline_obj = InlineKeyboardMarkup(row_width=1)

                for o in name_objects:
                    inline_obj_b = InlineKeyboardButton(text=o["name_item"], callback_data=f'uemeb_{o["name_item"]}')
                    inline_obj.add(inline_obj_b)

                await message.answer(text='Что уехало?', reply_markup=inline_obj)
                await message.answer(text='Для возврата нажмите Отмена', reply_markup=markups.back_count)
            elif 'uemeb_' in selone(f"SELECT act_sk FROM users WHERE id_user = '{user}'", user)['act_sk']:
                if message.text.isdigit():
                    object_name = selone(f"SELECT act_sk FROM users WHERE id_user = '{user}'", user)['act_sk'].split('_')[1]
                    object_count = message.text
                    update(f"UPDATE users SET act_sk = ' ' WHERE id_user = '{user}'", user)

                    name_objects = selist(f"SELECT * FROM warehouse_c", user)
                    count_obj = selone(f"SELECT count_item FROM warehouse_c WHERE name_item = '{object_name}'", user)['count_item']

                    res_ost = 'Остаток на складе:\n'

                    for o in name_objects:
                        if o["name_item"] == object_name:
                            update(f"UPDATE warehouse_c SET count_item = '{int(count_obj) - int(object_count)}' WHERE name_item = '{object_name}'", user)
                            res_ost += f'<b>{object_name}</b>: {int(count_obj) - int(object_count)}\n'

                    if selone(f"SELECT count_retail FROM users WHERE id_user = '{user}'", user)['count_retail'] == 2:
                        await message.answer(text='Остатки по складу в Цеху изменены!',
                                             reply_markup=markups.menu_count_retail_n)
                    elif selone(f"SELECT count_retail FROM users WHERE id_user = '{user}'", user)['count_retail'] == 1:
                        await message.answer(text='Остатки по складу в Цеху изменены!',
                                             reply_markup=markups.menu_count_retail_b)

                    await message.answer(text=res_ost)

                else:
                    await message.answer(text='Введите количество числом!')

            # Открыть смену
            elif message.text == markups.menu_count_retail_b5:
                datework = str(datetime.datetime.now())[:10]
                if selone(f"SELECT count_retail FROM users WHERE id_user = '{user}'", user)['count_retail'] == 2:
                    await message.answer(text='Смена была уже открыта!', reply_markup=markups.menu_count_retail_n)
                else:
                    if len(selist(f"SELECT * FROM wood WHERE status_ship = 'Обработано, ждет отправки'", user)) == 0:
                        if selone(f"SELECT date_work FROM work_wood WHERE date_work = '{datework}'", user) is None:

                            today = datetime.datetime.today()
                            if today.weekday() == 0 or today.weekday() == 1 or today.weekday() == 2 or today.weekday() == 3 or today.weekday() == 4 or today.weekday() == 5 or today.weekday() == 6 or today.weekday() == 7:
                                name_objects = selist(f"SELECT * FROM warehouse_c WHERE min_count <> -1", user)

                                res = 'monday_'

                                with open('user', 'w', encoding='utf-8') as outfile:
                                    json.dump(name_objects, outfile, ensure_ascii=False)

                                update(f"UPDATE users SET act_sk = '{res}' WHERE id_user = '{user}'", user)

                                await message.answer(text=f'Сколько {name_objects[0]["ed_2"]} на складе позиции <b>«{name_objects[0]["name_item"]}»</b>?\nПредыдущее значение: <b>{name_objects[0]["count_item"]}</b>', reply_markup=markups.back_count)
                            else:
                                create(f"INSERT INTO `data`.`work_wood` (`date_work`) VALUES ('{datework}')", user)
                                admins = selist(f"SELECT id_user FROM users WHERE count_retail = 1", user)
                                for adm in admins:
                                    id_adm = adm['id_user']
                                    update(f"UPDATE users SET count_retail = 2 WHERE id_user = '{id_adm}'", user)

                                if selone(f"SELECT count_retail FROM users WHERE id_user = '{user}'", user)['count_retail'] == 2:
                                    await message.answer(text='Смена открыта!',
                                                                  reply_markup=markups.menu_count_retail_n)
                                elif selone(f"SELECT count_retail FROM users WHERE id_user = '{user}'", user)['count_retail'] == 1:
                                    await message.answer(text='Смена открыта!',
                                                                  reply_markup=markups.menu_count_retail_b)
                        else:
                            await message.answer(text='Смена была уже открыта!', reply_markup=markups.menu_count_retail_n)
                    else:
                        await message.answer(text='Перед открытием смены, загрузите в машину все отправки!')
            elif 'monday_' in selone(f"SELECT act_sk FROM users WHERE id_user = '{user}'", user)['act_sk']:
                if message.text.isdigit():
                    with open('user', 'r', encoding='utf-8') as outfile:
                        name_objects = json.load(outfile)

                    object_name = name_objects[0]["name_item"]
                    update(f"UPDATE warehouse_c SET count_item = '{message.text}' WHERE name_item = '{object_name}'", user)

                    del name_objects[0]
                    await message.answer(f'Записано')

                    if len(name_objects) != 0:
                        with open('user', 'w', encoding='utf-8') as outfile:
                            json.dump(name_objects, outfile, ensure_ascii=False)
                        res = 'monday_'
                        update(f"UPDATE users SET act_sk = '{res}' WHERE id_user = '{user}'", user)
                        await message.answer(text=f'Сколько {name_objects[0]["ed_2"]} на складе позиции <b>«{name_objects[0]["name_item"]}»</b>?\nПредыдущее значение: <b>{name_objects[0]["count_item"]}</b>')
                    else:
                        datework = str(datetime.datetime.now())[:10]
                        create(f"INSERT INTO `data`.`work_wood` (`date_work`) VALUES ('{datework}')", user)
                        admins = selist(f"SELECT id_user FROM users WHERE count_retail = 1", user)
                        update(f"UPDATE users SET act_sk = ' ' WHERE id_user = '{user}'", user)
                        for adm in admins:
                            id_adm = adm['id_user']
                            update(f"UPDATE users SET count_retail = 2 WHERE id_user = '{id_adm}'", user)

                        if selone(f"SELECT count_retail FROM users WHERE id_user = '{user}'", user)['count_retail'] == 2:
                            await message.answer(text='Смена открыта!',
                                                 reply_markup=markups.menu_count_retail_n)
                        elif selone(f"SELECT count_retail FROM users WHERE id_user = '{user}'", user)['count_retail'] == 1:
                            await message.answer(text='Смена открыта!',
                                                 reply_markup=markups.menu_count_retail_b)
                else:
                    await message.answer(text=f'Введите количество числом!')

            # Закрыть смену
            elif message.text == markups.menu_count_retail_b4:
                delta_1 = datetime.timedelta(hours=5)
                delta_2 = datetime.timedelta(days=1)
                now = datetime.datetime.now() + delta_1
                yester = datetime.datetime.now() + delta_1 - delta_2

                if int(now.day) < 10:
                    day_edit = '0' + str(now.day)
                else:
                    day_edit = now.day

                if int(now.month) < 10:
                    month_edit = '0' + str(now.month)
                else:
                    month_edit = now.month

                date_now = str(day_edit) + '.' + str(month_edit) + '.' + str(now.year)

                if int(yester.day) < 10:
                    day_edit_1 = '0' + str(yester.day)
                else:
                    day_edit_1 = yester.day

                if int(yester.month) < 10:
                    month_edit_1 = '0' + str(yester.month)
                else:
                    month_edit_1 = yester.month

                date_yester = str(day_edit_1) + '.' + str(month_edit_1) + '.' + str(yester.year)

                if selone(f"SELECT count_retail FROM users WHERE id_user = '{user}'", user)['count_retail'] == 2:

                    if len(selist(f"SELECT * FROM wood WHERE (date_c = '{date_now}' AND status_ship = 'Обрабатывается в цеху') OR (date_c = '{date_yester}' AND status_ship = 'Обрабатывается в цеху')", user)) == 0:

                        update(f"UPDATE users SET act_sk = 'how_' WHERE id_user = '{user}'", user)

                        await message.answer(text=f'Сколько человек работало на производстве (ВМЕСТЕ С МАСТЕРОМ)?',
                                             reply_markup=markups.back_count)
                    else:
                        await message.answer(text=f'Прежде чем закрыть смену, нужно *подготовить все отправки на сегодня*!')
                else:
                    if selone(f"SELECT count_retail FROM users WHERE id_user = '{user}'", user)['count_retail'] == 2:
                        await message.answer(text='Смена была уже закрыта!',
                                             reply_markup=markups.menu_count_retail_n)
                    elif selone(f"SELECT count_retail FROM users WHERE id_user = '{user}'", user)['count_retail'] == 1:
                        await message.answer(text='Смена была уже закрыта!',
                                             reply_markup=markups.menu_count_retail_b)
            elif 'how_' in selone(f"SELECT act_sk FROM users WHERE id_user = '{user}'", user)['act_sk']:
                if message.text.isdigit() and int(message.text) > 0:
                    res = f'count_{message.text}'
                    update(f"UPDATE users SET act_sk = '{res}' WHERE id_user = '{user}'", user)

                    worksheet = sh.worksheet("Сотрудники")
                    name_worker = worksheet.col_values(2)
                    type_worker = worksheet.col_values(7)

                    name_objects = []

                    for i in range(1, len(name_worker)):
                        if type_worker[i] != 'Руководитель' and type_worker[i] != 'Начальник производства' and type_worker[i] != 'Уволен' and type_worker[i] != 'Стажировка':
                            name_objects.append(name_worker[i])

                    main_list = [name_objects, {}]

                    with open('user', 'w', encoding='utf-8') as outfile:
                        json.dump(main_list, outfile, ensure_ascii=False)

                    inline_workers = InlineKeyboardMarkup(row_width=1)
                    for w in name_objects:
                        inline_workers_b = InlineKeyboardButton(text=w, callback_data=f'work_{w}')
                        inline_workers.add(inline_workers_b)

                    await message.answer(text='Выберите сотрудника:', reply_markup=inline_workers)

                else:
                    await message.answer(text='Введите количество цифрами и количество должно быть больше 0:')
            elif 'rastysh1_' in selone(f"SELECT act_sk FROM users WHERE id_user = '{user}'", user)['act_sk']:
                if message.text.isdigit():
                    with open('user', 'r', encoding='utf-8') as outfile:
                        name_objects = json.load(outfile)

                    name_objects.append(message.text)

                    with open('user', 'w', encoding='utf-8') as outfile:
                        json.dump(name_objects, outfile, ensure_ascii=False)

                    res = 'rastysh2_'
                    update(f"UPDATE users SET act_sk = '{res}' WHERE id_user = '{user}'", user)
                    await message.answer('Сколько сегодня произведено Растущих 2?')
                else:
                    await message.answer(text='Введите количество цифрами:')
            elif 'rastysh2_' in selone(f"SELECT act_sk FROM users WHERE id_user = '{user}'", user)['act_sk']:
                if message.text.isdigit():
                    with open('user', 'r', encoding='utf-8') as outfile:
                        name_objects = json.load(outfile)

                    name_objects.append(message.text)

                    with open('user', 'w', encoding='utf-8') as outfile:
                        json.dump(name_objects, outfile, ensure_ascii=False)

                    res = 'pervozv1_'
                    update(f"UPDATE users SET act_sk = '{res}' WHERE id_user = '{user}'", user)
                    await message.answer('Сколько сегодня упаковано возвратов Растущий 1?')
                else:
                    await message.answer(text='Введите количество цифрами:')
            elif 'pervozv1_' in selone(f"SELECT act_sk FROM users WHERE id_user = '{user}'", user)['act_sk']:
                if message.text.isdigit():
                    with open('user', 'r', encoding='utf-8') as outfile:
                        name_objects = json.load(outfile)

                    name_objects.append(message.text)

                    with open('user', 'w', encoding='utf-8') as outfile:
                        json.dump(name_objects, outfile, ensure_ascii=False)

                    res = 'pervozv2_'
                    update(f"UPDATE users SET act_sk = '{res}' WHERE id_user = '{user}'", user)
                    await message.answer('Сколько сегодня упаковано возвратов Растущий 2?')
                else:
                    await message.answer(text='Введите количество цифрами:')
            elif 'pervozv2_' in selone(f"SELECT act_sk FROM users WHERE id_user = '{user}'", user)['act_sk']:
                if message.text.isdigit():
                    await message.answer('Минуточку...')
                    update(f"UPDATE users SET act_sk = ' ' WHERE id_user = '{user}'", user)
                    with open('user', 'r', encoding='utf-8') as outfile:
                        name_objects = json.load(outfile)

                    workers = name_objects[1]

                    rast_1 = name_objects[2]
                    rast_2 = name_objects[3]
                    rast_all = int(rast_1) + int(rast_2)
                    pervozv_1 = name_objects[4]
                    pervozv_2 = message.text
                    pervozv_all = int(pervozv_1) + int(pervozv_2)

                    count_i = selone(f"SELECT count_item FROM warehouse_c WHERE name_item = 'Коробка Растущий'", user)['count_item']
                    update(f"UPDATE warehouse_c SET count_item = '{int(count_i) - int(rast_all)}' WHERE name_item = 'Коробка Растущий'", user)

                    count_i = selone(f"SELECT count_item FROM warehouse_c WHERE name_item = 'Фурнитуры Растущий'", user)['count_item']
                    update(f"UPDATE warehouse_c SET count_item = '{int(count_i) - int(rast_all)}' WHERE name_item = 'Фурнитуры Растущий'", user)

                    count_i = selone(f"SELECT count_item FROM warehouse_c WHERE name_item = 'Раздатка растущий 1'", user)['count_item']
                    update(f"UPDATE warehouse_c SET count_item = '{int(count_i) - int(rast_1)}' WHERE name_item = 'Раздатка растущий 1'",user)

                    count_i = selone(f"SELECT count_item FROM warehouse_c WHERE name_item = 'Раздатка растущий 2'", user)['count_item']
                    update(f"UPDATE warehouse_c SET count_item = '{int(count_i) - int(rast_2)}' WHERE name_item = 'Раздатка растущий 2'", user)

                    count_i = selone(f"SELECT count_item FROM warehouse_c WHERE name_item = 'ЛДСП (столешка)'", user)['count_item']
                    update(f"UPDATE warehouse_c SET count_item = '{int(count_i) - int(rast_all)}' WHERE name_item = 'ЛДСП (столешка)'", user)

                    count_i = selone(f"SELECT count_item FROM warehouse_c WHERE name_item = 'ЛДСП (спинка)'", user)['count_item']
                    update(f"UPDATE warehouse_c SET count_item = '{int(count_i) - int(rast_all)}' WHERE name_item = 'ЛДСП (спинка)'", user)

                    count_i = selone(f"SELECT count_item FROM warehouse_c WHERE name_item = 'ЛДСП (перемычка)'", user)['count_item']
                    update(f"UPDATE warehouse_c SET count_item = '{int(count_i) - int(rast_all)}' WHERE name_item = 'ЛДСП (перемычка)'", user)

                    count_i = selone(f"SELECT count_item FROM warehouse_c WHERE name_item = 'ЛДСП (сидушка)'", user)['count_item']
                    update(f"UPDATE warehouse_c SET count_item = '{int(count_i) - int(rast_all)}' WHERE name_item = 'ЛДСП (сидушка)'", user)

                    count_i = selone(f"SELECT count_item FROM warehouse_c WHERE name_item = 'Фанера 12мм'", user)['count_item']
                    update(f"UPDATE warehouse_c SET count_item = '{int(count_i) - int(int(rast_all) / 3)}' WHERE name_item = 'Фанера 12мм'",user)

                    count_i = selone(f"SELECT count_item FROM warehouse_c WHERE name_item = 'Коробка Растущий'", user)['count_item']
                    update(f"UPDATE warehouse_c SET count_item = '{int(count_i) - int(pervozv_all)}' WHERE name_item = 'Коробка Растущий'",user)

                    count_v = selone(f"SELECT count_item FROM warehouse_refunds WHERE name_item = 'Растущий стол и стул 1'", user)['count_item']
                    update(f"UPDATE warehouse_refunds SET count_item = '{int(count_v) - int(pervozv_1)}' WHERE name_item = 'Растущий стол и стул 1'", user)

                    count_v = selone(f"SELECT count_item FROM warehouse_refunds WHERE name_item = 'Растущий стол и стул 2'", user)['count_item']
                    update(f"UPDATE warehouse_refunds SET count_item = '{int(count_v) - int(pervozv_2)}' WHERE name_item = 'Растущий стол и стул 2'", user)


                    await message.answer('Заполнение гугл листа «От бота»')
                    worksheet = sh.worksheet("От бота")
                    count_date = worksheet.col_values(1)

                    delta_1 = datetime.timedelta(hours=5)
                    now = datetime.datetime.now()
                    if int(now.day) < 10:
                        day_edit = '0' + str(now.day)
                    else:
                        day_edit = now.day

                    if int(now.month) < 10:
                        month_edit = '0' + str(now.month)
                    else:
                        month_edit = now.month

                    date_create = f'{day_edit}.{month_edit}.{now.year}'

                    worksheet.update_cell(len(count_date) + 1, 1, date_create)
                    worksheet.update_cell(len(count_date) + 1, 3, rast_1)
                    worksheet.update_cell(len(count_date) + 1, 4, rast_2)
                    worksheet.update_cell(len(count_date) + 1, 7, pervozv_1)
                    worksheet.update_cell(len(count_date) + 1, 8, pervozv_2)

                    count_w = 10
                    for worker in workers:
                        worksheet.update_cell(len(count_date) + 1, count_w, worker)
                        count_w += 1

                    await message.answer('Заполнение гугл листа «График»')

                    if now.month == 1:
                        name_list = f"График Январь {now.year}"
                    elif now.month == 2:
                        name_list = f"График Февраль {now.year}"
                    elif now.month == 3:
                        name_list = f"График Март {now.year}"
                    elif now.month == 4:
                        name_list = f"График Апрель {now.year}"
                    elif now.month == 5:
                        name_list = f"График Май {now.year}"
                    elif now.month == 6:
                        name_list = f"График Июнь {now.year}"
                    elif now.month == 7:
                        name_list = f"График Июль {now.year}"
                    elif now.month == 8:
                        name_list = f"График Август {now.year}"
                    elif now.month == 9:
                        name_list = f"График Сентябрь {now.year}"
                    elif now.month == 10:
                        name_list = f"График Октябрь {now.year}"
                    elif now.month == 11:
                        name_list = f"График Ноябрь {now.year}"
                    elif now.month == 12:
                        name_list = f"График Декабрь {now.year}"

                    worksheet_2 = sh.worksheet(name_list)
                    num_row = int(now.day) + 1

                    worksheet_2.update_cell(num_row, 5, rast_all)
                    worksheet_2.update_cell(num_row, 6, pervozv_all)

                    for w in workers:
                        cell = worksheet_2.find(w)
                        num_col_b = int(cell.col)
                        num_col_n = int(cell.col) + 1
                        worksheet_2.update_cell(num_row, num_col_b, workers[w][0])
                        worksheet_2.update_cell(num_row, num_col_n, workers[w][1])


                    res = f'razgr_{message.text}'
                    update(f"UPDATE users SET act_sk = '{res}' WHERE id_user = '{user}'", user)
                    await message.answer('Сколько раз разгружали машину сегодня?')

                else:
                    await message.answer(text='Введите количество цифрами:')
            elif 'razgr_' in selone(f"SELECT act_sk FROM users WHERE id_user = '{user}'", user)['act_sk']:
                if message.text.isdigit():
                    delta_1 = datetime.timedelta(hours=5)
                    now = datetime.datetime.now()
                    await message.answer('Минуточку...')

                    await message.answer('Заполнение гугл листа «График»')

                    if now.month == 1:
                        name_list = f"График Январь {now.year}"
                    elif now.month == 2:
                        name_list = f"График Февраль {now.year}"
                    elif now.month == 3:
                        name_list = f"График Март {now.year}"
                    elif now.month == 4:
                        name_list = f"График Апрель {now.year}"
                    elif now.month == 5:
                        name_list = f"График Май {now.year}"
                    elif now.month == 6:
                        name_list = f"График Июнь {now.year}"
                    elif now.month == 7:
                        name_list = f"График Июль {now.year}"
                    elif now.month == 8:
                        name_list = f"График Август {now.year}"
                    elif now.month == 9:
                        name_list = f"График Сентябрь {now.year}"
                    elif now.month == 10:
                        name_list = f"График Октябрь {now.year}"
                    elif now.month == 11:
                        name_list = f"График Ноябрь {now.year}"
                    elif now.month == 12:
                        name_list = f"График Декабрь {now.year}"

                    worksheet_2 = sh.worksheet(name_list)
                    num_row = int(now.day) + 1

                    worksheet_2.update_cell(num_row, 4, message.text)



                    with open('user', 'r', encoding='utf-8') as outfile:
                        name_objects = json.load(outfile)

                    workers = name_objects[1]
                    rast_1 = name_objects[2]
                    rast_2 = name_objects[3]
                    rast_all = int(rast_1) + int(rast_2)
                    pervozv_1 = name_objects[4]
                    pervozv_2 = selone(f"SELECT act_sk FROM users WHERE id_user = '{user}'", user)['act_sk'].split('_')[1]
                    pervozv_all = int(pervozv_1) + int(pervozv_2)
                    razgr = message.text
                    update(f"UPDATE users SET act_sk = ' ' WHERE id_user = '{user}'", user)
                    mes = '✅ Производственная смена закрыта!\n\nРаботали: '

                    count_w = 4
                    for worker in workers:
                        mes += f'*{worker} *'
                        count_w += 1

                    acp = f'A{num_row}'
                    acd = f'B{num_row}'

                    plan = worksheet_2.acell(acp).value
                    dop = float(worksheet_2.acell(acd).value[2:].replace(',', '.'))
                    chs = float(worksheet_2.acell('C34').value[2:].replace(',', '.'))
                    chm = float(worksheet_2.acell('C35').value[2:].replace(',', '.'))
                    zav = float(worksheet_2.acell('C36').value[2:].replace(',', '.'))
                    nght = float(worksheet_2.acell('C37').value[2:].replace(',', '.'))
                    razs = float(worksheet_2.acell('C38').value[2:].replace(',', '.'))

                    worksheet_3 = sh.worksheet("От бота")
                    count_date = worksheet_3.col_values(1)

                    worksheet_3.update_cell(len(count_date), 9, message.text)
                    worksheet_3.update_cell(len(count_date), 2, plan)

                    mes += f'\n——————————————' \
                           f'\n🐥 Сделано растущих: *{rast_all}*' \
                           f'\n\nПлан: *{plan}*' \
                           f'\nСумма за одно доп. изделие: *{dop} руб.*' \
                           f'\nСумма за доп. изделия: *{(int(rast_all) - int(plan)) * dop} руб.*' \
                           f'\n——————————————' \
                           f'\n📦 Упаковано возвратов: *{pervozv_all}*' \
                           f'\n\nСумма за один возврат: *{zav} руб.*' \
                           f'\nСумма за возвраты: *{int(pervozv_all) * zav} руб.*' \
                           f'\n——————————————' \
                           f'\n🚚 Разгрузок: *{razgr}*' \
                           f'\n\nСумма за одну разгрузку: *{razs} руб.*' \
                           f'\nСумма за разгрузки: *{int(razgr) * razs} руб.*'

                    await bot.send_message(chat_id=-1002146643966, text=mes, message_thread_id=2111, parse_mode='Markdown')


                    admins = selist(f"SELECT id_user FROM users WHERE count_retail = 2", user)
                    for adm in admins:
                        id_adm = adm['id_user']
                        update(f"UPDATE users SET count_retail = 1 WHERE id_user = '{id_adm}'", user)

                    if selone(f"SELECT count_retail FROM users WHERE id_user = '{user}'", user)['count_retail'] == 2:
                        await message.answer(text='Смена закрыта!',
                                                      reply_markup=markups.menu_count_retail_n)
                    elif selone(f"SELECT count_retail FROM users WHERE id_user = '{user}'", user)['count_retail'] == 1:
                        await message.answer(text='Смена закрыта!',
                                                      reply_markup=markups.menu_count_retail_b)

                else:
                    await message.answer(text='Введите количество цифрами:')

            # Ночная смена
            elif message.text == markups.menu_count_retail_b9:
                update(f"UPDATE users SET act_sk = 'hows_' WHERE id_user = '{user}'", user)

                await message.answer(text=f'Сколько человек работало на ночью?', reply_markup=markups.back_count)
            elif 'hows_' in selone(f"SELECT act_sk FROM users WHERE id_user = '{user}'", user)['act_sk']:
                if message.text.isdigit() and int(message.text) > 0:
                    await message.answer(text='Минуточку...')
                    res = f'counts_{message.text}'
                    update(f"UPDATE users SET act_sk = '{res}' WHERE id_user = '{user}'", user)

                    worksheet = sh.worksheet("Сотрудники")
                    name_worker = worksheet.col_values(2)
                    type_worker = worksheet.col_values(7)

                    name_objects = []

                    for i in range(1, len(name_worker)):
                        if type_worker[i] != 'Руководитель' and type_worker[i] != 'Начальник производства' and type_worker[i] != 'Уволен' and type_worker[i] != 'Стажировка':
                            name_objects.append(name_worker[i])

                    main_list = [name_objects, {}]

                    with open('user', 'w', encoding='utf-8') as outfile:
                        json.dump(main_list, outfile, ensure_ascii=False)

                    inline_workers = InlineKeyboardMarkup(row_width=1)
                    for w in name_objects:
                        inline_workers_b = InlineKeyboardButton(text=w, callback_data=f'works_{w}')
                        inline_workers.add(inline_workers_b)

                    await message.answer(text='Выберите сотрудника:', reply_markup=inline_workers)

                else:
                    await message.answer(text='Введите количество цифрами и количество должно быть больше 0:')
            elif 'rastyshs1_' in selone(f"SELECT act_sk FROM users WHERE id_user = '{user}'", user)['act_sk']:
                if message.text.isdigit():
                    res = 'rastyshs2_' + message.text
                    update(f"UPDATE users SET act_sk = '{res}' WHERE id_user = '{user}'", user)
                    await message.answer('Сколько произведено Растущих 2?')
                else:
                    await message.answer(text='Введите количество цифрами:')
            elif 'rastyshs2_' in selone(f"SELECT act_sk FROM users WHERE id_user = '{user}'", user)['act_sk']:
                if message.text.isdigit():
                    await message.answer('Минуточку...')
                    with open('user', 'r', encoding='utf-8') as outfile:
                        name_objects = json.load(outfile)

                    workers = name_objects[1]
                    rast_1 = selone(f"SELECT act_sk FROM users WHERE id_user = '{user}'", user)['act_sk'].split('_')[1]
                    rast_2 = message.text
                    rast_all = int(rast_1) + int(rast_2)
                    update(f"UPDATE users SET act_sk = ' ' WHERE id_user = '{user}'", user)
                    count_i = selone(f"SELECT count_item FROM warehouse_c WHERE name_item = 'Коробка Растущий'", user)['count_item']
                    update(f"UPDATE warehouse_c SET count_item = '{int(count_i) - int(rast_all)}' WHERE name_item = 'Коробка Растущий'",user)

                    count_i = selone(f"SELECT count_item FROM warehouse_c WHERE name_item = 'Раздатка 1'", user)['count_item']
                    update(f"UPDATE warehouse_c SET count_item = '{int(count_i) - int(rast_1)}' WHERE name_item = 'Раздатка 1'",user)

                    count_i = selone(f"SELECT count_item FROM warehouse_c WHERE name_item = 'Раздатка 2'", user)['count_item']
                    update(f"UPDATE warehouse_c SET count_item = '{int(count_i) - int(rast_2)}' WHERE name_item = 'Раздатка 2'", user)

                    count_i = selone(f"SELECT count_item FROM warehouse_c WHERE name_item = 'Фурнитуры Растущий'", user)['count_item']
                    update(f"UPDATE warehouse_c SET count_item = '{int(count_i) - int(rast_all)}' WHERE name_item = 'Фурнитуры Растущий'",user)

                    count_i = selone(f"SELECT count_item FROM warehouse_c WHERE name_item = 'ЛДСП (столешка)'", user)['count_item']
                    update(f"UPDATE warehouse_c SET count_item = '{int(count_i) - int(rast_all)}' WHERE name_item = 'ЛДСП (столешка)'", user)

                    count_i = selone(f"SELECT count_item FROM warehouse_c WHERE name_item = 'ЛДСП (спинка)'", user)['count_item']
                    update(f"UPDATE warehouse_c SET count_item = '{int(count_i) - int(rast_all)}' WHERE name_item = 'ЛДСП (спинка)'", user)

                    count_i = selone(f"SELECT count_item FROM warehouse_c WHERE name_item = 'ЛДСП (перемычка)'", user)['count_item']
                    update(f"UPDATE warehouse_c SET count_item = '{int(count_i) - int(rast_all)}' WHERE name_item = 'ЛДСП (перемычка)'", user)

                    count_i = selone(f"SELECT count_item FROM warehouse_c WHERE name_item = 'ЛДСП (сидушка)'", user)['count_item']
                    update(f"UPDATE warehouse_c SET count_item = '{int(count_i) - int(rast_all)}' WHERE name_item = 'ЛДСП (сидушка)'", user)

                    count_i = selone(f"SELECT count_item FROM warehouse_c WHERE name_item = 'Фанера 15мм'", user)['count_item']
                    update(f"UPDATE warehouse_c SET count_item = '{int(count_i) - int(int(rast_all) / 3)}' WHERE name_item = 'Фанера 15мм'",user)

                    await message.answer('Заполнение гугл листа «От бота»')
                    worksheet_4 = sh.worksheet("От бота")
                    count_date = worksheet_4.col_values(1)

                    delta_1 = datetime.timedelta(days=1)
                    now = datetime.datetime.now() - delta_1
                    if int(now.day) < 10:
                        day_edit = '0' + str(now.day)
                    else:
                        day_edit = now.day

                    if int(now.month) < 10:
                        month_edit = '0' + str(now.month)
                    else:
                        month_edit = now.month

                    date_create = f'{day_edit}.{month_edit}.{now.year}'
                    cell = worksheet_4.find(date_create)
                    num_col_n = int(cell.row)
                    worksheet_4.update_cell(num_col_n, 5, rast_1)
                    worksheet_4.update_cell(num_col_n, 6, rast_2)

                    await message.answer('Заполнение гугл листа «График»')

                    if now.month == 1:
                        name_list = f"График Январь {now.year}"
                    elif now.month == 2:
                        name_list = f"График Февраль {now.year}"
                    elif now.month == 3:
                        name_list = f"График Март {now.year}"
                    elif now.month == 4:
                        name_list = f"График Апрель {now.year}"
                    elif now.month == 5:
                        name_list = f"График Май {now.year}"
                    elif now.month == 6:
                        name_list = f"График Июнь {now.year}"
                    elif now.month == 7:
                        name_list = f"График Июль {now.year}"
                    elif now.month == 8:
                        name_list = f"График Август {now.year}"
                    elif now.month == 9:
                        name_list = f"График Сентябрь {now.year}"
                    elif now.month == 10:
                        name_list = f"График Октябрь {now.year}"
                    elif now.month == 11:
                        name_list = f"График Ноябрь {now.year}"
                    elif now.month == 12:
                        name_list = f"График Декабрь {now.year}"

                    worksheet_2 = sh.worksheet(name_list)
                    num_row = int(now.day) + 1

                    edrast = round(int(rast_all) / len(workers), 2)

                    for w in workers:
                        cell = worksheet_2.find(w)
                        num_col_n = int(cell.col) + 2
                        worksheet_2.update_cell(num_row, num_col_n, edrast)

                    update(f"UPDATE users SET act_sk = ' ' WHERE id_user = '{user}'", user)

                    mes = '🌙 Была закрыта ночная смена.\n\nРаботали: '

                    count_w = 4
                    for worker in workers:
                        mes += f'*{worker} *'
                        count_w += 1

                    nght = float(worksheet_2.acell('C37').value[2:].replace(',', '.'))

                    mes += f'\n——————————————' \
                           f'\n🐥 Сделано растущих: *{rast_all}*' \
                           f'\n\nСумма за одно изделие: *{nght} руб.*' \
                           f'\nОбщая сумма за изделия: *{int(rast_all) * nght} руб.*' \


                    await bot.send_message(chat_id=-1002146643966, text=mes, message_thread_id=2111, parse_mode='Markdown')

                    await message.answer('✅ Записано!\n\n_Для продолжения нажмите Отмена_', parse_mode='Markdown')

                else:
                    await message.answer(text='Введите количество цифрами:')

            # Меню логистика
            elif message.text == markups.menu_admin_b4:
                if selone(f"SELECT company FROM users WHERE id_user = '{user}'", user)['company'] == 'Босс':
                    await message.answer(text=texts.menu_logistic, reply_markup=markups.menu_logistic)

                else:
                    await message.answer(text='У вас нет доступа!')

            # Отмена Склад ФФ
            elif message.text == markups.menu_back_logistic:
                defaul_values(user)
                await message.answer(text=texts.menu_logistic, reply_markup=markups.menu_logistic)

            # Создать заявку
            elif message.text == markups.menu_logistic_b1:
                update(f"UPDATE users SET act_log = 'type_' WHERE id_user = '{user}'", user)
                inline_type_b = ReplyKeyboardMarkup(resize_keyboard=True)
                inline_type_b1 = 'Забор'
                inline_type_b2 = 'FBS'
                inline_type_b3 = 'FBO'
                inline_type_b4 = 'Расходники'
                inline_type_b5 = 'Внутренняя'
                inline_type_b6 = 'Доставка'
                inline_type_b7 = 'Возвраты'
                menu_back_logistic = '❌ Отмена'
                inline_type_b.add(inline_type_b1, inline_type_b2, inline_type_b3).add(inline_type_b6).add(inline_type_b7).add(inline_type_b4, inline_type_b5).add(menu_back_logistic)
                await message.answer(text='Выберите тип заявки или введите иное', reply_markup=inline_type_b)
            elif 'type_' in selone(f"SELECT act_log FROM users WHERE id_user = '{user}'", user)['act_log']:
                res = 'date_' + message.text
                update(f"UPDATE users SET act_log = '{res}' WHERE id_user = '{user}'", user)
                inline_date = ReplyKeyboardMarkup(resize_keyboard=True)
                inline_date_b1 = f'{sk.date_create()}'
                inline_date_b2 = f'{sk.date_tomorrow_create()}'
                menu_back_logistic = '❌ Отмена'
                inline_date.add(inline_date_b1, inline_date_b2).add(menu_back_logistic)
                await message.answer(text='Введите дату когда нужно выполнить заявку <i>(в формате 01.11.2023)</i>', reply_markup=inline_date)
            elif 'date_' in selone(f"SELECT act_log FROM users WHERE id_user = '{user}'", user)['act_log']:
                if len(message.text.split('.')) == 3 and len(message.text) == 10:
                    delta_1 = datetime.timedelta(hours=5)
                    now = datetime.datetime.now() + delta_1

                    if ((int(message.text[0:2]) < int(now.day)) and (int(message.text[3:5]) == int(now.month))) or (int(message.text[3:5]) < int(now.month)):
                        await message.answer(text='Вы можете указать дату начиная с сегодняшнего дня:', reply_markup=markups.back_logistic)

                    elif (int(message.text[0:2]) == int(now.day)) and (int(sk.time_create()[0:2]) > 18):
                        await message.answer(text='На сегодня вы уже не можете создать заявку, укажите другую дату:', reply_markup=markups.back_logistic)

                    elif selone(f"SELECT date_work FROM work_ship WHERE date_work = '{message.text}'", user) is not None:
                        th_res = selone(f"SELECT act_log FROM users WHERE id_user = '{user}'", user)['act_log']
                        sec_res = th_res + '_' + str(message.text)
                        first_res = sec_res.split('_')
                        del first_res[0]


                        newlist = selist(f"SELECT * FROM shipping WHERE date_ship = '{message.text}' AND (status_ship = 'В очереди' OR status_ship = 'Принят' OR status_ship = 'Едет к получателю')", user)
                        if len(newlist) > 0:
                            await message.answer(text='<b>Очередь заявок на этот день:</b>',
                                                 reply_markup=markups.back_logistic)
                            list_log = sorted(newlist, key=lambda d: d['num_ship'])
                            for l in list_log:
                                await message.answer(text=f'ID: *{l["id_ship"]}*\n'
                                                          f'Тип: *{l["type_ship"]}*\n'
                                                          f'Дата: *{l["date_ship"]}*\n'
                                                          f'Время: *{l["time_ship"]}*\n'
                                                          f'Предмет: *{l["item_ship"]}*\n'
                                                          f'Количество: *{l["count_item_ship"]}*\n'
                                                          f'Вес: *{l["w_ship"]}*\n\n'
                                                          f'Адрес загрузки: *{l["adress_begin"]}*\n'
                                                          f'Адрес разгрузки: *{l["adress_end"]}*\n'
                                                          f'Комментарий: *{l["comment_ship"]}*\n', parse_mode='Markdown')
                            res = 'dateyes_' + '_'.join(first_res)
                            update(f"UPDATE users SET act_log = '{res}' WHERE id_user = '{user}'", user)
                            update(f"UPDATE users SET comment_pack_fbs = '{message.text}' WHERE id_user = '{user}'", user)
                            await message.answer(text='Введите ID заявки, после которой вы хотите вставить новую заявку')
                            await message.answer(text='Если хотите поставить заявку в начало, введите 0')
                        else:
                            newlist = selist(f"SELECT num_ship FROM shipping WHERE date_ship = '{message.text}'", user)
                            list_log = sorted(newlist, key=lambda d: d['num_ship'])
                            num_ship = int(list_log[-1]['num_ship']) + 1
                            th_res = selone(f"SELECT act_log FROM users WHERE id_user = '{user}'", user)['act_log']
                            sec_res = th_res + '_' + str(message.text) + '_'+ str(num_ship)
                            first_res = sec_res.split('_')
                            del first_res[0]

                            if first_res[0] == 'Забор':
                                res = 'count_' + '_'.join(first_res) + '_Короб'
                                update(f"UPDATE users SET act_log = '{res}' WHERE id_user = '{user}'", user)
                                await message.answer(text='Введите количество коробов:',
                                                     reply_markup=markups.back_logistic)
                            elif first_res[0] == 'FBS':
                                inline_item = ReplyKeyboardMarkup(resize_keyboard=True)
                                inline_item_b1 = 'Мебель'
                                inline_item_b2 = 'Клиентские заказы'
                                menu_back_logistic = '❌ Отмена'
                                inline_item.add(inline_item_b1).add(inline_item_b2).add(menu_back_logistic)

                                res = 'item_' + '_'.join(first_res)
                                update(f"UPDATE users SET act_log = '{res}' WHERE id_user = '{user}'", user)
                                await message.answer(
                                    text='Выберите наименование наименование предметов или введите иное:',
                                    reply_markup=inline_item)
                            elif first_res[0] == 'Возвраты':
                                inline_item = ReplyKeyboardMarkup(resize_keyboard=True)
                                inline_item_b1 = 'Мебель'
                                menu_back_logistic = '❌ Отмена'
                                inline_item.add(inline_item_b1).add(menu_back_logistic)

                                res = 'item_' + '_'.join(first_res)
                                update(f"UPDATE users SET act_log = '{res}' WHERE id_user = '{user}'", user)
                                await message.answer(
                                    text='Выберите наименование наименование предметов или введите иное:',
                                    reply_markup=inline_item)
                            elif first_res[0] == 'Доставка':
                                inline_item = ReplyKeyboardMarkup(resize_keyboard=True)
                                inline_item_b1 = 'Мебель'
                                menu_back_logistic = '❌ Отмена'
                                inline_item.add(inline_item_b1).add(menu_back_logistic)

                                res = 'item_' + '_'.join(first_res)
                                update(f"UPDATE users SET act_log = '{res}' WHERE id_user = '{user}'", user)
                                await message.answer(
                                    text='Выберите наименование наименование предметов или введите иное:',
                                    reply_markup=inline_item)
                            elif first_res[0] == 'FBO':
                                res = 'count_' + '_'.join(first_res) + '_Короб'
                                update(f"UPDATE users SET act_log = '{res}' WHERE id_user = '{user}'", user)
                                await message.answer(text='Введите количество коробов:',
                                                     reply_markup=markups.back_logistic)
                            elif first_res[0] == 'Расходники':
                                res = 'item_' + '_'.join(first_res)
                                update(f"UPDATE users SET act_log = '{res}' WHERE id_user = '{user}'", user)
                                await message.answer(text='Введите наименование предмета:',
                                                     reply_markup=markups.back_logistic)
                            elif first_res[0] == 'Внутренняя':
                                inline_item = ReplyKeyboardMarkup(resize_keyboard=True)
                                inline_item_b1 = 'Растущий стол и стул 1'
                                inline_item_b2 = 'Растущий стол и стул 2'
                                inline_item_b3 = 'Наполнитель 15 кг'
                                inline_item_b4 = 'Парящие полки'
                                menu_back_logistic = '❌ Отмена'
                                inline_item.add(inline_item_b1, inline_item_b2).add(inline_item_b3, inline_item_b4).add(menu_back_logistic)

                                res = 'item_' + '_'.join(first_res)
                                update(f"UPDATE users SET act_log = '{res}' WHERE id_user = '{user}'", user)
                                await message.answer(
                                    text='Выберите наименование предметов или введите иное:',
                                    reply_markup=inline_item)
                            else:
                                res = 'item_' + '_'.join(first_res)
                                update(f"UPDATE users SET act_log = '{res}' WHERE id_user = '{user}'", user)
                                await message.answer(text='Введите наименование предмета:',
                                                     reply_markup=markups.back_logistic)

                    else:
                        th_res = selone(f"SELECT act_log FROM users WHERE id_user = '{user}'", user)['act_log']
                        sec_res = th_res + '_' + str(message.text)
                        first_res = sec_res.split('_')
                        del first_res[0]

                        if first_res[0] == 'Забор':
                            res = 'count_' + '_'.join(first_res) + '_0' + '_Короб'
                            update(f"UPDATE users SET act_log = '{res}' WHERE id_user = '{user}'", user)
                            await message.answer(text='Введите количество коробов:', reply_markup=markups.back_logistic)
                        elif first_res[0] == 'FBS':
                            inline_item = ReplyKeyboardMarkup(resize_keyboard=True)
                            inline_item_b1 = 'Мебель'
                            inline_item_b2 = 'Клиентские заказы'
                            menu_back_logistic = '❌ Отмена'
                            inline_item.add(inline_item_b1).add(inline_item_b2).add(menu_back_logistic)

                            res = 'item_' + '_'.join(first_res) + '_0'
                            update(f"UPDATE users SET act_log = '{res}' WHERE id_user = '{user}'", user)
                            await message.answer(text='Выберите наименование наименование предметов или введите иное:', reply_markup=inline_item)
                        elif first_res[0] == 'Доставка':
                            inline_item = ReplyKeyboardMarkup(resize_keyboard=True)
                            inline_item_b1 = 'Мебель'
                            menu_back_logistic = '❌ Отмена'
                            inline_item.add(inline_item_b1).add(menu_back_logistic)

                            res = 'item_' + '_'.join(first_res) + '_0'
                            update(f"UPDATE users SET act_log = '{res}' WHERE id_user = '{user}'", user)
                            await message.answer(text='Выберите наименование наименование предметов или введите иное:', reply_markup=inline_item)
                        elif first_res[0] == 'FBO':
                            res = 'count_' + '_'.join(first_res) + '_0' + '_Короб'
                            update(f"UPDATE users SET act_log = '{res}' WHERE id_user = '{user}'", user)
                            await message.answer(text='Введите количество коробов:', reply_markup=markups.back_logistic)
                        elif first_res[0] == 'Возвраты':
                            inline_item = ReplyKeyboardMarkup(resize_keyboard=True)
                            inline_item_b1 = 'Мебель'
                            menu_back_logistic = '❌ Отмена'
                            inline_item.add(inline_item_b1).add(menu_back_logistic)

                            res = 'item_' + '_'.join(first_res) + '_0'
                            update(f"UPDATE users SET act_log = '{res}' WHERE id_user = '{user}'", user)
                            await message.answer(
                                text='Выберите наименование наименование предметов или введите иное:',
                                reply_markup=inline_item)
                        elif first_res[0] == 'Расходники':
                            res = 'item_' + '_'.join(first_res) + '_0'
                            update(f"UPDATE users SET act_log = '{res}' WHERE id_user = '{user}'", user)
                            await message.answer(text='Введите наименование предмета:', reply_markup=markups.back_logistic)
                        elif first_res[0] == 'Внутренняя':
                            inline_item = ReplyKeyboardMarkup(resize_keyboard=True)
                            inline_item_b1 = 'Растущий стол и стул 1'
                            inline_item_b2 = 'Растущий стол и стул 2'
                            inline_item_b3 = 'Наполнитель 15 кг'
                            inline_item_b4 = 'Парящие полки'
                            menu_back_logistic = '❌ Отмена'
                            inline_item.add(inline_item_b1, inline_item_b2).add(inline_item_b3, inline_item_b4).add(menu_back_logistic)

                            res = 'item_' + '_'.join(first_res) + '_0'
                            update(f"UPDATE users SET act_log = '{res}' WHERE id_user = '{user}'", user)
                            await message.answer(text='Выберите наименование наименование предметов или введите иное:', reply_markup=inline_item)

                        else:
                            res = 'item_' + '_'.join(first_res) + '_0'
                            update(f"UPDATE users SET act_log = '{res}' WHERE id_user = '{user}'", user)
                            await message.answer(text='Введите наименование предмета:', reply_markup=markups.back_logistic)
                else:
                    await message.answer(text='Введите дату в формате 01.11.2023:', reply_markup=markups.back_logistic)
            elif 'dateyes_' in selone(f"SELECT act_log FROM users WHERE id_user = '{user}'", user)['act_log']:
                if message.text.isdigit():
                    if int(message.text) == 0:
                        date_create = selone(f"SELECT comment_pack_fbs FROM users WHERE id_user = '{user}'", user)['comment_pack_fbs']
                        newlist = selist(f"SELECT * FROM shipping WHERE date_ship = '{date_create}'", user)
                        list_log = sorted(newlist, key=lambda d: d['num_ship'])
                        for l in list_log:
                            if l['num_ship'] != 0:
                                num_ship = l['num_ship'] / 2
                                break

                        th_res = selone(f"SELECT act_log FROM users WHERE id_user = '{user}'", user)['act_log']
                        sec_res = th_res + '_' + str(num_ship)
                        first_res = sec_res.split('_')
                        del first_res[0]

                        if first_res[0] == 'Забор':
                            res = 'count_' + '_'.join(first_res) + '_Короб'
                            update(f"UPDATE users SET act_log = '{res}' WHERE id_user = '{user}'", user)
                            await message.answer(text='Введите количество коробов:', reply_markup=markups.back_logistic)
                        elif first_res[0] == 'FBS':
                            inline_item = ReplyKeyboardMarkup(resize_keyboard=True)
                            inline_item_b1 = 'Мебель'
                            inline_item_b2 = 'Клиентские заказы'
                            menu_back_logistic = '❌ Отмена'
                            inline_item.add(inline_item_b1).add(inline_item_b2).add(menu_back_logistic)

                            res = 'item_' + '_'.join(first_res)
                            update(f"UPDATE users SET act_log = '{res}' WHERE id_user = '{user}'", user)
                            await message.answer(text='Выберите наименование предметов или введите иное:', reply_markup=inline_item)
                        elif first_res[0] == 'Возвраты':
                            inline_item = ReplyKeyboardMarkup(resize_keyboard=True)
                            inline_item_b1 = 'Мебель'
                            menu_back_logistic = '❌ Отмена'
                            inline_item.add(inline_item_b1).add(menu_back_logistic)

                            res = 'item_' + '_'.join(first_res)
                            update(f"UPDATE users SET act_log = '{res}' WHERE id_user = '{user}'", user)
                            await message.answer(text='Выберите наименование предметов или введите иное:', reply_markup=inline_item)
                        elif first_res[0] == 'Доставка':
                            inline_item = ReplyKeyboardMarkup(resize_keyboard=True)
                            inline_item_b1 = 'Мебель'
                            menu_back_logistic = '❌ Отмена'
                            inline_item.add(inline_item_b1).add(menu_back_logistic)

                            res = 'item_' + '_'.join(first_res)
                            update(f"UPDATE users SET act_log = '{res}' WHERE id_user = '{user}'", user)
                            await message.answer(text='Выберите наименование предметов или введите иное:', reply_markup=inline_item)
                        elif first_res[0] == 'FBO':
                            res = 'count_' + '_'.join(first_res) + '_Короб'
                            update(f"UPDATE users SET act_log = '{res}' WHERE id_user = '{user}'", user)
                            await message.answer(text='Введите количество коробов:', reply_markup=markups.back_logistic)
                        elif first_res[0] == 'Расходники':
                            res = 'item_' + '_'.join(first_res)
                            update(f"UPDATE users SET act_log = '{res}' WHERE id_user = '{user}'", user)
                            await message.answer(text='Введите наименование предмета:', reply_markup=markups.back_logistic)
                        elif first_res[0] == 'Внутренняя':
                            inline_item = ReplyKeyboardMarkup(resize_keyboard=True)
                            inline_item_b1 = 'Растущий стол и стул 1'
                            inline_item_b2 = 'Растущий стол и стул 2'
                            inline_item_b3 = 'Наполнитель 15 кг'
                            inline_item_b4 = 'Парящие полки'
                            menu_back_logistic = '❌ Отмена'
                            inline_item.add(inline_item_b1, inline_item_b2).add(inline_item_b3, inline_item_b4).add(menu_back_logistic)

                            res = 'item_' + '_'.join(first_res)
                            update(f"UPDATE users SET act_log = '{res}' WHERE id_user = '{user}'", user)
                            await message.answer(text='Выберите наименование наименование предметов или введите иное:', reply_markup=inline_item)
                        else:
                            res = 'item_' + '_'.join(first_res)
                            update(f"UPDATE users SET act_log = '{res}' WHERE id_user = '{user}'", user)
                            await message.answer(text='Введите наименование предмета:', reply_markup=markups.back_logistic)


                    elif selone(f"SELECT num_ship FROM shipping WHERE id_ship = '{int(message.text)}'", user) is not None:
                        date_create = selone(f"SELECT date_ship FROM shipping WHERE id_ship = '{int(message.text)}'", user)['date_ship']
                        newlist = selist(f"SELECT * FROM shipping WHERE date_ship = '{date_create}'", user)
                        num_start = selone(f"SELECT num_ship FROM shipping WHERE id_ship = '{int(message.text)}'", user)['num_ship']
                        list_log = sorted(newlist, key=lambda d: d['num_ship'])
                        for i in range(len(list_log)):
                            if i == len(list_log) - 1:
                                num_ship = list_log[i]['num_ship'] + 1
                            elif list_log[i]['num_ship'] == num_start:
                                num_ship = list_log[i]['num_ship'] + ((list_log[i + 1]['num_ship'] - list_log[i]['num_ship']) / 2)
                                break

                        th_res = selone(f"SELECT act_log FROM users WHERE id_user = '{user}'", user)['act_log']
                        sec_res = th_res + '_' + str(num_ship)
                        first_res = sec_res.split('_')
                        del first_res[0]

                        if first_res[0] == 'Забор':
                            res = 'count_' + '_'.join(first_res) + '_Короб'
                            update(f"UPDATE users SET act_log = '{res}' WHERE id_user = '{user}'", user)
                            await message.answer(text='Введите количество коробов:', reply_markup=markups.back_logistic)
                        elif first_res[0] == 'FBS':
                            inline_item = ReplyKeyboardMarkup(resize_keyboard=True)
                            inline_item_b1 = 'Мебель'
                            inline_item_b2 = 'Клиентские заказы'
                            menu_back_logistic = '❌ Отмена'
                            inline_item.add(inline_item_b1).add(inline_item_b2).add(menu_back_logistic)

                            res = 'item_' + '_'.join(first_res)
                            update(f"UPDATE users SET act_log = '{res}' WHERE id_user = '{user}'", user)
                            await message.answer(text='Выберите наименование наименование предметов или введите иное:', reply_markup=inline_item)
                        elif first_res[0] == 'Возвраты':
                            inline_item = ReplyKeyboardMarkup(resize_keyboard=True)
                            inline_item_b1 = 'Мебель'
                            menu_back_logistic = '❌ Отмена'
                            inline_item.add(inline_item_b1).add(menu_back_logistic)

                            res = 'item_' + '_'.join(first_res)
                            update(f"UPDATE users SET act_log = '{res}' WHERE id_user = '{user}'", user)
                            await message.answer(text='Выберите наименование наименование предметов или введите иное:',
                                                 reply_markup=inline_item)
                        elif first_res[0] == 'Доставка':
                            inline_item = ReplyKeyboardMarkup(resize_keyboard=True)
                            inline_item_b1 = 'Мебель'
                            menu_back_logistic = '❌ Отмена'
                            inline_item.add(inline_item_b1).add(menu_back_logistic)

                            res = 'item_' + '_'.join(first_res)
                            update(f"UPDATE users SET act_log = '{res}' WHERE id_user = '{user}'", user)
                            await message.answer(text='Выберите наименование наименование предметов или введите иное:', reply_markup=inline_item)
                        elif first_res[0] == 'FBO':
                            res = 'count_' + '_'.join(first_res) + '_Короб'
                            update(f"UPDATE users SET act_log = '{res}' WHERE id_user = '{user}'", user)
                            await message.answer(text='Введите количество коробов:', reply_markup=markups.back_logistic)
                        elif first_res[0] == 'Расходники':
                            res = 'item_' + '_'.join(first_res)
                            update(f"UPDATE users SET act_log = '{res}' WHERE id_user = '{user}'", user)
                            await message.answer(text='Введите наименование предмета:', reply_markup=markups.back_logistic)
                        elif first_res[0] == 'Внутренняя':
                            inline_item = ReplyKeyboardMarkup(resize_keyboard=True)
                            inline_item_b1 = 'Растущий стол и стул 1'
                            inline_item_b2 = 'Растущий стол и стул 2'
                            inline_item_b3 = 'Наполнитель 15 кг'
                            inline_item_b4 = 'Парящие полки'
                            menu_back_logistic = '❌ Отмена'
                            inline_item.add(inline_item_b1, inline_item_b2).add(inline_item_b3, inline_item_b4).add(menu_back_logistic)

                            res = 'item_' + '_'.join(first_res)
                            update(f"UPDATE users SET act_log = '{res}' WHERE id_user = '{user}'", user)
                            await message.answer(text='Выберите наименование наименование предметов или введите иное:', reply_markup=inline_item)
                        else:
                            res = 'item_' + '_'.join(first_res)
                            update(f"UPDATE users SET act_log = '{res}' WHERE id_user = '{user}'", user)
                            await message.answer(text='Введите наименование предмета:', reply_markup=markups.back_logistic)
                    else:
                        await message.answer(text='Заявки с таким ID не найдено, введите другой ID:', reply_markup=markups.back_logistic)
                else:
                    await message.answer(text='Введите ID числом:', reply_markup=markups.back_logistic)
            elif 'item_' in selone(f"SELECT act_log FROM users WHERE id_user = '{user}'", user)['act_log']:
                th_res = selone(f"SELECT act_log FROM users WHERE id_user = '{user}'", user)['act_log']
                sec_res = th_res + '_' + str(message.text)
                first_res = sec_res.split('_')
                del first_res[0]
                if message.text == 'Клиентские заказы':
                    res = 'adressb_' + '_'.join(first_res) + '_Не указано' + '_Не указано'
                    update(f"UPDATE users SET act_log = '{res}' WHERE id_user = '{user}'", user)
                    inline_ad = ReplyKeyboardMarkup(resize_keyboard=True)
                    inline_ad_b1 = 'Сафроновский проезд 6 (ФФ)'
                    inline_ad_b2 = 'Аральская 47 (Мебельный цех)'
                    menu_back_logistic = '❌ Отмена'
                    inline_ad.add(inline_ad_b1).add(inline_ad_b2).add(menu_back_logistic)
                    await message.answer(text='Выберите адрес загрузки или введите иной:', reply_markup=inline_ad)
                else:
                    res = 'count_' + '_'.join(first_res)
                    update(f"UPDATE users SET act_log = '{res}' WHERE id_user = '{user}'", user)
                    await message.answer(text='Введите количество:', reply_markup=markups.back_logistic)
            elif 'count_' in selone(f"SELECT act_log FROM users WHERE id_user = '{user}'", user)['act_log']:
                if message.text.isdigit():
                    th_res = selone(f"SELECT act_log FROM users WHERE id_user = '{user}'", user)['act_log']
                    sec_res = th_res + '_' + str(message.text)
                    first_res = sec_res.split('_')
                    del first_res[0]
                    res = 'we_' + '_'.join(first_res)
                    update(f"UPDATE users SET act_log = '{res}' WHERE id_user = '{user}'", user)
                    await message.answer(text='Укажите общий вес <i>(например 20кг. или 1т.)</i>:', reply_markup=markups.back_logistic)
                else:
                    await message.answer(text='Введите количество числом:', reply_markup=markups.back_logistic)
            elif 'we_' in selone(f"SELECT act_log FROM users WHERE id_user = '{user}'", user)['act_log']:
                th_res = selone(f"SELECT act_log FROM users WHERE id_user = '{user}'", user)['act_log']
                sec_res = th_res + '_' + str(message.text)
                first_res = sec_res.split('_')
                del first_res[0]
                if first_res[0] == 'Забор':
                    res = 'adressb_' + '_'.join(first_res)
                    update(f"UPDATE users SET act_log = '{res}' WHERE id_user = '{user}'", user)
                    await message.answer(text='Введите адрес и номер подъезда:', reply_markup=markups.back_logistic)
                elif first_res[0] == 'FBS':
                    inline_ad = ReplyKeyboardMarkup(resize_keyboard=True)
                    inline_ad_b1 = 'Сафроновский проезд 6 (ФФ)'
                    inline_ad_b2 = 'Аральская 47 (Мебельный цех)'
                    menu_back_logistic = '❌ Отмена'
                    inline_ad.add(inline_ad_b1).add(inline_ad_b2).add(menu_back_logistic)

                    res = 'adressb_' + '_'.join(first_res)
                    update(f"UPDATE users SET act_log = '{res}' WHERE id_user = '{user}'", user)
                    await message.answer(text='Выберите адрес загрузки или введите иной:', reply_markup=inline_ad)
                elif first_res[0] == 'Возвраты':
                    inline_ad = ReplyKeyboardMarkup(resize_keyboard=True)
                    inline_ad_b1 = 'Чернышевского 7 (Wildberries)'
                    inline_ad_b2 = 'Гафури 101 (Яндекс Маркет)'
                    inline_ad_b3 = 'Карьерная 7 ст7 (OZON)'
                    menu_back_logistic = '❌ Отмена'
                    inline_ad.add(inline_ad_b1).add(inline_ad_b2).add(inline_ad_b3).add(menu_back_logistic)

                    res = 'adressb_' + '_'.join(first_res)
                    update(f"UPDATE users SET act_log = '{res}' WHERE id_user = '{user}'", user)
                    await message.answer(text='Выберите адрес загрузки или введите иной:', reply_markup=inline_ad)
                elif first_res[0] == 'Доставка':
                    inline_ad = ReplyKeyboardMarkup(resize_keyboard=True)
                    inline_ad_b1 = 'Сафроновский проезд 6 (ФФ)'
                    inline_ad_b2 = 'Аральская 47 (Мебельный цех)'
                    menu_back_logistic = '❌ Отмена'
                    inline_ad.add(inline_ad_b1).add(inline_ad_b2).add(menu_back_logistic)

                    res = 'adressb_' + '_'.join(first_res)
                    update(f"UPDATE users SET act_log = '{res}' WHERE id_user = '{user}'", user)
                    await message.answer(text='Выберите адрес загрузки или введите иной:', reply_markup=inline_ad)
                elif first_res[0] == 'FBO':
                    inline_ad = ReplyKeyboardMarkup(resize_keyboard=True)
                    inline_ad_b1 = 'Сафроновский проезд 6 (ФФ)'
                    inline_ad_b2 = 'Аральская 47 (Мебельный цех)'
                    menu_back_logistic = '❌ Отмена'
                    inline_ad.add(inline_ad_b1).add(inline_ad_b2).add(menu_back_logistic)

                    res = 'adressb_' + '_'.join(first_res)
                    update(f"UPDATE users SET act_log = '{res}' WHERE id_user = '{user}'", user)
                    await message.answer(text='Выберите адрес загрузки или введите иной:', reply_markup=inline_ad)
                elif first_res[0] == 'Расходники':
                    inline_ad = ReplyKeyboardMarkup(resize_keyboard=True)
                    inline_ad_b1 = 'Российская 60Б (УфаСклад)'
                    inline_ad_b2 = 'Силикатная ул., 3/1 (Гофрика)'
                    inline_ad_b3 = 'Новожёнова, 88В (Стройпак)'
                    inline_ad_b4 = 'Базисный пр., 2 (Боярд)'
                    inline_ad_b5 = 'Владивостокская, 4Б (Фрезы 102)'
                    inline_ad_b6 = 'Благоварская, 4 к.1'
                    menu_back_logistic = '❌ Отмена'
                    inline_ad.add(inline_ad_b1).add(inline_ad_b2).add(inline_ad_b3).add(inline_ad_b4).add(inline_ad_b5).add(inline_ad_b6).add(menu_back_logistic)

                    res = 'adressb_' + '_'.join(first_res)
                    update(f"UPDATE users SET act_log = '{res}' WHERE id_user = '{user}'", user)
                    await message.answer(text='Выберите адрес загрузки или введите иной:', reply_markup=inline_ad)
                elif first_res[0] == 'Внутренняя':
                    inline_ad = ReplyKeyboardMarkup(resize_keyboard=True)
                    inline_ad_b1 = 'Сафроновский проезд 6 (ФФ)'
                    inline_ad_b2 = 'Аральская 47 (Мебельный цех)'
                    inline_ad_b4 = 'Силикатная 28Б (Офис)'
                    menu_back_logistic = '❌ Отмена'
                    inline_ad.add(inline_ad_b1).add(inline_ad_b2).add(inline_ad_b4).add(menu_back_logistic)

                    res = 'adressb_' + '_'.join(first_res)
                    update(f"UPDATE users SET act_log = '{res}' WHERE id_user = '{user}'", user)
                    await message.answer(text='Выберите адрес загрузки или введите иной:', reply_markup=inline_ad)
                else:
                    inline_ad = ReplyKeyboardMarkup(resize_keyboard=True)
                    inline_ad_b1 = 'Сафроновский проезд 6 (ФФ)'
                    inline_ad_b2 = 'Аральская 47 (Мебельный цех)'
                    inline_ad_b4 = 'Силикатная 28Б (Офис)'
                    menu_back_logistic = '❌ Отмена'
                    inline_ad.add(inline_ad_b1).add(inline_ad_b2).add(inline_ad_b4).add(menu_back_logistic)

                    res = 'adressb_' + '_'.join(first_res)
                    update(f"UPDATE users SET act_log = '{res}' WHERE id_user = '{user}'", user)
                    await message.answer(text='Выберите адрес загрузки или введите иной:', reply_markup=inline_ad)
            elif 'adressb_' in selone(f"SELECT act_log FROM users WHERE id_user = '{user}'", user)['act_log']:
                th_res = selone(f"SELECT act_log FROM users WHERE id_user = '{user}'", user)['act_log']
                sec_res = th_res + '_' + str(message.text)
                first_res = sec_res.split('_')
                del first_res[0]

                if first_res[0] == 'Забор':
                    res = 'phoneb_' + '_'.join(first_res)
                    update(f"UPDATE users SET act_log = '{res}' WHERE id_user = '{user}'", user)
                    await message.answer(text='Введите номер телефона и имя клиента:', reply_markup=markups.back_logistic)
                elif first_res[0] == 'FBS':
                    if message.text == 'Сафроновский проезд 6 (ФФ)':
                        inline_phone = ReplyKeyboardMarkup(resize_keyboard=True)
                        inline_phone_b2 = '8-996-102-04-54 Ануар'
                        inline_phone_b4 = '8-995-948-29-00 Рахман'
                        menu_back_logistic = '❌ Отмена'
                        inline_phone.add(inline_phone_b2).add(inline_phone_b4).add(menu_back_logistic)
                        res = 'phoneb_' + '_'.join(first_res)
                        update(f"UPDATE users SET act_log = '{res}' WHERE id_user = '{user}'", user)
                        await message.answer(text='Выберите контакт или введите иной:', reply_markup=inline_phone)
                    elif message.text == 'Аральская 47 (Мебельный цех)':
                        inline_phone = ReplyKeyboardMarkup(resize_keyboard=True)
                        inline_phone_b1 = '8-986-702-18-15 Нурислам'
                        inline_phone_b2 = '8-987-351-37-49 Рамиль'

                        menu_back_logistic = '❌ Отмена'
                        inline_phone.add(inline_phone_b1).add(inline_phone_b2).add(menu_back_logistic)
                        res = 'phoneb_' + '_'.join(first_res)
                        update(f"UPDATE users SET act_log = '{res}' WHERE id_user = '{user}'", user)
                        await message.answer(text='Выберите контакт или введите иной:', reply_markup=inline_phone)
                    else:
                        res = 'phoneb_' + '_'.join(first_res)
                        update(f"UPDATE users SET act_log = '{res}' WHERE id_user = '{user}'", user)
                        await message.answer(text='Введите номер телефона и имя:', reply_markup=markups.back_logistic)
                elif first_res[0] == 'Доставка':
                    if message.text == 'Сафроновский проезд 6 (ФФ)':
                        inline_phone = ReplyKeyboardMarkup(resize_keyboard=True)
                        inline_phone_b2 = '8-996-102-04-54 Ануар'
                        inline_phone_b4 = '8-995-948-29-00 Рахман'
                        menu_back_logistic = '❌ Отмена'
                        inline_phone.add(inline_phone_b2).add(inline_phone_b4).add(menu_back_logistic)
                        res = 'phoneb_' + '_'.join(first_res)
                        update(f"UPDATE users SET act_log = '{res}' WHERE id_user = '{user}'", user)
                        await message.answer(text='Выберите контакт или введите иной:', reply_markup=inline_phone)
                    elif message.text == 'Аральская 47 (Мебельный цех)':
                        inline_phone = ReplyKeyboardMarkup(resize_keyboard=True)
                        inline_phone_b1 = '8-986-702-18-15 Нурислам'
                        inline_phone_b2 = '8-987-351-37-49 Рамиль'

                        menu_back_logistic = '❌ Отмена'
                        inline_phone.add(inline_phone_b1).add(inline_phone_b2).add(menu_back_logistic)
                        res = 'phoneb_' + '_'.join(first_res)
                        update(f"UPDATE users SET act_log = '{res}' WHERE id_user = '{user}'", user)
                        await message.answer(text='Выберите контакт или введите иной:', reply_markup=inline_phone)
                    else:
                        res = 'phoneb_' + '_'.join(first_res)
                        update(f"UPDATE users SET act_log = '{res}' WHERE id_user = '{user}'", user)
                        await message.answer(text='Введите номер телефона и имя:', reply_markup=markups.back_logistic)
                elif first_res[0] == 'FBO':
                    if message.text == 'Сафроновский проезд 6 (ФФ)':
                        inline_phone = ReplyKeyboardMarkup(resize_keyboard=True)
                        inline_phone_b2 = '8-996-102-04-54 Ануар'
                        inline_phone_b4 = '8-995-948-29-00 Рахман'
                        menu_back_logistic = '❌ Отмена'
                        inline_phone.add(inline_phone_b2).add(inline_phone_b4).add(menu_back_logistic)
                        res = 'phoneb_' + '_'.join(first_res)
                        update(f"UPDATE users SET act_log = '{res}' WHERE id_user = '{user}'", user)
                        await message.answer(text='Выберите контакт или введите иной:', reply_markup=inline_phone)
                    elif message.text == 'Аральская 47 (Мебельный цех)':
                        inline_phone = ReplyKeyboardMarkup(resize_keyboard=True)
                        inline_phone_b1 = '8-986-702-18-15 Нурислам'
                        inline_phone_b2 = '8-987-351-37-49 Рамиль'

                        menu_back_logistic = '❌ Отмена'
                        inline_phone.add(inline_phone_b1).add(inline_phone_b2).add(menu_back_logistic)
                        res = 'phoneb_' + '_'.join(first_res)
                        update(f"UPDATE users SET act_log = '{res}' WHERE id_user = '{user}'", user)
                        await message.answer(text='Выберите контакт или введите иной:', reply_markup=inline_phone)
                    else:
                        res = 'phoneb_' + '_'.join(first_res)
                        update(f"UPDATE users SET act_log = '{res}' WHERE id_user = '{user}'", user)
                        await message.answer(text='Введите номер телефона и имя:', reply_markup=markups.back_logistic)
                elif first_res[0] == 'Расходники':
                    res = 'phoneb_' + '_'.join(first_res)
                    update(f"UPDATE users SET act_log = '{res}' WHERE id_user = '{user}'", user)
                    await message.answer(text='Введите номер телефона и имя:', reply_markup=markups.back_logistic)
                elif first_res[0] == 'Внутренняя':
                    if message.text == 'Сафроновский проезд 6 (ФФ)':
                        inline_phone = ReplyKeyboardMarkup(resize_keyboard=True)
                        inline_phone_b2 = '8-996-102-04-54 Ануар'
                        inline_phone_b4 = '8-995-948-29-00 Рахман'
                        menu_back_logistic = '❌ Отмена'
                        inline_phone.add(inline_phone_b2).add(inline_phone_b4).add(menu_back_logistic)
                        res = 'phoneb_' + '_'.join(first_res)
                        update(f"UPDATE users SET act_log = '{res}' WHERE id_user = '{user}'", user)
                        await message.answer(text='Выберите контакт или введите иной:', reply_markup=inline_phone)
                    elif message.text == 'Аральская 47 (Мебельный цех)':
                        inline_phone = ReplyKeyboardMarkup(resize_keyboard=True)
                        inline_phone_b1 = '8-986-702-18-15 Нурислам'
                        inline_phone_b2 = '8-987-351-37-49 Рамиль'

                        menu_back_logistic = '❌ Отмена'
                        inline_phone.add(inline_phone_b1).add(inline_phone_b2).add(menu_back_logistic)
                        res = 'phoneb_' + '_'.join(first_res)
                        update(f"UPDATE users SET act_log = '{res}' WHERE id_user = '{user}'", user)
                        await message.answer(text='Выберите контакт или введите иной:', reply_markup=inline_phone)

                    elif message.text == 'Силикатная 28Б (Офис)':
                        inline_phone = ReplyKeyboardMarkup(resize_keyboard=True)
                        inline_phone_b1 = '8-987-256-07-06 Роман'
                        inline_phone_b2 = '8-917-782-17-21 Айнур'

                        menu_back_logistic = '❌ Отмена'
                        inline_phone.add(inline_phone_b1).add(inline_phone_b2).add(menu_back_logistic)
                        res = 'phoneb_' + '_'.join(first_res)
                        update(f"UPDATE users SET act_log = '{res}' WHERE id_user = '{user}'", user)
                        await message.answer(text='Выберите контакт или введите иной:', reply_markup=inline_phone)
                    else:
                        res = 'phoneb_' + '_'.join(first_res)
                        update(f"UPDATE users SET act_log = '{res}' WHERE id_user = '{user}'", user)
                        await message.answer(text='Введите номер телефона и имя:', reply_markup=markups.back_logistic)
                else:
                    res = 'phoneb_' + '_'.join(first_res)
                    update(f"UPDATE users SET act_log = '{res}' WHERE id_user = '{user}'", user)
                    await message.answer(text='Введите номер телефона и имя:', reply_markup=markups.back_logistic)
            elif 'phoneb_' in selone(f"SELECT act_log FROM users WHERE id_user = '{user}'", user)['act_log']:
                th_res = selone(f"SELECT act_log FROM users WHERE id_user = '{user}'", user)['act_log']
                sec_res = th_res + '_' + str(message.text)
                first_res = sec_res.split('_')
                del first_res[0]

                if first_res[0] == 'Забор':
                    inline_tm = ReplyKeyboardMarkup(resize_keyboard=True)
                    inline_tm_b1 = 'с 13:00 до 17:00'
                    menu_back_logistic = '❌ Отмена'
                    inline_tm.add(inline_tm_b1).add(menu_back_logistic)

                    res = 'timeship_' + '_'.join(first_res)
                    update(f"UPDATE users SET act_log = '{res}' WHERE id_user = '{user}'", user)
                    await message.answer(text='Выберите время или введите иное:', reply_markup=inline_tm)
                elif first_res[0] == 'FBS':
                    inline_tm = ReplyKeyboardMarkup(resize_keyboard=True)
                    inline_tm_b1 = 'с 10:00 до 13:00'
                    menu_back_logistic = '❌ Отмена'
                    inline_tm.add(inline_tm_b1).add(menu_back_logistic)

                    res = 'timeship_' + '_'.join(first_res)
                    update(f"UPDATE users SET act_log = '{res}' WHERE id_user = '{user}'", user)
                    await message.answer(text='Выберите время или введите иное:', reply_markup=inline_tm)
                elif first_res[0] == 'FBO':
                    inline_tm = ReplyKeyboardMarkup(resize_keyboard=True)
                    inline_tm_b1 = 'до 20:00'
                    menu_back_logistic = '❌ Отмена'
                    inline_tm.add(inline_tm_b1).add(menu_back_logistic)

                    res = 'timeship_' + '_'.join(first_res)
                    update(f"UPDATE users SET act_log = '{res}' WHERE id_user = '{user}'", user)
                    await message.answer(text='Выберите время или введите иное:', reply_markup=inline_tm)
                elif first_res[0] == 'Расходники':
                    inline_tm = ReplyKeyboardMarkup(resize_keyboard=True)
                    inline_tm_b1 = 'до 13:00'
                    inline_tm_b2 = 'до 14:00'
                    inline_tm_b3 = 'до 15:00'
                    inline_tm_b4 = 'до 16:00'
                    inline_tm_b5 = 'до 17:00'
                    menu_back_logistic = '❌ Отмена'
                    inline_tm.add(inline_tm_b1, inline_tm_b2).add(inline_tm_b3, inline_tm_b4).add(inline_tm_b5).add(menu_back_logistic)

                    res = 'timeship_' + '_'.join(first_res)
                    update(f"UPDATE users SET act_log = '{res}' WHERE id_user = '{user}'", user)
                    await message.answer(text='Выберите время или введите иное:', reply_markup=inline_tm)
                elif first_res[0] == 'Доставка':
                    inline_tm = ReplyKeyboardMarkup(resize_keyboard=True)
                    inline_tm_b2 = 'до 14:00'
                    inline_tm_b3 = 'до 15:00'
                    inline_tm_b4 = 'до 16:00'
                    inline_tm_b5 = 'до 17:00'
                    menu_back_logistic = '❌ Отмена'
                    inline_tm.add(inline_tm_b2, inline_tm_b3).add(inline_tm_b4, inline_tm_b5).add(menu_back_logistic)

                    res = 'timeship_' + '_'.join(first_res)
                    update(f"UPDATE users SET act_log = '{res}' WHERE id_user = '{user}'", user)
                    await message.answer(text='Выберите время или введите иное:', reply_markup=inline_tm)
                elif first_res[0] == 'Внутренняя':
                    inline_tm = ReplyKeyboardMarkup(resize_keyboard=True)
                    inline_tm_b1 = 'до 13:00'
                    inline_tm_b2 = 'до 14:00'
                    inline_tm_b3 = 'до 15:00'
                    inline_tm_b4 = 'до 16:00'
                    inline_tm_b5 = 'до 17:00'
                    menu_back_logistic = '❌ Отмена'
                    inline_tm.add(inline_tm_b1, inline_tm_b2).add(inline_tm_b3, inline_tm_b4).add(inline_tm_b5).add(menu_back_logistic)

                    res = 'timeship_' + '_'.join(first_res)
                    update(f"UPDATE users SET act_log = '{res}' WHERE id_user = '{user}'", user)
                    await message.answer(text='Выберите время или введите иное:', reply_markup=inline_tm)
                else:
                    inline_tm = ReplyKeyboardMarkup(resize_keyboard=True)
                    inline_tm_b1 = 'до 13:00'
                    inline_tm_b2 = 'до 14:00'
                    inline_tm_b3 = 'до 15:00'
                    inline_tm_b4 = 'до 16:00'
                    inline_tm_b5 = 'до 17:00'
                    menu_back_logistic = '❌ Отмена'
                    inline_tm.add(inline_tm_b1, inline_tm_b2).add(inline_tm_b3, inline_tm_b4).add(inline_tm_b5).add(
                        menu_back_logistic)

                    res = 'timeship_' + '_'.join(first_res)
                    update(f"UPDATE users SET act_log = '{res}' WHERE id_user = '{user}'", user)
                    await message.answer(text='Выберите время или введите иное:', reply_markup=inline_tm)
            elif 'timeship_' in selone(f"SELECT act_log FROM users WHERE id_user = '{user}'", user)['act_log']:
                th_res = selone(f"SELECT act_log FROM users WHERE id_user = '{user}'", user)['act_log']
                sec_res = th_res + '_' + str(message.text)
                first_res = sec_res.split('_')
                del first_res[0]

                if first_res[0] == 'Забор':
                    inline_ad = ReplyKeyboardMarkup(resize_keyboard=True)
                    inline_ad_b1 = 'Сафроновский проезд 6 (ФФ)'
                    menu_back_logistic = '❌ Отмена'
                    inline_ad.add(inline_ad_b1).add(menu_back_logistic)

                    res = 'adressn_' + '_'.join(first_res)
                    update(f"UPDATE users SET act_log = '{res}' WHERE id_user = '{user}'", user)
                    await message.answer(text='Выберите адрес разгрузки или введите иной:', reply_markup=inline_ad)
                elif first_res[0] == 'FBS':
                    inline_ad = ReplyKeyboardMarkup(resize_keyboard=True)
                    inline_ad_b1 = 'Ленина 128 (CDEK)'
                    inline_ad_b2 = 'Гафури 101 (Яндекс Маркет)'
                    inline_ad_b3 = 'Комсомольская 15 (OZON)'
                    inline_ad_b4 = 'Карьерная 7 ст7 (OZON)'
                    inline_ad_b5 = 'Электрозаводская 2А (Wildberries)'
                    menu_back_logistic = '❌ Отмена'
                    inline_ad.add(inline_ad_b1).add(inline_ad_b2).add(inline_ad_b3).add(inline_ad_b4).add(inline_ad_b5).add(menu_back_logistic)

                    res = 'adressn_' + '_'.join(first_res)
                    update(f"UPDATE users SET act_log = '{res}' WHERE id_user = '{user}'", user)
                    await message.answer(text='Выберите адрес разгрузки или введите иной:', reply_markup=inline_ad)
                elif first_res[0] == 'FBO':
                    inline_ad = ReplyKeyboardMarkup(resize_keyboard=True)
                    inline_ad_b1 = 'Карьерная 7 ст7 (OZON)'
                    inline_ad_b2 = 'Мокроусовская 8г (Wildberries)'
                    menu_back_logistic = '❌ Отмена'
                    inline_ad.add(inline_ad_b1).add(inline_ad_b2).add(menu_back_logistic)

                    res = 'adressn_' + '_'.join(first_res)
                    update(f"UPDATE users SET act_log = '{res}' WHERE id_user = '{user}'", user)
                    await message.answer(text='Выберите адрес разгрузки или введите иной:', reply_markup=inline_ad)
                elif first_res[0] == 'Расходники':
                    inline_ad = ReplyKeyboardMarkup(resize_keyboard=True)
                    inline_ad_b1 = 'Сафроновский проезд 6 (ФФ)'
                    inline_ad_b2 = 'Аральская 47 (Мебельный цех)'
                    menu_back_logistic = '❌ Отмена'
                    inline_ad.add(inline_ad_b1).add(inline_ad_b2).add(menu_back_logistic)

                    res = 'adressn_' + '_'.join(first_res)
                    update(f"UPDATE users SET act_log = '{res}' WHERE id_user = '{user}'", user)
                    await message.answer(text='Выберите адрес разгрузки или введите иной:', reply_markup=inline_ad)
                elif first_res[0] == 'Возвраты':
                    inline_ad = ReplyKeyboardMarkup(resize_keyboard=True)
                    inline_ad_b1 = 'Сафроновский проезд 6 (ФФ)'
                    inline_ad_b2 = 'Аральская 47 (Мебельный цех)'
                    menu_back_logistic = '❌ Отмена'
                    inline_ad.add(inline_ad_b1).add(inline_ad_b2).add(menu_back_logistic)

                    res = 'adressn_' + '_'.join(first_res)
                    update(f"UPDATE users SET act_log = '{res}' WHERE id_user = '{user}'", user)
                    await message.answer(text='Выберите адрес разгрузки или введите иной:', reply_markup=inline_ad)
                elif first_res[0] == 'Внутренняя':
                    inline_ad = ReplyKeyboardMarkup(resize_keyboard=True)
                    inline_ad_b1 = 'Сафроновский проезд 6 (ФФ)'
                    inline_ad_b2 = 'Аральская 47 (Мебельный цех)'
                    inline_ad_b4 = 'Силикатная 28Б (Офис)'
                    menu_back_logistic = '❌ Отмена'
                    inline_ad.add(inline_ad_b1).add(inline_ad_b2).add(inline_ad_b4).add(menu_back_logistic)

                    res = 'adressn_' + '_'.join(first_res)
                    update(f"UPDATE users SET act_log = '{res}' WHERE id_user = '{user}'", user)
                    await message.answer(text='Выберите адрес разгрузки или введите иной:', reply_markup=inline_ad)
                else:
                    inline_ad = ReplyKeyboardMarkup(resize_keyboard=True)
                    inline_ad_b1 = 'Сафроновский проезд 6 (ФФ)'
                    inline_ad_b2 = 'Аральская 47 (Мебельный цех)'
                    inline_ad_b4 = 'Силикатная 28Б (Офис)'
                    menu_back_logistic = '❌ Отмена'
                    inline_ad.add(inline_ad_b1).add(inline_ad_b2).add(inline_ad_b4).add(menu_back_logistic)

                    res = 'adressn_' + '_'.join(first_res)
                    update(f"UPDATE users SET act_log = '{res}' WHERE id_user = '{user}'", user)
                    await message.answer(text='Выберите адрес разгрузки или введите иной:', reply_markup=inline_ad)
            elif 'adressn_' in selone(f"SELECT act_log FROM users WHERE id_user = '{user}'", user)['act_log']:
                th_res = selone(f"SELECT act_log FROM users WHERE id_user = '{user}'", user)['act_log']
                sec_res = th_res + '_' + str(message.text)
                first_res = sec_res.split('_')
                del first_res[0]

                if message.text == 'Сафроновский проезд 6 (ФФ)':
                    inline_phone = ReplyKeyboardMarkup(resize_keyboard=True)
                    inline_phone_b2 = '8-996-102-04-54 Ануар'
                    inline_phone_b4 = '8-995-948-29-00 Рахман'
                    menu_back_logistic = '❌ Отмена'
                    inline_phone.add(inline_phone_b2).add(inline_phone_b4).add(menu_back_logistic)
                    res = 'phonen_' + '_'.join(first_res)
                    update(f"UPDATE users SET act_log = '{res}' WHERE id_user = '{user}'", user)
                    await message.answer(text='Выберите контакт или введите иной:', reply_markup=inline_phone)
                elif message.text == 'Ленина 128 (CDEK)' or message.text == 'Гафури 101 (Яндекс Маркет)' or message.text == 'Комсомольская 15 (OZON)' or message.text == 'Карьерная 7 ст7 (OZON)' or message.text == 'Мокроусовская 8г (Wildberries)' or message.text == 'Электрозаводская 2А (Wildberries)':
                    res = 'comment_' + '_'.join(first_res) + '_Нет номера'
                    update(f"UPDATE users SET act_log = '{res}' WHERE id_user = '{user}'", user)
                    await message.answer(text='Укажите дополнительный комментарий:', reply_markup=markups.back_logistic)
                elif message.text == 'Аральская 47 (Мебельный цех)':
                    inline_phone = ReplyKeyboardMarkup(resize_keyboard=True)
                    inline_phone_b1 = '8-986-702-18-15 Нурислам'
                    inline_phone_b2 = '8-987-351-37-49 Рамиль'

                    menu_back_logistic = '❌ Отмена'
                    inline_phone.add(inline_phone_b1).add(inline_phone_b2).add(menu_back_logistic)
                    res = 'phonen_' + '_'.join(first_res)
                    update(f"UPDATE users SET act_log = '{res}' WHERE id_user = '{user}'", user)
                    await message.answer(text='Выберите контакт или введите иной:', reply_markup=inline_phone)
                elif message.text == 'Силикатная 28Б (Офис)':
                    inline_phone = ReplyKeyboardMarkup(resize_keyboard=True)
                    inline_phone_b1 = '8-987-256-07-06 Роман'
                    inline_phone_b2 = '8-917-782-17-21 Айнур'

                    menu_back_logistic = '❌ Отмена'
                    inline_phone.add(inline_phone_b1).add(inline_phone_b2).add(menu_back_logistic)
                    res = 'phonen_' + '_'.join(first_res)
                    update(f"UPDATE users SET act_log = '{res}' WHERE id_user = '{user}'", user)
                    await message.answer(text='Выберите контакт или введите иной:', reply_markup=inline_phone)
                else:
                    res = 'phonen_' + '_'.join(first_res)
                    update(f"UPDATE users SET act_log = '{res}' WHERE id_user = '{user}'", user)
                    await message.answer(text='Введите номер телефона и имя для связи на разгрузке:', reply_markup=markups.back_logistic)
            elif 'phonen_' in selone(f"SELECT act_log FROM users WHERE id_user = '{user}'", user)['act_log']:
                th_res = selone(f"SELECT act_log FROM users WHERE id_user = '{user}'", user)['act_log']
                sec_res = th_res + '_' + str(message.text)
                first_res = sec_res.split('_')
                del first_res[0]

                res = 'comment_' + '_'.join(first_res)
                update(f"UPDATE users SET act_log = '{res}' WHERE id_user = '{user}'", user)
                await message.answer(text='Укажите дополнительный комментарий:', reply_markup=markups.back_logistic)
            elif 'comment_' in selone(f"SELECT act_log FROM users WHERE id_user = '{user}'", user)['act_log']:
                first_res = selone(f"SELECT act_log FROM users WHERE id_user = '{user}'", user)['act_log'].split('_')
                type_ship = first_res[1]
                date_ship = first_res[2]
                num_ship = first_res[3]
                item_ship = first_res[4]
                count_item_ship = first_res[5]
                w_ship = first_res[6]
                adress_begin = first_res[7]
                phone_begin = first_res[8]
                time_ship = first_res[9]
                adress_end = first_res[10]
                phone_end = first_res[11]
                comment_ship = message.text
                update(f"UPDATE users SET act_log = ' ' WHERE id_user = '{user}'", user)

                create(f"REPLACE INTO shipping(type_ship, date_ship, num_ship, item_ship, count_item_ship, w_ship, adress_begin, phone_begin, time_ship, adress_end, phone_end, comment_ship) VALUES ('{type_ship}', '{date_ship}', '{num_ship}', '{item_ship}', '{count_item_ship}', '{w_ship}', '{adress_begin}', '{phone_begin}', '{time_ship}', '{adress_end}', '{phone_end}', '{comment_ship}')", user)

                list_all_users = selist(f"SELECT * FROM users", user)
                list_user = []
                for us in list_all_users:
                    if 'log' in us['notif']:
                        list_user.append(us)

                for user1 in list_user:
                    try:
                        chat_id = str(user1["id_user"])
                        destination_bot = Bot(token='6490496152:AAHnBwfDRlUTyTFMOMGGCK6Eu3WejYpesIE')
                        await destination_bot.send_message(chat_id, f'*Новая заявка!*\n\n'
                                                                    f'Тип: *{type_ship}*\n'
                                                                    f'Дата: *{date_ship}*\n'
                                                                    f'Время: *{time_ship}*\n'
                                                                    f'Предмет: *{item_ship}*\n'
                                                                    f'Количество: *{count_item_ship}*\n'
                                                                    f'Вес: *{w_ship}*\n\n'
                                                                    f'Адрес загрузки: *{adress_begin}*\n'
                                                                    f'Адрес разгрузки: *{adress_end}*\n'
                                                                    f'Комментарий: *{comment_ship}*\n', parse_mode='Markdown')
                    except:
                        pass

                await message.answer(text='Заявка создана', reply_markup=markups.menu_logistic)

            # Заявки на доставку
            elif message.text == markups.menu_logistic_b6:
                if len(selist(f"SELECT * FROM shipping WHERE (type_ship = 'Доставка' AND status_ship <> 'Отменен') AND (type_ship = 'Доставка' AND status_ship <> 'Закончен')", user)) != 0:
                    await message.answer(text='*Очередь заявок на доставку:*', reply_markup=markups.back_logistic, parse_mode='Markdown')
                    newlist = selist(f"SELECT * FROM shipping WHERE (type_ship = 'Доставка' AND status_ship <> 'Отменен') AND (type_ship = 'Доставка' AND status_ship <> 'Закончен')", user)

                    list_log = sorted(newlist, key=lambda d: d['num_ship'])
                    for l in list_log:
                        inline_m = InlineKeyboardMarkup(row_width=2)
                        inline_m_b1 = InlineKeyboardButton(text='Отменить', callback_data=f'logisnoyes_{l["id_ship"]}')
                        inline_m.add(inline_m_b1)
                        await message.answer(text=f'ID: *{l["id_ship"]}*\n'
                                                  f'Тип: *{l["type_ship"]}*\n'
                                                  f'Дата: *{l["date_ship"]}*\n'
                                                  f'Время: *{l["time_ship"]}*\n'
                                                  f'Предмет: *{l["item_ship"]}*\n'
                                                  f'Количество: *{l["count_item_ship"]}*\n'
                                                  f'Вес: *{l["w_ship"]}*\n\n'
                                                  f'Адрес загрузки: `{l["adress_begin"]}`\n'
                                                  f'Телефон загрузки: `{l["phone_begin"]}`\n'
                                                  f'Адрес разгрузки: `{l["adress_end"]}`\n'
                                                  f'Телефон разгрузки: `{l["phone_end"]}`\n'
                                                  f'Комментарий: *{l["comment_ship"]}*\n\n'
                                                  f'Статус: *{l["status_ship"]}*', parse_mode='Markdown',
                                             reply_markup=inline_m)
                else:
                    await message.answer(text='Очередь пуста!')

            # Заявки на забор
            elif message.text == markups.menu_logistic_b7:
                if len(selist(f"SELECT * FROM shipping WHERE (type_ship = 'Забор' AND status_ship <> 'Отменен') AND (type_ship = 'Забор' AND status_ship <> 'Закончен')", user)) != 0:
                    await message.answer(text='*Очередь заявок на забор:*', reply_markup=markups.back_logistic, parse_mode='Markdown')
                    newlist = selist(f"SELECT * FROM shipping WHERE (type_ship = 'Забор' AND status_ship <> 'Отменен') AND (type_ship = 'Забор' AND status_ship <> 'Закончен')", user)

                    list_log = sorted(newlist, key=lambda d: d['num_ship'])
                    for l in list_log:
                        inline_m = InlineKeyboardMarkup(row_width=2)
                        inline_m_b1 = InlineKeyboardButton(text='Отменить', callback_data=f'logisnoyes_{l["id_ship"]}')
                        inline_m.add(inline_m_b1)
                        await message.answer(text=f'ID: *{l["id_ship"]}*\n'
                                                  f'Тип: *{l["type_ship"]}*\n'
                                                  f'Дата: *{l["date_ship"]}*\n'
                                                  f'Время: *{l["time_ship"]}*\n'
                                                  f'Предмет: *{l["item_ship"]}*\n'
                                                  f'Количество: *{l["count_item_ship"]}*\n'
                                                  f'Вес: *{l["w_ship"]}*\n\n'
                                                  f'Адрес загрузки: `{l["adress_begin"]}`\n'
                                                  f'Телефон загрузки: `{l["phone_begin"]}`\n'
                                                  f'Адрес разгрузки: `{l["adress_end"]}`\n'
                                                  f'Телефон разгрузки: `{l["phone_end"]}`\n'
                                                  f'Комментарий: *{l["comment_ship"]}*\n\n'
                                                  f'Статус: *{l["status_ship"]}*', parse_mode='Markdown',
                                             reply_markup=inline_m)
                else:
                    await message.answer(text='Очередь пуста!')

            # Маршрутный лист
            elif message.text == markups.menu_logistic_b2:
                update(f"UPDATE users SET act_log = 'numd_' WHERE id_user = '{user}'", user)

                inline_date = ReplyKeyboardMarkup(resize_keyboard=True)
                inline_date_b1 = f'{sk.date_create()}'
                inline_date_b2 = f'{sk.date_tomorrow_create()}'
                menu_back_logistic = '❌ Отмена'
                inline_date.add(inline_date_b1, inline_date_b2).add(menu_back_logistic)

                await message.answer(text='Выберите дату', reply_markup=inline_date)
            elif 'newz_' in selone(f"SELECT act_log FROM users WHERE id_user = '{user}'", user)['act_log']:
                phone_begin = message.text
                date_ship = selone(f"SELECT act_log FROM users WHERE id_user = '{user}'", user)['act_log'].split('_')[1]
                if selone(f"SELECT date_work FROM work_ship_begin WHERE date_work = '{message.text}'", user) is None:
                    create(f"REPLACE INTO shipping(type_ship, date_ship, num_ship, item_ship, count_item_ship, w_ship, adress_begin, phone_begin, time_ship, adress_end, phone_end, comment_ship) VALUES ('FBS', '{date_ship}', 0, 'Мебель', 'Не указано', 'Не указано', 'Аральская 47 (Мебельный цех)', '{phone_begin}', 'с 10:00 до 13:00', 'Гафури 101 (Яндекс Маркет)', 'Нет номера', 'Успеть сдать до 18:00')", user)
                    create(f"REPLACE INTO shipping(type_ship, date_ship, num_ship, item_ship, count_item_ship, w_ship, adress_begin, phone_begin, time_ship, adress_end, phone_end, comment_ship) VALUES ('FBS', '{date_ship}', 0, 'Краска', 1, 'Не указано', 'Глазовская 24/1 ст3 (Колор Центр)', '89872553335', 'с 10:00 до 13:00', 'Электрозаводская 2А (Wildberries)', 'Нет номера', 'Успеть сдать до 18:00')", user)
                    create(f"REPLACE INTO shipping(type_ship, date_ship, num_ship, item_ship, count_item_ship, w_ship, adress_begin, phone_begin, time_ship, adress_end, phone_end, comment_ship) VALUES ('FBS', '{date_ship}', 0, 'Мебель', 'Не указано', 'Не указано', 'Аральская 47 (Мебельный цех)', '{phone_begin}', 'с 10:00 до 13:00', 'Электрозаводская 2А (Wildberries)', 'Нет номера', 'Успеть сдать до 18:00')", user)
                    create(f"REPLACE INTO shipping(type_ship, date_ship, num_ship, item_ship, count_item_ship, w_ship, adress_begin, phone_begin, time_ship, adress_end, phone_end, comment_ship) VALUES ('FBS', '{date_ship}', 0, 'Мебель', 'Не указано', 'Не указано', 'Аральская 47 (Мебельный цех)', '{phone_begin}', 'с 10:00 до 13:00', 'Карьерная 7 ст7 (OZON)', 'Нет номера', 'Успеть сдать до 13:00')", user)
                    create(f"REPLACE INTO work_ship_begin(date_work) VALUES ('{date_ship}')", user)
                list_log = selist(f"SELECT * FROM shipping WHERE date_ship = '{date_ship}' AND status_ship = 'В очереди'", user)
                await message.answer(text='<b>Начните распределение:</b>', reply_markup=markups.back_logistic)
                update(f"UPDATE users SET act_log = '100' WHERE id_user = '{user}'", user)
                update(f"UPDATE users SET count_logis = 0 WHERE id_user = '{user}'", user)
                for l in list_log:
                    inline_m = InlineKeyboardMarkup(row_width=2)
                    inline_m_b1 = InlineKeyboardButton(text='В очередь', callback_data=f'logis_{date_ship}_{l["id_ship"]}')
                    inline_m_b3 = InlineKeyboardButton(text='Перенос', callback_data=f'edite_{l["id_ship"]}')
                    inline_m_b2 = InlineKeyboardButton(text='Отменить', callback_data=f'logisnoyes_{l["id_ship"]}')
                    inline_m.add(inline_m_b1).add(inline_m_b3).add(inline_m_b2)
                    await message.answer(text=f'ID: *{l["id_ship"]}*\n'
                                              f'Тип: *{l["type_ship"]}*\n'
                                              f'Дата: *{l["date_ship"]}*\n'
                                              f'Время: *{l["time_ship"]}*\n'
                                              f'Предмет: *{l["item_ship"]}*\n'
                                              f'Количество: *{l["count_item_ship"]}*\n'
                                              f'Вес: *{l["w_ship"]}*\n\n'
                                              f'Телефон загрузки: `{l["phone_begin"]}`\n'
                                              f'Адрес загрузки: `{l["adress_begin"]}`\n'
                                              f'Телефон разгрузки: `{l["phone_end"]}`\n'
                                              f'Адрес разгрузки: `{l["adress_end"]}`\n'
                                              f'Комментарий: *{l["comment_ship"]}*\n', parse_mode='Markdown',
                                         reply_markup=inline_m)
            elif 'numd_' in selone(f"SELECT act_log FROM users WHERE id_user = '{user}'", user)['act_log']:
                if len(message.text.split('.')) == 3 and len(message.text) == 10:
                    list_chek = selist(f"SELECT * FROM shipping WHERE date_ship = '{message.text}'", user)

                    list_log = selist(f"SELECT * FROM shipping WHERE date_ship = '{message.text}' AND status_ship = 'В очереди'", user)
                    if selone(f"SELECT date_work FROM work_ship WHERE date_work = '{message.text}'", user) is None:
                        inline_phone = ReplyKeyboardMarkup(resize_keyboard=True)
                        inline_phone_b2 = '8-996-102-04-54 Ануар'
                        inline_phone_b4 = '8-995-948-29-00 Рахман'
                        menu_back_logistic = '❌ Отмена'
                        inline_phone.add(inline_phone_b2).add(inline_phone_b4).add(menu_back_logistic)
                        res = f'newz_{message.text}'
                        update(f"UPDATE users SET act_log = '{res}' WHERE id_user = '{user}'", user)
                        await message.answer(text='Выберите контакт на ФФ или введите иной:', reply_markup=inline_phone)
                    else:
                        await message.answer(text='<b>Очередь заявок на этот день:</b>', reply_markup=markups.back_logistic)
                        newlist = selist(f"SELECT * FROM shipping WHERE date_ship = '{message.text}'", user)
                        list_log = sorted(newlist, key=lambda d: d['num_ship'])
                        for l in list_log:
                            if l["status_ship"] == 'Отменен' or l["status_ship"] == 'Закончен':
                                await message.answer(text=f'ID: *{l["id_ship"]}*\n'
                                                          f'Тип: *{l["type_ship"]}*\n'
                                                          f'Дата: *{l["date_ship"]}*\n'
                                                          f'Время: *{l["time_ship"]}*\n'
                                                          f'Предмет: *{l["item_ship"]}*\n'
                                                          f'Количество: *{l["count_item_ship"]}*\n'
                                                          f'Вес: *{l["w_ship"]}*\n\n'
                                                          f'Телефон загрузки: `{l["phone_begin"]}`\n'
                                                          f'Адрес загрузки: `{l["adress_begin"]}`\n'
                                                          f'Телефон разгрузки: `{l["phone_end"]}`\n'
                                                          f'Адрес разгрузки: `{l["adress_end"]}`\n'
                                                          f'Комментарий: *{l["comment_ship"]}*\n\n'
                                                          f'Статус: *{l["status_ship"]}*', parse_mode='Markdown')
                            else:
                                inline_m = InlineKeyboardMarkup(row_width=2)
                                inline_m_b2 = InlineKeyboardButton(text='Отменить', callback_data=f'logisno_{l["id_ship"]}')
                                inline_m_b3 = InlineKeyboardButton(text='Перенос', callback_data=f'edite_{l["id_ship"]}')
                                inline_m.add(inline_m_b2).add(inline_m_b3)
                                await message.answer(text=f'ID: *{l["id_ship"]}*\n'
                                                          f'Тип: *{l["type_ship"]}*\n'
                                                          f'Дата: *{l["date_ship"]}*\n'
                                                          f'Время: *{l["time_ship"]}*\n'
                                                          f'Предмет: *{l["item_ship"]}*\n'
                                                          f'Количество: *{l["count_item_ship"]}*\n'
                                                          f'Вес: *{l["w_ship"]}*\n\n'
                                                          f'Телефон загрузки: `{l["phone_begin"]}`\n'
                                                          f'Адрес загрузки: `{l["adress_begin"]}`\n'
                                                          f'Телефон разгрузки: `{l["phone_end"]}`\n'
                                                          f'Адрес разгрузки: `{l["adress_end"]}`\n'
                                                          f'Комментарий: *{l["comment_ship"]}*\n\n'
                                                          f'Статус: *{l["status_ship"]}*', parse_mode='Markdown', reply_markup=inline_m)


                else:
                    await message.answer(text='Выберите другую дату')
            elif 'edite_' in selone(f"SELECT act_log FROM users WHERE id_user = '{user}'", user)['act_log']:
                callback_data = selone(f"SELECT act_log FROM users WHERE id_user = '{user}'", user)['act_log']
                list_call = callback_data.split('_')
                id_ship = list_call[1]
                if len(message.text.split('.')) == 3 and len(message.text) == 10:
                    delta_1 = datetime.timedelta(hours=5)
                    now = datetime.datetime.now() + delta_1

                    if ((int(message.text[0:2]) < int(now.day)) and (int(message.text[3:5]) == int(now.month))) or (
                            int(message.text[3:5]) < int(now.month)):
                        await message.answer(text='Вы можете указать дату начиная с сегодняшнего дня:')

                    elif (int(message.text[0:2]) == int(now.day)) and (int(sk.time_create()[0:2]) > 18):
                        await message.answer(text='На сегодня вы уже не можете создать заявку, укажите другую дату:')

                    else:
                        update(f"UPDATE users SET edit_log = ' ' WHERE id_user = '{user}'", user)
                        update(f"UPDATE users SET act_log = ' ' WHERE id_user = '{user}'", user)
                        update(f"UPDATE shipping SET date_ship = '{message.text}' WHERE id_ship = '{id_ship}'", user)
                        update(f"UPDATE shipping SET num_ship = 0 WHERE id_ship = '{id_ship}'", user)
                        update(f"UPDATE shipping SET status_ship = 'В очереди' WHERE id_ship = '{id_ship}'", user)

                        l = selist(f"SELECT * FROM shipping WHERE id_ship = '{id_ship}'", user)[0]

                        list_all_users = selist(f"SELECT * FROM users", user)
                        list_user = []
                        for us in list_all_users:
                            if 'log' in us['notif']:
                                list_user.append(us)
                        for user1 in list_user:
                            try:
                                chat_id = str(user1["id_user"])
                                destination_bot = Bot(token='6490496152:AAHnBwfDRlUTyTFMOMGGCK6Eu3WejYpesIE')
                                await destination_bot.send_message(chat_id, f'Изменилась дата у заявки с ID: {id_ship}!\n\n'
                                                                            f'Тип: *{l["type_ship"]}*\n'
                                                                            f'Дата: *{l["date_ship"]}*\n'
                                                                            f'Время: *{l["time_ship"]}*\n'
                                                                            f'Предмет: *{l["item_ship"]}*\n'
                                                                            f'Количество: *{l["count_item_ship"]}*\n'
                                                                            f'Вес: *{l["w_ship"]}*\n\n'
                                                                            f'Телефон загрузки: `{l["phone_begin"]}`\n'
                                                                            f'Адрес загрузки: `{l["adress_begin"]}`\n'
                                                                            f'Телефон разгрузки: `{l["phone_end"]}`\n'
                                                                            f'Адрес разгрузки: `{l["adress_end"]}`\n'
                                                                            f'Комментарий: *{l["comment_ship"]}*\n\n'
                                                                            f'Статус: *{l["status_ship"]}*')
                            except:
                                pass

                        await message.answer(text='Дата изменена!', reply_markup=markups.menu_log_n)

            # Редактировать
            elif message.text == markups.menu_logistic_b5:
                update(f"UPDATE users SET act_log = 'edit_' WHERE id_user = '{user}'", user)
                await message.answer(text='Введите ID заявки:', reply_markup=markups.back_logistic)
            elif 'edit_' in selone(f"SELECT act_log FROM users WHERE id_user = '{user}'", user)['act_log']:
                if message.text.isdigit():
                    list_chek = selist(f"SELECT * FROM shipping WHERE id_ship = '{int(message.text)}'", user)
                    if len(list_chek) != 0:
                        update(f"UPDATE users SET act_log = ' ' WHERE id_user = '{user}'", user)
                        l = list_chek[0]
                        inline_m = InlineKeyboardMarkup(row_width=2)
                        inline_m_b1 = InlineKeyboardButton(text='Редактировать', callback_data=f'logisedit_{l["id_ship"]}')
                        inline_m.add(inline_m_b1)
                        await message.answer(text=f'ID: *{l["id_ship"]}*\n'
                                                  f'Тип: *{l["type_ship"]}*\n'
                                                  f'Дата: *{l["date_ship"]}*\n'
                                                  f'Время: *{l["time_ship"]}*\n'
                                                  f'Предмет: *{l["item_ship"]}*\n'
                                                  f'Количество: *{l["count_item_ship"]}*\n'
                                                  f'Вес: *{l["w_ship"]}*\n\n'
                                                  f'Телефон загрузки: `{l["phone_begin"]}`\n'
                                                  f'Адрес загрузки: `{l["adress_begin"]}`\n'
                                                  f'Телефон разгрузки: `{l["phone_end"]}`\n'
                                                  f'Адрес разгрузки: `{l["adress_end"]}`\n'
                                                  f'Комментарий: *{l["comment_ship"]}*\n', parse_mode='Markdown', reply_markup=inline_m)
                    else:
                        await message.answer(text=f'Заявки с таким ID не найдено. Введите другой ID', parse_mode='Markdown')
                else:
                    await message.answer(text=f'Введите ID числом!', parse_mode='Markdown')
            elif 'logised_' in selone(f"SELECT edit_log FROM users WHERE id_user = '{user}'", user)['edit_log']:
                callback_data = selone(f"SELECT edit_log FROM users WHERE id_user = '{user}'", user)['edit_log']
                list_call = callback_data.split('_')
                val_edit = list_call[1]
                id_ship = list_call[2]

                inline_m = InlineKeyboardMarkup(row_width=2)
                inline_m_b8 = InlineKeyboardButton(text='⬅️ Назад', callback_data=f'logisedit_{id_ship}')
                inline_m.add(inline_m_b8)

                if val_edit == 'дата':
                    if len(message.text.split('.')) == 3 and len(message.text) == 10:
                        delta_1 = datetime.timedelta(hours=5)
                        now = datetime.datetime.now() + delta_1

                        if ((int(message.text[0:2]) < int(now.day)) and (int(message.text[3:5]) == int(now.month))) or (
                                int(message.text[3:5]) < int(now.month)):
                            await message.answer(text='Вы можете указать дату начиная с сегодняшнего дня:',
                                                 reply_markup=inline_m)

                        elif (int(message.text[0:2]) == int(now.day)) and (int(sk.time_create()[0:2]) > 18):
                            await message.answer(text='На сегодня вы уже не можете создать заявку, укажите другую дату:',
                                                 reply_markup=inline_m)

                        else:
                            update(f"UPDATE users SET edit_log = ' ' WHERE id_user = '{user}'", user)
                            update(f"UPDATE shipping SET date_ship = '{message.text}' WHERE id_ship = '{id_ship}'", user)

                            l = selist(f"SELECT * FROM shipping WHERE id_ship = '{id_ship}'", user)[0]
                            inline_m = InlineKeyboardMarkup(row_width=2)
                            inline_m_b1 = InlineKeyboardButton(text='Редактировать', callback_data=f'logisedit_{l["id_ship"]}')
                            inline_m.add(inline_m_b1)
                            await message.answer(text=f'ID: *{l["id_ship"]}*\n'
                                                      f'Тип: *{l["type_ship"]}*\n'
                                                      f'Дата: *{l["date_ship"]}*\n'
                                                      f'Время: *{l["time_ship"]}*\n'
                                                      f'Предмет: *{l["item_ship"]}*\n'
                                                      f'Количество: *{l["count_item_ship"]}*\n'
                                                      f'Вес: *{l["w_ship"]}*\n\n'
                                                      f'Адрес загрузки: *{l["adress_begin"]}*\n'
                                                      f'Адрес разгрузки: *{l["adress_end"]}*\n'
                                                      f'Комментарий: *{l["comment_ship"]}*\n\n'
                                                      f'Статус: *{l["status_ship"]}*', parse_mode='Markdown', reply_markup=inline_m)


                elif val_edit == 'время':
                    update(f"UPDATE users SET edit_log = ' ' WHERE id_user = '{user}'", user)
                    update(f"UPDATE shipping SET time_ship = '{message.text}' WHERE id_ship = '{id_ship}'", user)

                    l = selist(f"SELECT * FROM shipping WHERE id_ship = '{id_ship}'", user)[0]
                    inline_m = InlineKeyboardMarkup(row_width=2)
                    inline_m_b1 = InlineKeyboardButton(text='Редактировать', callback_data=f'logisedit_{l["id_ship"]}')
                    inline_m.add(inline_m_b1)
                    await message.answer(text=f'ID: *{l["id_ship"]}*\n'
                                              f'Тип: *{l["type_ship"]}*\n'
                                              f'Дата: *{l["date_ship"]}*\n'
                                              f'Время: *{l["time_ship"]}*\n'
                                              f'Предмет: *{l["item_ship"]}*\n'
                                              f'Количество: *{l["count_item_ship"]}*\n'
                                              f'Вес: *{l["w_ship"]}*\n\n'
                                              f'Адрес загрузки: *{l["adress_begin"]}*\n'
                                              f'Адрес разгрузки: *{l["adress_end"]}*\n'
                                              f'Комментарий: *{l["comment_ship"]}*\n\n'
                                              f'Статус: *{l["status_ship"]}*', parse_mode='Markdown', reply_markup=inline_m)

                elif val_edit == 'количество':
                    if message.text.isdigit():
                        if int(message.text) > 0:
                            update(f"UPDATE users SET edit_log = ' ' WHERE id_user = '{user}'", user)
                            update(f"UPDATE shipping SET count_item_ship = '{message.text}' WHERE id_ship = '{id_ship}'", user)

                            l = selist(f"SELECT * FROM shipping WHERE id_ship = '{id_ship}'", user)[0]
                            inline_m = InlineKeyboardMarkup(row_width=2)
                            inline_m_b1 = InlineKeyboardButton(text='Редактировать', callback_data=f'logisedit_{l["id_ship"]}')
                            inline_m.add(inline_m_b1)
                            await message.answer(text=f'ID: *{l["id_ship"]}*\n'
                                                      f'Тип: *{l["type_ship"]}*\n'
                                                      f'Дата: *{l["date_ship"]}*\n'
                                                      f'Время: *{l["time_ship"]}*\n'
                                                      f'Предмет: *{l["item_ship"]}*\n'
                                                      f'Количество: *{l["count_item_ship"]}*\n'
                                                      f'Вес: *{l["w_ship"]}*\n\n'
                                                      f'Адрес загрузки: *{l["adress_begin"]}*\n'
                                                      f'Адрес разгрузки: *{l["adress_end"]}*\n'
                                                      f'Комментарий: *{l["comment_ship"]}*\n\n'
                                                      f'Статус: *{l["status_ship"]}*', parse_mode='Markdown', reply_markup=inline_m)
                        else:
                            await message.answer(text='Количество должно быть больше нуля:')
                    else:
                        await message.answer(text='Количество должно быть числом:')

                elif val_edit == 'вес':
                    update(f"UPDATE users SET edit_log = ' ' WHERE id_user = '{user}'", user)
                    update(f"UPDATE shipping SET w_ship = '{message.text}' WHERE id_ship = '{id_ship}'", user)

                    l = selist(f"SELECT * FROM shipping WHERE id_ship = '{id_ship}'", user)[0]
                    inline_m = InlineKeyboardMarkup(row_width=2)
                    inline_m_b1 = InlineKeyboardButton(text='Редактировать', callback_data=f'logisedit_{l["id_ship"]}')
                    inline_m.add(inline_m_b1)
                    await message.answer(text=f'ID: *{l["id_ship"]}*\n'
                                              f'Тип: *{l["type_ship"]}*\n'
                                              f'Дата: *{l["date_ship"]}*\n'
                                              f'Время: *{l["time_ship"]}*\n'
                                              f'Предмет: *{l["item_ship"]}*\n'
                                              f'Количество: *{l["count_item_ship"]}*\n'
                                              f'Вес: *{l["w_ship"]}*\n\n'
                                              f'Адрес загрузки: *{l["adress_begin"]}*\n'
                                              f'Адрес разгрузки: *{l["adress_end"]}*\n'
                                              f'Комментарий: *{l["comment_ship"]}*\n\n'
                                              f'Статус: *{l["status_ship"]}*', parse_mode='Markdown', reply_markup=inline_m)
                elif val_edit == 'адресз':
                    update(f"UPDATE users SET edit_log = ' ' WHERE id_user = '{user}'", user)
                    update(f"UPDATE shipping SET adress_begin = '{message.text}' WHERE id_ship = '{id_ship}'", user)

                    l = selist(f"SELECT * FROM shipping WHERE id_ship = '{id_ship}'", user)[0]
                    inline_m = InlineKeyboardMarkup(row_width=2)
                    inline_m_b1 = InlineKeyboardButton(text='Редактировать', callback_data=f'logisedit_{l["id_ship"]}')
                    inline_m.add(inline_m_b1)
                    await message.answer(text=f'ID: *{l["id_ship"]}*\n'
                                              f'Тип: *{l["type_ship"]}*\n'
                                              f'Дата: *{l["date_ship"]}*\n'
                                              f'Время: *{l["time_ship"]}*\n'
                                              f'Предмет: *{l["item_ship"]}*\n'
                                              f'Количество: *{l["count_item_ship"]}*\n'
                                              f'Вес: *{l["w_ship"]}*\n\n'
                                              f'Адрес загрузки: *{l["adress_begin"]}*\n'
                                              f'Адрес разгрузки: *{l["adress_end"]}*\n'
                                              f'Комментарий: *{l["comment_ship"]}*\n\n'
                                              f'Статус: *{l["status_ship"]}*', parse_mode='Markdown', reply_markup=inline_m)
                elif val_edit == 'адреср':
                    update(f"UPDATE users SET edit_log = ' ' WHERE id_user = '{user}'", user)
                    update(f"UPDATE shipping SET adress_end = '{message.text}' WHERE id_ship = '{id_ship}'", user)

                    l = selist(f"SELECT * FROM shipping WHERE id_ship = '{id_ship}'", user)[0]
                    inline_m = InlineKeyboardMarkup(row_width=2)
                    inline_m_b1 = InlineKeyboardButton(text='Редактировать', callback_data=f'logisedit_{l["id_ship"]}')
                    inline_m.add(inline_m_b1)
                    await message.answer(text=f'ID: *{l["id_ship"]}*\n'
                                              f'Тип: *{l["type_ship"]}*\n'
                                              f'Дата: *{l["date_ship"]}*\n'
                                              f'Время: *{l["time_ship"]}*\n'
                                              f'Предмет: *{l["item_ship"]}*\n'
                                              f'Количество: *{l["count_item_ship"]}*\n'
                                              f'Вес: *{l["w_ship"]}*\n\n'
                                              f'Адрес загрузки: *{l["adress_begin"]}*\n'
                                              f'Адрес разгрузки: *{l["adress_end"]}*\n'
                                              f'Комментарий: *{l["comment_ship"]}*\n\n'
                                              f'Статус: *{l["status_ship"]}*', parse_mode='Markdown', reply_markup=inline_m)
                elif val_edit == 'коммент':
                    update(f"UPDATE users SET edit_log = ' ' WHERE id_user = '{user}'", user)
                    update(f"UPDATE shipping SET comment_ship = '{message.text}' WHERE id_ship = '{id_ship}'", user)

                    l = selist(f"SELECT * FROM shipping WHERE id_ship = '{id_ship}'", user)[0]
                    inline_m = InlineKeyboardMarkup(row_width=2)
                    inline_m_b1 = InlineKeyboardButton(text='Редактировать', callback_data=f'logisedit_{l["id_ship"]}')
                    inline_m.add(inline_m_b1)
                    await message.answer(text=f'ID: *{l["id_ship"]}*\n'
                                              f'Тип: *{l["type_ship"]}*\n'
                                              f'Дата: *{l["date_ship"]}*\n'
                                              f'Время: *{l["time_ship"]}*\n'
                                              f'Предмет: *{l["item_ship"]}*\n'
                                              f'Количество: *{l["count_item_ship"]}*\n'
                                              f'Вес: *{l["w_ship"]}*\n\n'
                                              f'Адрес загрузки: *{l["adress_begin"]}*\n'
                                              f'Адрес разгрузки: *{l["adress_end"]}*\n'
                                              f'Комментарий: *{l["comment_ship"]}*\n\n'
                                              f'Статус: *{l["status_ship"]}*', parse_mode='Markdown', reply_markup=inline_m)

            # Добавить водителя
            elif selone(f"SELECT new_name_user FROM users WHERE id_user = '{user}'", user)['new_name_user'] == 100:
                update(f"UPDATE users SET new_name_user = 0 WHERE id_user = '{user}'", user)
                update(f"UPDATE users SET name_new_user = '{message.text}' WHERE id_user = '{user}'", user)
                await message.answer(text='Выберите должность сотрудника:', reply_markup=markups.inline_add_dr)
            elif selone(f"SELECT new_id_user FROM users WHERE id_user = '{user}'", user)['new_id_user'] == 100:
                if message.text.isdigit():
                    update(f"UPDATE users SET new_id_user = 0 WHERE id_user = '{user}'", user)
                    update(f"UPDATE users SET new_id_user_text = '{message.text}' WHERE id_user = '{user}'", user)
                    update(f"UPDATE users SET new_name_user = 100 WHERE id_user = '{user}'", user)
                    await message.answer("Введите Фамилию и Имя сотрудника")
                else:
                    await message.answer(text='Пришлите <b>id</b> сотрудника числом:')
            elif message.text == markups.menu_logistic_b3:
                update(f"UPDATE users SET new_id_user = 100 WHERE id_user = '{user}'", user)
                await message.answer(
                    "Пришлите <b>id</b> сотрудника <i>(для того, чтобы узнать его, сотрудник должен написать боту команду /info)</i>", )
                await message.answer(text="Для возврата нажмите 'Отмена'", reply_markup=markups.back_logistic)

            # Удалить вадителя
            elif selone(f"SELECT remove_user FROM users WHERE id_user = '{user}'", user)['remove_user'] == 100:
                if message.text.isdigit():
                    check = 0
                    search = selist(f"SELECT id_user, name_user FROM users WHERE company = 'Водитель'", user)
                    for i in search:
                        if int(message.text) == int(i['id_user']):
                            check = 1
                    if check == 1:
                        update(f"UPDATE users SET remove_user = 0 WHERE id_user = '{user}'", user)
                        update(f"DELETE FROM users WHERE id_user = '{message.text}'", user)
                        await message.answer("Сотрудник удален", reply_markup=markups.menu_logistic)
                    else:
                        await message.answer(
                            text='Сотрудник с таким ID не найден!\nПришлите корректный <b>id</b> сотрудника:')
                else:
                    await message.answer(text='Пришлите <b>id</b> сотрудника числом:')
            elif message.text == markups.menu_logistic_b4:
                update(f"UPDATE users SET remove_user = 100 WHERE id_user = '{user}'", user)
                search = selist(f"SELECT id_user, name_user, company FROM users WHERE company = 'Водитель'", user)
                res = ''
                for i in search:
                    res += str(i['id_user']) + " - "
                    res += i['name_user'] + "\n"
                await message.answer(res)
                await message.answer('Введите ID сотрудника, которого хотите удалить')
                await message.answer(text="Для возврата нажмите 'Отмена'", reply_markup=markups.back_logistic)

            # Не понятно
            else:
                await message.answer(text='Я вас не понял', reply_markup=markups.menu_admin)



if __name__ == '__main__':
    executor.start_polling(db, on_startup=startup, skip_updates=True)