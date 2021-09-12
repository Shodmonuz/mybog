from telebot import TeleBot
from num2words import num2words
TOKEN = "1978637966:AAEPdNu56x34fz2SsVFlwx6ceS2bnXRA-9A"

bot = TeleBot(TOKEN)
azolar = 0
azolarid = []
@bot.message_handler(commands=["start"])
def command_start(message):
	bot.reply_to(message,"Salom botga xush kelibsiz, Menga raqam yuboring.")
	if message.chat.id in azolarid:
	  azolarid.append(message.chat.id)
	  azolar += 1
	  
@bot.message_handler()
def habar(message):
  try:
    bot.reply_to(message,num2words(message.text))
  except:
    bot.reply_to(message,'Iltimos raqam yuboring')
	if message.chat.id=639390974:
	  if message.text='Statistika':
	    bot.reply_to(message,f"👥Barcha azolar soni {azolar}")
	  
	  
	  
bot.polling()