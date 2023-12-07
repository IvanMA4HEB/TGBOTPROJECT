# TGBOTPROJECT
Данный телеграмм-бот предназначен для музыкальных коллективов, дающих концертов.
Бот помогает оптимизировать процесс разработки расписания выступлений.
Участникам он предоставляет расписание, а разработчику ответы участников.

ЗАПУСК НА ЛОКАЛЬНОЙ МАШИНЕ

Чтобы запустить бота на локальной машине, необходимо вставить id бота в телеграмм,
а затем запустить код бота в среде предназначенной для Python.
Ссылка на бота [https://t.me/rpck_band_bot]

КАК ПОЛЬЗОВАТЬСЯ БОТОМ

1. При запуске бота необходимо написать "Привет"
2. После необходимо написат команду "/schedule"
3. Перейдя по ссылке и ознакомившись с расписанием, необходимо нажать одну из кнопок
"Да" или "Нет"
4. После нажатия на кнопку "Нет" необходимо написать команду "/report"
5. После нужно написать номер пункта, который вас не устраивает в расписании, и нажать на кнопку "Enter"

КОД БОТА
from telebot import types
import telebot;
bot = telebot.TeleBot('6310172647:AAHqMz4bMl8jK3a6Oc5rdBzKFIwLg9sjk8g');
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, наш разработчик составил новое расписание выступлений, чтобы его увидеть напиши команду /schedule")
    elif message.text == "/schedule":
      keyboard = types.InlineKeyboardMarkup(); #наша клавиатура
      key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes'); #кнопка «Да»
      keyboard.add(key_yes); #добавляем кнопку в клавиатуру
      key_no= types.InlineKeyboardButton(text='Нет', callback_data='no');
      keyboard.add(key_no);
      question = 'Вот дащборд с расписанием [https://700c-188-130-255-192.ngrok-free.app ]. Тебя оно устраивает?';
      bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
    elif message.text == '/report':
            bot.send_message(message.from_user.id, "Напиши пожалуйста номер того, что тебя не устраивает.");
    elif message.text == '1' or '2' or '3' or '4' or '5' or '6' or '7':
            bot.send_message(message.from_user.id, 'Я зафиксировал и отправил твои пожелания разработчику.');
            bot.reply_to(message,"Этот пункт не устраивает пользователя.");
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /schedule.")

    @bot.callback_query_handler(func=lambda call: True)
    def callback_worker(call):
        if call.data == "yes":
            bot.send_message(call.message.chat.id, 'Отлично! Я отправлю твой ответ разработчику.');
            bot.send_message(1944402724, 'Пользователя устраивает расписание');
        elif call.data == "no":
            ...
            bot.send_message(call.message.chat.id, 'Напиши команду /report')
   

bot.polling(none_stop=True, interval=0)

КОНТАКТНАЯ ИНФОРМАЦИЯ

GitHub [https://github.com/IvanMA4HEB]
Email [primerpochty2000@gmail.com]