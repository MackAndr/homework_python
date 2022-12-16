import telebot
import requests
import time
import io
from random import randint 
bot = telebot.TeleBot("5817446788:AAEJ6D2hLdomr7Q9GT79a0zy8Uw0w8bioFY", parse_mode=None)


task2 = False

@bot.message_handler(commands=['start', 'help', 'hello'])
def send_welcome(message):
    print(message)
    bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(content_types=['text'])
def hello_user(message):
    global task1, task2

    if task2:
        users_quests = str(message.from_user.id) + ' ' + str(message.from_user.first_name) + ' ' + str(message.text) + '\n'
        queste = open('users_questions.txt', 'a+', encoding='utf-8')
        try:
            lines3 = queste.readlines()
            print(users_quests)
            print(lines3)
            if users_quests not in lines3:
                queste.writelines(str(message.from_user.id) + ' ' + str(message.from_user.first_name) + ': ' + str(message.text) + '\n')
                bot.send_message(message.from_user.id, 'Ваш вопрос записан в users_questions.txt')
            else:
                bot.send_message(message.from_user.id, 'Ваш вопрос уже записан')
        except io.UnsupportedOperation:
            queste.writelines(str(message.from_user.id) + ' ' + str(message.from_user.first_name) + ': ' + str(message.text) + '\n')
            bot.send_message(message.from_user.id, 'Обращение записано в users_requets.txt')
        queste.close() 
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
        
        elif message.text == 'вопрос' or message.text == 'Задача 2' or message.text == 'задача 2':
            task2 = True
            bot.reply_to(message, f'Задайте боту вопрос: ')
            


        
        elif message.text == 'регистрация':
            user_id = str(message.from_user.id) + '\n'
            data = open('users.txt', 'r+', encoding='utf-8')
            try:
                lines = data.readlines()
                print(user_id)
                print(lines)
                if user_id not in lines:
                    data.writelines(str(message.from_user.id) + '\n')
                    bot.send_message(message.from_user.id, 'Регистрация прошла успешно')
                else:
                    bot.send_message(message.from_user.id, 'Данный аккаунт уже зарегистрирован')
            except io.UnsupportedOperation:
                data.writelines(str(message.from_user.id) + '\n')
                bot.send_message(message.from_user.id, 'Регистрация прошла успешно')
            data.close() 
        else:
            users_requests = str(message.from_user.id) + ' ' + str(message.from_user.first_name) + ' ' + str(message.text) + '\n'
            data2 = open('users_requets.txt', 'r+', encoding='utf-8')
            try:
                lines2 = data2.readlines()
                print(users_requests)
                print(lines2)
                if users_requests not in lines2:
                    data2.writelines(str(message.from_user.id) + ' ' + str(message.from_user.first_name) + ': ' + str(message.text) + '\n')
                    bot.send_message(message.from_user.id, 'Обращение записано в users_requets.txt')
                else:
                    bot.send_message(message.from_user.id, 'Данное обращение уже записнао')
            except io.UnsupportedOperation:
                data2.writelines(str(message.from_user.id) + ' ' + str(message.from_user.first_name) + ': ' + str(message.text) + '\n')
                bot.send_message(message.from_user.id, 'Обращение записано в users_requets.txt')
            data2.close() 


bot.infinity_polling()
