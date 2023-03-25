import telebot
from telebot import types

bot = telebot.TeleBot('5876097484:AAEE_QLwtEuz9y3evezKatSwlZkTeGh4WjQ')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn1 = types.KeyboardButton('Оформить заказ✅')
    btn2 = types.KeyboardButton('Посчитать стоимость💴')
    btn3 = types.KeyboardButton('Подобрать размер📏')
    btn4 = types.KeyboardButton('Скачать каталог🗂')
    btn5 = types.KeyboardButton('FAQ❓')
    btn6 = types.KeyboardButton('Другой вопрос⁉️')
    btn7 = types.KeyboardButton('Поддержка💬')
    btn8 = types.KeyboardButton('Наш Инстаграм📲')
    btn9 = types.KeyboardButton('Остановить бота⛔️')
    markup.row(btn1, btn2, btn3)
    markup.row(btn4, btn5, btn6)
    markup.row(btn7, btn8, btn9)
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}! Какой у тебя вопрос?', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def order(message):
    if message.chat.type == 'private':
        if message.text == 'Оформить заказ✅':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=9, one_time_keyboard=True)
            btn1 = types.KeyboardButton('Да✅')
            btn2 = types.KeyboardButton('Нет✖️')
            back = types.KeyboardButton('🔙Назад')
            markup.add(btn1, btn2, back)
            # markup = types.InlineKeyboardMarkup()
            # markup.add(types.InlineKeyboardButton('Да', callback_data='Да'))
            # markup.add(types.InlineKeyboardButton('Нет', callback_data='Нет'))
            bot.send_message(message.chat.id, f'{message.from_user.first_name}, ты выбрал(а) товар который хочешь заказать?', reply_markup=markup)

        elif message.text == 'Да✅':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=9, one_time_keyboard=True)
            btn1 = types.KeyboardButton('Да✔️')
            btn2 = types.KeyboardButton('Нет😬')
            back = types.KeyboardButton('🔙Назад')
            markup.add(btn1, btn2, back)
            bot.send_message(message.chat.id, f'{message.from_user.first_name}, ты знаешь полную стоимость cвоего товара в рублях?', reply_markup=markup)

            
        elif message.text == 'Нет😬':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=9, one_time_keyboard=True)
            back = types.KeyboardButton('🔙Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Жми назад и переходи в раздел Посчитать стоимость💴' , reply_markup=markup)

        
        elif message.text == 'Да✔️':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=9, one_time_keyboard=True)
            btn1 = types.KeyboardButton('Сбербанк')
            btn2 = types.KeyboardButton('Газпромбанк')
            btn3 = types.KeyboardButton('ВТБ')
            btn4 = types.KeyboardButton('Райффайзен банк')
            btn5 = types.KeyboardButton('Тинькофф')
            back = types.KeyboardButton('🔙Назад')
            markup.add(btn1, btn2, btn3)
            markup.add(btn4, btn5, back)
            bot.send_message(message.chat.id, 'Если готов(а) оплачивать, выбери банк на который удобно совершить платёж.', reply_markup=markup)

        elif message.text == 'Нет✖️':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=9, one_time_keyboard=True)
            back = types.KeyboardButton('🔙Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Жми назад и переходи в раздел Скачать каталог🗂', reply_markup=markup)


        elif message.text == 'Сбербанк':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=9, one_time_keyboard=True)
            back = types.KeyboardButton('🔙Назад')
            paid = types.KeyboardButton('Оплатил(а)')
            markup.add(paid, back)
            bot.send_message(message.chat.id, 'Оплата по номеру телефона: 89778480013', reply_markup=markup)
            bot.send_message(message.chat.id, 'Оплата по номеру карты: 4276400035973222', reply_markup=markup)
            bot.send_message(message.chat.id, 'Получатель Глеб Михайлович Ш.', reply_markup=markup)
            
        elif message.text == 'Газпромбанк':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=9, one_time_keyboard=True)
            back = types.KeyboardButton('🔙Назад')
            paid = types.KeyboardButton('Оплатил(а)')
            markup.add(paid, back)
            bot.send_message(message.chat.id, 'Оплата по номеру телефона: 89778480013', reply_markup=markup)
            bot.send_message(message.chat.id, 'Оплата по номеру карты: 4249175006061314', reply_markup=markup)
            bot.send_message(message.chat.id, 'Получатель Глеб Михайлович Ш.', reply_markup=markup)

        elif message.text == 'ВТБ':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=9, one_time_keyboard=True)
            back = types.KeyboardButton('🔙Назад')
            paid = types.KeyboardButton('Оплатил(а)')
            markup.add(paid, back)
            bot.send_message(message.chat.id, 'Оплата по номеру телефона: 89778480013', reply_markup=markup)
            bot.send_message(message.chat.id, 'Оплата по номеру карты: 4893470479049683', reply_markup=markup)
            bot.send_message(message.chat.id, 'Получатель Глеб Михайлович Ш.', reply_markup=markup)

        elif message.text == 'Райффайзен банк':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=9, one_time_keyboard=True)
            back = types.KeyboardButton('🔙Назад')
            paid = types.KeyboardButton('Оплатил(а)')
            markup.add(paid, back)
            bot.send_message(message.chat.id, 'Оплата по номеру телефона: 89778480013', reply_markup=markup)
            bot.send_message(message.chat.id, 'Оплата по номеру карты: 5379653046439996', reply_markup=markup)
            bot.send_message(message.chat.id, 'Получатель Глеб Михайлович Ш.', reply_markup=markup)

        elif message.text == 'Тинькофф':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=9, one_time_keyboard=True)
            back = types.KeyboardButton('🔙Назад')
            paid = types.KeyboardButton('Оплатил(а)')
            markup.add(paid, back)
            bot.send_message(message.chat.id, 'Оплата по номеру телефона: 89264232169', reply_markup=markup)
            bot.send_message(message.chat.id, 'Оплата по номеру карты: 5536913985255492', reply_markup=markup)
            bot.send_message(message.chat.id, 'Получатель Наталья Андреевна Б.', reply_markup=markup)
        
        elif message.text == 'Оплатил(а)':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=9, one_time_keyboard=True)
            back = types.KeyboardButton('🔙Назад')
            markup.add(back)
            bot.send_message(message.chat.id, f'Спасибо за заказ {message.from_user.first_name}! В течении 24-х часов мы пришлём тебе скриншот об успешном заказе!', reply_markup=markup)
        
        elif message.text == 'Посчитать стоимость💴':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=9, one_time_keyboard=True)
            btn1 = types.KeyboardButton('☑️Да')
            btn2 = types.KeyboardButton('✖️Нет')
            back = types.KeyboardButton('🔙Назад')
            markup.add(btn1, btn2, back) 
            bot.send_message(message.chat.id, f'{message.from_user.first_name}, ты знаешь стоимость твоего товара в юанях?', reply_markup=markup)

        elif message.text == '☑️Да':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=9, one_time_keyboard=True)
            back = types.KeyboardButton('🔙Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Напиши точную сумму в юанях в чат и я посчитаю стоимость товара в рублях вместе с доставкой и комиссией', reply_markup=markup)
            
        
        elif message.text == '✖️Нет':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=9, one_time_keyboard=True)
            back = types.KeyboardButton('🔙Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Жми назад и переходи в раздел FAQ❓' , reply_markup=markup)

        elif message.text == 'Подобрать размер📏':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=9, one_time_keyboard=True)
            btn1 = types.KeyboardButton('Adidas')
            btn2 = types.KeyboardButton('Nike')
            btn3 = types.KeyboardButton('Jordan')
            btn4 = types.KeyboardButton('New Balance')
            btn5 = types.KeyboardButton('GGDB')
            back = types.KeyboardButton('🔙Назад')
            markup.add(btn1, btn2, btn3)
            markup.add(btn4, btn5, back)
            bot.send_message(message.chat.id, 'Размерная сетка какого бренда тебе интересна?', reply_markup=markup)

        elif message.text == 'Adidas':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=9, one_time_keyboard=True)
            back = types.KeyboardButton('🔙Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Отправил размерую сетку Adidas, помни что лучше всего выбирать размер по сантиметрам!' , reply_markup=markup)

        elif message.text == 'Nike':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=9, one_time_keyboard=True)
            back = types.KeyboardButton('🔙Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Отправил размерую сетку Nike, помни что лучше всего выбирать размер по сантиметрам!' , reply_markup=markup)

        elif message.text == 'Jordan':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=9, one_time_keyboard=True)
            back = types.KeyboardButton('🔙Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Отправил размерую сетку Jordan, помни что лучше всего выбирать размер по сантиметрам!' , reply_markup=markup)

        elif message.text == 'New Balance':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=9, one_time_keyboard=True)
            back = types.KeyboardButton('🔙Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Отправил размерую сетку New Balance, помни что лучше всего выбирать размер по сантиметрам!' , reply_markup=markup)

        elif message.text == 'GGDB':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=9, one_time_keyboard=True)
            back = types.KeyboardButton('🔙Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Отправил размерую сетку GGDB, помни что лучше всего выбирать размер по сантиметрам!' , reply_markup=markup)

        elif message.text == 'Скачать каталог🗂':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=9, one_time_keyboard=True)
            back = types.KeyboardButton('🔙Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'https://apps.apple.com/app/id1012871328' , reply_markup=markup)

        elif message.text == 'Наш Инстаграм📲':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=9, one_time_keyboard=True)
            back = types.KeyboardButton('🔙Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'https://instagram.com/resell__space' , reply_markup=markup)

        elif message.text == '🔙Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            btn1 = types.KeyboardButton('Оформить заказ✅')
            btn2 = types.KeyboardButton('Посчитать стоимость💴')
            btn3 = types.KeyboardButton('Подобрать размер📏')
            btn4 = types.KeyboardButton('Скачать каталог🗂')
            btn5 = types.KeyboardButton('FAQ❓')
            btn6 = types.KeyboardButton('Другой вопрос⁉️')
            btn7 = types.KeyboardButton('Поддержка💬')
            btn8 = types.KeyboardButton('Наш Инстаграм📲')
            btn9 = types.KeyboardButton('Остановить бота⛔️')
            markup.row(btn1, btn2, btn3)
            markup.row(btn4, btn5, btn6)
            markup.row(btn7, btn8, btn9)
            bot.send_message(message.chat.id, f'Какой у тебя вопрос?', reply_markup=markup)



# @bot.message_handler(commands=['order'])
# def start(message):
#     markup = types.InlineKeyboardMarkup())
#     markup.add(types.InlineKeyboardButton('Да', callback_data='order'))
#     markup.add(types.InlineKeyboardButton('Нет', callback_data='order'))
#     bot.send_message(message.chat.id, f'{message.from_user.first_name}, ты выбрал(а) товар который хочешь заказать?', reply_markup=markup)
    

# @bot.message_handler(commands=['price'])
# def price(message)::
#     markup = types.InlineKeyboardMarkup()
#     markup.add(types.InlineKeyboardButton('Да', callback_data='order'))
#     markup.add(types.InlineKeyboardButton('Нет', callback_data='order'))
#     bot.send_message(message.chat.id, f'{message.from_user.first_name}, ты знаешь стоимость твоего товара в юанях?')
#
# @bot.message_handler(commands=['size'])
# def start(message):
#     markup = types.InlineKeyboardMarkup()
#     markup.add(types.InlineKeyboardButton('Да', callback_data='order'))
#     markup.add(types.InlineKeyboardButton('Нет', callback_data='order'))
#     bot.send_message(message.chat.id, f'{message.from_user.first_name}, ты знаешь свой размер обуви в US или в сантиметрах?')

# @bot.message_handler(commands=['poizon'])
# def poizon(message):
#     bot.send_message(message.chat.id, 'https://apps.apple.com/app/id1012871328')

# @bot.message_handler(commands=['faq'])
# def start(message):
#     bot.send_message(message.chat.id, 'Выбери какой вопрос тебя интересует')

# @bot.message_handler(commands=['other'])
# def start(message):
#     bot.send_message(message.chat.id, 'Если ты не нашёл(ла), ответа на свой вопрос из /faq, то спроси меня прмо в чате!')

# @bot.message_handler(commands=['operator'])
# def start(message):
#     bot.send_message(message.chat.id, 'Переключаю на оператора!')

# @bot.message_handler(commands=['instagram'])
# def start(message):
#     bot.send_message(message.chat.id, 'https://instagram.com/resell__space')

# @bot.message_handler(commands=['stop'])
# def start(message):
#     bot.send_message(message.chat.id, 'f')

# @bot.message_handler()
# def start(message):
#     if message.text.lower() == 'позвать оператора':
#         bot.reply_to(message, '/operator')
#     elif message.text.lower() == 'позвать специалиста':
#         bot.reply_to(message, '/operator')
#     elif message.text.lower() == 'как долго идет доставка':
#         bot.reply_to(message, '/faq')
#     elif message.text.lower() == 'как отследить посылку':
#         bot.reply_to(message, 'Напиши оператору и он предоставит вам трек номер!')
#     elif message.text.lower() == 'куда переводить?':
#         bot.reply_to(message, '/order')
 
# def order(message):
#     bot.send_message(message.chat.id, )

# @bot.message_handler(commands=['menu'])
# def menu(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
#     makeOrder = types.KeyboardButton('Оформить заказ')
#     start = types.KeyboardButton('Начать')

#     markup.add(makeOrder, start)
#     bot.send_message(message.chat.id, 'Выбери категорию', reply_markup=markup)



if __name__ == '__main__':
    bot.polling(non_stop=True)