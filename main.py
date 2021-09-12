from telebot import TeleBot
from num2words import num2words
TOKEN = "1978637966:AAEPdNu56x34fz2SsVFlwx6ceS2bnXRA-9A"

bot = TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def command_start(message):
	bot.reply_to(message,"Salom botga xush kelibsiz, Menga raqam yuboring.")

@bot.message_handler()
def habar(message):
  try:
    bot.reply_to(message,num2words(message.text))
  except:
    bot.reply_to(message,'Iltimos raqam yuboring')
	
bot.polling()