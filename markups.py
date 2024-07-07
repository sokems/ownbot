from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

menu_main = '🗓 Главное меню'
menu_main_count = '🗄 Главное меню'
menu_back_main = 'Отмена ❌'
menu_back_retail = 'Отмена 🛑'
menu_back_count = 'Отмена ⭕️'
menu_back_count_retail = 'Отмена 🧨'
menu_back_logistic = '❌ Отмена'
menu_back_set = '🧨 Отмена'

main_menu = ReplyKeyboardMarkup(resize_keyboard=True)
main_menu.add(menu_main)

menu_admin = ReplyKeyboardMarkup(resize_keyboard=True)
menu_admin_b2 = 'РИТЕЙЛ ПЛЮС'
menu_admin_b3 = 'Мебельное производство'
menu_admin_b4 = 'Логистика'
menu_admin_b5 = 'Настройки'
menu_admin.add(menu_admin_b2).add(menu_admin_b3).add(menu_admin_b4).add(menu_admin_b5)

menu_set_admin = ReplyKeyboardMarkup(resize_keyboard=True)
menu_set_admin_b1 = '🔔 Уведомления'
menu_set_admin_b2 = '🔄 Обновить базу данных'
menu_set_admin.add(menu_set_admin_b2).add(menu_set_admin_b1).add(menu_main)

menu_logistic = ReplyKeyboardMarkup(resize_keyboard=True)
menu_logistic_b1 = '🚛 Создать заявку'
menu_logistic_b2 = '🚀 Маршрутный лист'
menu_logistic_b3 = '🚚 Добавить водителя'
menu_logistic_b4 = '🚨 Удалить водителя'
menu_logistic_b5 = '✏️ Редактировать'
menu_logistic_b6 = '📦 Заявки на доставку'
menu_logistic_b7 = '⭐️ Заявки на забор'
menu_logistic.add(menu_logistic_b1, menu_logistic_b2).add(menu_logistic_b6, menu_logistic_b7).add(menu_logistic_b3, menu_logistic_b4).add(menu_logistic_b5, menu_main)

menu_count = ReplyKeyboardMarkup(resize_keyboard=True)
menu_count_b1 = '🥇 Добавить сотрудника'
menu_count_b2 = '🔥 Удалить сотрудника'
menu_count_b3 = '📓 Список сотрудников'
menu_count_b5 = '🪓 Цех'
menu_count_b6 = '🗯 Написать сообщение сотрудникам'
menu_count.add(menu_count_b5).add(menu_count_b1, menu_count_b2).add(menu_count_b3, menu_count_b6).add(menu_main)

menu_count_retail = ReplyKeyboardMarkup(resize_keyboard=True)
menu_count_retail_b = ReplyKeyboardMarkup(resize_keyboard=True)
menu_count_retail_n = ReplyKeyboardMarkup(resize_keyboard=True)
menu_count_retail_b1 = '🧰 Остаток'
menu_count_retail_b2 = '🚛 Прибыло'
menu_count_retail_b3 = '🚚 Уехало'
menu_count_retail_b6 = '⭐️ Сделано'
menu_count_retail_b4 = '🔒 Закрыть смену'
menu_count_retail_b5 = '🔐 Открыть смену'
menu_count_retail_b7 = '🚚 Отправки'
menu_count_retail_b8 = '😡 Брак'
menu_count_retail_b9 = '🌙 Ночная смена'
menu_count_retail.add(menu_count_retail_b7, menu_count_retail_b8).add(menu_count_retail_b1, menu_count_retail_b6).add(menu_count_retail_b2, menu_count_retail_b3).add(menu_count_retail_b9, menu_count_retail_b5).add(menu_main_count)
menu_count_retail_n.add(menu_count_retail_b7, menu_count_retail_b8).add(menu_count_retail_b1, menu_count_retail_b6).add(menu_count_retail_b2, menu_count_retail_b3).add(menu_count_retail_b9, menu_count_retail_b4).add(menu_main_count)
menu_count_retail_b.add(menu_count_retail_b9, menu_count_retail_b7).add(menu_count_retail_b5).add(menu_main_count)

menu_retail = ReplyKeyboardMarkup(resize_keyboard=True)
menu_retail_b2 = '🔴 Расход'
menu_retail_b3 = '💳 Реквизиты'
menu_retail_b4 = '🚀 Сменить план'
menu_retail_b6 = '📝 CRM'
menu_retail_b8 = '💢 Подтвердить расход'
menu_retail_b9 = '📦 Возвраты'
menu_retail.add(menu_retail_b6, menu_retail_b4).add(menu_retail_b3 ,menu_retail_b9).add(menu_retail_b2, menu_retail_b8).add(menu_main)

menu_none = ReplyKeyboardMarkup(resize_keyboard=True)
menu_none_b1 = '...'
menu_none.add(menu_none_b1)

inline_add_dr = InlineKeyboardMarkup(row_width=1)
inline_add_dr_b1 = InlineKeyboardButton(text='Водитель', callback_data='add_dr')
inline_add_dr.add(inline_add_dr_b1)

