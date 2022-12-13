import telebot
import requests
import time
from random import randint 
bot = telebot.TeleBot("5817446788:AAEJ6D2hLdomr7Q9GT79a0zy8Uw0w8bioFY", parse_mode=None)

number = None
task1 = False
# task1 = Задача 1. Добавьте telegram-боту возможность вычислять выражения:
# 1 + 4 * 2 -> 9
task2 = False
# task2 = Задача 2. Добавьте в бота игру «Угадай числа». Бот загадывает число от 1 до 1000. Когда
# игрок угадывает его, бот выводит количество сделанных ходов.

@bot.message_handler(content_types=['text'])
def hello_user(message):
    global task1, task2, number
    # global task2
    # global number
    if task1:
        bot.reply_to(message, eval(message.text))
        task1 = False
    elif task2:
        if message.text.isdigit():
            input_number = int(message.text)
            if input_number > number:
                bot.send_message(message.chat.id, 'Ваше число больше заданного')
            elif input_number < number:
                bot.send_message(message.chat.id, 'Ваше число меньше заданного')
            else:
                bot.send_message(message.chat.id, f'Поздравляю! Вы угадали число {number}')
                task2 = False
        else:
            bot.send_message(message.from_user.id, 'Это не число!')
    else:
        if 'привет' in message.text:
            bot.reply_to(message, 'привет, ' + message.from_user.first_name)
        elif message.text == 'погода':
            r = requests.get('https://wttr.in/?0T')
            bot.send_message(message.chat.id, r.text)
            # bot.reply_to(message, r.text)
        elif message.text == 'котик':
            r = f'https://cataas.com/cat?t=${time.time()}'
            bot.send_photo(message.chat.id, r)
        elif message.text == 'вычислить' or message.text == 'Задача 1' or message.text == 'задача 1':
            task1 = True
            bot.reply_to(message, 'Задайте выражение')
        elif message.text == 'игра' or message.text == 'Задача 2' or message.text == 'задача 2':
            task2 = True
            number = randint(1, 1000)
            bot.reply_to(message, f'Угадайте число от 1 до 1000, ({number}). Введите число')

@bot.message_handler(commands=['start', 'help', 'hello'])
def send_welcome(message):
    print(message)
    bot.reply_to(message, "Howdy, how are you doing?")

bot.infinity_polling()
