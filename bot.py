
import telebot 
from botlogic import flipcoin
# Замени 'TOKEN' на токен твоего бота
# Этот токен ты получаешь от BotFather, чтобы бот мог работать
bot = telebot.TeleBot("8078515996:AAET-v43OmT3ptiy98AoMUYN3Dehf_e_PuI")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, f'Привет! Я бот {bot.get_me().first_name}!')

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


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.polling()