inline_add_user_retail = InlineKeyboardMarkup(row_width=1)
inline_add_user_retail_b1 = InlineKeyboardButton(text='Управляющий РИТЕЙЛ', callback_data='add_retail_adm')
inline_add_user_retail.add(inline_add_user_retail_b1)

inline_del_user_retail = InlineKeyboardMarkup(row_width=1)
inline_del_user_retail_b1 = InlineKeyboardButton(text='Управляющий РИТЕЙЛ', callback_data='del_retail_adm')
inline_del_user_retail.add(inline_del_user_retail_b1)

inline_add_user_count = InlineKeyboardMarkup(row_width=1)
inline_add_user_count_b2 = InlineKeyboardButton(text='Мастер', callback_data='add_count_mas')
inline_add_user_count_b3 = InlineKeyboardButton(text='Сборщик', callback_data='add_count_sbor')
inline_add_user_count.add(inline_add_user_count_b2).add(inline_add_user_count_b3)

inline_del_user_count = InlineKeyboardMarkup(row_width=1)
inline_del_user_count_b1 = InlineKeyboardButton(text='Управление складом', callback_data='del_count_adm')
inline_del_user_count.add(inline_del_user_count_b1)


back_main = ReplyKeyboardMarkup(resize_keyboard=True)
back_main.add(menu_back_main)

back_retail = ReplyKeyboardMarkup(resize_keyboard=True)
back_retail.add(menu_back_retail)

back_count = ReplyKeyboardMarkup(resize_keyboard=True)
back_count.add(menu_back_count)

back_set = ReplyKeyboardMarkup(resize_keyboard=True)
back_set.add(menu_back_set)

back_count_retail = ReplyKeyboardMarkup(resize_keyboard=True)
back_count_retail.add(menu_back_count_retail)

back_logistic = ReplyKeyboardMarkup(resize_keyboard=True)
back_logistic.add(menu_back_logistic)

inline_cat = InlineKeyboardMarkup(row_width=1)
inline_cat_b1 = InlineKeyboardButton(text='Аренда', callback_data='cat_arenda')
inline_cat_b2 = InlineKeyboardButton(text='ФОТ', callback_data='cat_fot')
inline_cat_b3 = InlineKeyboardButton(text='Расходники', callback_data='cat_rash')
inline_cat_b4 = InlineKeyboardButton(text='Логистика', callback_data='cat_logist')
inline_cat_b5 = InlineKeyboardButton(text='Инструменты', callback_data='cat_instr')
inline_cat_b6 = InlineKeyboardButton(text='Прочее', callback_data='cat_other')
inline_cat_b7 = InlineKeyboardButton(text='Аутсорс', callback_data='cat_outs')
inline_cat.add(inline_cat_b1).add(inline_cat_b2).add(inline_cat_b3).add(inline_cat_b4).add(inline_cat_b5).add(inline_cat_b6).add(inline_cat_b7)

inline_pay = InlineKeyboardMarkup(row_width=1)
inline_pay_b1 = InlineKeyboardButton(text='Карта Фархат', callback_data='pay_fara')
inline_pay_b2 = InlineKeyboardButton(text='p/c ООО (Альфа банк)', callback_data='pay_kay')
inline_pay_b3 = InlineKeyboardButton(text='p/c ООО (Тинькофф)', callback_data='pay_ooo')
inline_pay_b4 = InlineKeyboardButton(text='р/с ИП Истяков (Тинькофф)', callback_data='pay_ipfara')
inline_pay_b5 = InlineKeyboardButton(text='р/с ИП Калимуллин (Тинькофф)', callback_data='pay_ipkay')
inline_pay_b6 = InlineKeyboardButton(text='р/с ИП Калимуллин (Ozon)', callback_data='pay_ozok')
inline_pay_b7 = InlineKeyboardButton(text='р/с ООО (Ozon)', callback_data='pay_ozooo')
inline_pay_b8 = InlineKeyboardButton(text='РН-Карт', callback_data='pay_rn')
inline_pay_b9 = InlineKeyboardButton(text='Авито', callback_data='pay_avito')
inline_pay_b10 = InlineKeyboardButton(text='Модуль Банк', callback_data='pay_modbank')
inline_pay.add(inline_pay_b1).add(inline_pay_b2).add(inline_pay_b3).add(inline_pay_b4).add(inline_pay_b5).add(inline_pay_b6).add(inline_pay_b7).add(inline_pay_b8).add(inline_pay_b9).add(inline_pay_b10)

inline_pay_3 = InlineKeyboardMarkup(row_width=1)
inline_pay_3_b1 = InlineKeyboardButton(text='Продолжить', callback_data='pay_nonepay')
inline_pay_3.add(inline_pay_3_b1)

inline_done = InlineKeyboardMarkup(row_width=1)
inline_done_b1 = InlineKeyboardButton(text='Да', callback_data='donepay_yes')
inline_done_b2 = InlineKeyboardButton(text='Нет', callback_data='donepay_no')
inline_done.add(inline_done_b1).add(inline_done_b2)
