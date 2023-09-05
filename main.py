import telebot
import sympy
import random

from telebot import types

bot = telebot.TeleBot('5116204495:AAGWOEaLji9mqwkB2u0qfSGyFXm-eeEE50E')


# @bot.message_handler(commands=['start'])
# def welcome(message):
#     sti = open('static/welcome.webp', 'rb')
#     bot.send_sticker(message.chat.id, sti)
#
#     # keyboard
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     item1 = types.KeyboardButton("🎲 Рандомное число")
#     item2 = types.KeyboardButton("😊 Как дела?")
#
#     markup.add(item1, item2)
#
#     bot.send_message(message.chat.id,
#                      "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы быть подопытным кроликом.".format(
#                          message.from_user, bot.get_me()),
#                      parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def lalala(message):
    try:
        if message.chat.type == 'private':

            if message.text == '/start':
                bot.send_message(message.chat.id, 'ХАЙ')
                return

            x, y = sympy.symbols('x y')

            usertext = message.text.split('\n')

            xi = usertext[0].split('=')
            eta = usertext[1].split('=')
            enterux = usertext[2].split('=')
            enteruy = usertext[3].split('=')
            enteruxx = usertext[4].split('=')
            enteruyy = usertext[5].split('=')
            enteruxy = usertext[6].split('=')

            xix = sympy.diff(xi[1], x)
            xixx = sympy.diff(xix, x)
            xiy = sympy.diff(xi[1], y)
            xiyy = sympy.diff(xiy, y)
            etax = sympy.diff(eta[1], x)
            etaxx = sympy.diff(etax, x)
            etay = sympy.diff(eta[1], y)
            etayy = sympy.diff(etay, y)
            etaxy = sympy.diff(etay, x)
            xixy = sympy.diff(xiy, x)

            xixy, xix, xiy, xiyy = str(xixy), str(xix), str(xiy), str(xiyy)
            etax, etaxx, etay, etayy = str(etax), str(etaxx), str(etay), str(etayy)
            etaxy, xixy = str(etaxy), str(xixy)

            dicfun = {'*log(e)': ''}

            for key in dicfun.keys():
                xixy = xixy.replace(key, dicfun[key])
                xix = xix.replace(key, dicfun[key])
                xiy = xiy.replace(key, dicfun[key])
                xiyy = xiyy.replace(key, dicfun[key])
                etax = etax.replace(key, dicfun[key])
                etaxx = etaxx.replace(key, dicfun[key])
                etay = etay.replace(key, dicfun[key])
                etayy = etayy.replace(key, dicfun[key])
                etaxy = etaxy.replace(key, dicfun[key])
                xixy = xixy.replace(key, dicfun[key])

            bot.send_message(message.chat.id, f'ξx={xix}\nξy={xiy}\n')
            bot.send_message(message.chat.id, f'ηx={etax}\nηy={etay}\n')
            bot.send_message(message.chat.id, f'ξxx={xixx}\nξyy={xiyy}\n')
            bot.send_message(message.chat.id, f'ηxx={etaxx}\nηyy={etayy}\n')
            bot.send_message(message.chat.id, f'ξxy={xixy}\nηxy={etaxy}\n')

            dicvar = {'a': 'Uξ', 'b': 'Uη', 'g': 'Uξη', 'd': 'Uξξ', 'f': 'Uηη'}

            ux = sympy.simplify(f'a*{xix} + b*{etax}')
            uy = sympy.simplify(f'a*{xiy} + b*{etay}')
            uxx = sympy.simplify(
                f'd*{xix}*{xix} + 2*g*{xix}*{etax} + f*{etax}*{etax} + a*{xixx} + b*{etaxx}')
            uxy = sympy.simplify(
                f'd*{xix}*{xiy} + g*({xix}*{etay} + {xiy}*{etax}) + f*{etax}*{etay} + a*{xixy} + b*{etaxy}')
            uyy = sympy.simplify(
                f'd*{xiy}*{xiy} + 2*g*{xiy}*{etay} + f*{etay}*{etay} + a*{xiyy} + b*{etayy}')

            ux = str(ux)
            uy = str(uy)
            uyy = str(uyy)
            uxx = str(uxx)
            uxy = str(uxy)

            equat = sympy.simplify(
                f'{enterux[1]}*({ux}) + {enteruy[1]}*({uy}) + {enteruxx[1]}*({uxx}) + {enteruyy[1]}*({uyy}) + {enteruxy[1]}*({uxy})')

            equat = str(equat)

            for key in dicvar.keys():
                ux = ux.replace(key, dicvar[key])
                uy = uy.replace(key, dicvar[key])
                uxx = uxx.replace(key, dicvar[key])
                uxy = uxy.replace(key, dicvar[key])
                uyy = uyy.replace(key, dicvar[key])
                equat = equat.replace(key, dicvar[key])

            bot.send_message(message.chat.id, f'Ux={ux}\nUy={uy}\nUxx={uxx}\nUyy={uyy}\nUxy={uxy}\n')
            bot.send_message(message.chat.id, f'Подстановка: {equat}')

            # if message.text == '🎲 Рандомное число':
            #     bot.send_message(message.chat.id, str(random.randint(0, 100)))
            # elif message.text == '😊 Как дела?':
            #
            #     markup = types.InlineKeyboardMarkup(row_width=2)
            #     item1 = types.InlineKeyboardButton("Хорошо", callback_data='good')
            #     item2 = types.InlineKeyboardButton("Не очень", callback_data='bad')
            #
            #     markup.add(item1, item2)
            #
            #     bot.send_message(message.chat.id, 'Отлично, сам как?', reply_markup=markup)
            # else:
            #     bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')

    except Exception as e:
        bot.send_message(message.chat.id, 'непон')


# @bot.callback_query_handler(func=lambda call: True)
# def callback_inline(call):
#     try:
#         if call.message:
#             if call.data == 'good':
#                 bot.send_message(call.message.chat.id, 'Вот и отличненько 😊')
#             elif call.data == 'bad':
#                 bot.send_message(call.message.chat.id, 'Бывает 😢')
#
#             # remove inline buttons
#             bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="😊 Как дела?",
#                                   reply_markup=None)
#
#             # show alert
#             bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
#                                       text="ЭТО ТЕСТОВОЕ УВЕДОМЛЕНИЕ!!11")
#
#     except Exception as e:
#         print(repr(e))


# RUN
bot.polling(none_stop=True)