import random
import telebot 
import os
from botlogic import flipcoin
bot = telebot.TeleBot("")

tasks = []

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, f'Привет! Я бот {bot.get_me().first_name}! Напиши /help')

@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = """
Доступные команды:
/start - начать
/help - помощь
/dice - Бросить кубик
/random - Случайное число
/coin - бросить монетку
/hello - поздороваться
/bye - попрощаться
/heh - хех
    """
    bot.reply_to(message, help_text)

@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")

@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands=['coin'])
def send_coin(message):
    coin = flipcoin()
    bot.reply_to(message, f" выпала монетка  : {coin}")
 
@bot.message_handler(commands=['heh'])
def send_heh(message):
        try: 
             count_heh = int(message.text.split()[1])
        except:
            (IndexError, ValueError)
        count_heh = 5

@bot.message_handler(commands=['dice'])
def roll_dice(message):
    dice = random.randint(1, 6)
    bot.reply_to(message, f" Выпало: {dice}")

@bot.message_handler(commands=['random'])
def random_number(message):
    if len(message.text.split()) > 2:
        try:
            firstn = int(message.text.split()[1])
            endn = int(message.text.split()[2])
            num = random.randint(firstn, endn)
            bot.reply_to(message, f" Случайное число: {num}")
        except:
            bot.reply_to(message, "Напиши: /random 1 100")

@bot.message_handler(commands=['password'])
def generate_password(message):
    length=int(input("Сколько символов должно быть в пароле:"))
    while length == 0:
        print("нельзя 0 символов")
    else:
        x= "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
        password += random.choice(x)
        bot.reply_to(message, f" Сгенерирован пароль: `{password}`", )

@bot.message_handler(commands=['mem'])
def send_mem(message):
    randimage = random.choice(os.listdir('images'))
    with open(f'images/{randimage}', 'rb') as f: 
        bot.send_photo(message.chat.id, f)


@bot.message_handler(func=lambda message: True)         
def echo_all(message):
    bot.reply_to(message, message.text)


bot.polling()
