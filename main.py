from telebot import TeleBot

TOKEN = "1978637966:AAEPdNu56x34fz2SsVFlwx6ceS2bnXRA-9A"

bot = TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def command_start(message):
	bot.reply_to(message,"Salom botga xush kelibsiz,")
	
	
bot.polling()