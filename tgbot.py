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
      question = 'Вот дащборд с расписанием [https://1a82-188-130-255-192.ngrok-free.app/ ]. Тебя оно устраивает?';
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
