import telebot
from telebot.types import InputFile

TOKEN = "YOUR_TOKEN_HERE"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(msg):
    bot.reply_to(msg, "Salom! MP3 yuklab beruvchi bot tayyor.")

@bot.message_handler(content_types=['photo'])
def photo_handler(msg):
    bot.reply_to(msg, "Rasm oldim! Tez orada style qo‘shish funksiyasi qo‘shiladi.")

@bot.message_handler(commands=['mp3'])
def mp3_cmd(msg):
    try:
        audio = InputFile('audio.mp3')
        bot.send_audio(msg.chat.id, audio)
    except:
        bot.reply_to(msg, "audio.mp3 topilmadi.")

bot.infinity_polling()
