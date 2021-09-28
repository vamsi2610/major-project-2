from telegram.ext import Updater, MessageHandler, Filters
from Adafruit_IO import Client

import os
 
client_name=os.getenv('client_name')
client_api=os.getenv('client_api')
 
aio=Client(client_name,client_api)
 
def light_on(bot,update):
  chat_id = bot.message.chat_id
  bot.message.reply_text('Turning on Lights')
  aio.send('light ',1)

def light_off(bot,update):
   chat_id = bot.message.chat_id
   bot.message.reply_text('Turning off the Lights')
   aio.send('light ',0)
 
def fan_on(bot,update):
  chat_id = bot.message.chat_id
  bot.message.reply_text('Fan is turned ON')
  aio.send('fan ',1)

def fan_off(bot,update):
  chat_id = bot.message.chat_id
  bot.message.reply_text('Fan is turned OFF')
  aio.send('fan ',0)

def main(bot,update):
  a= bot.message.text
  if a =="turn on the lights":
    light_on(bot,update)
  elif a=="turn off the lights":
    light_off(bot,update)
  elif a=="turn on the fan":
    fan_on(bot,update)
  elif a=="turn off the fan":
    fan_off(bot,update)
bot_token = '2022287894:AAGj9lfHmvhtAogZYY2Lrfkg_q6E6HvykL4'
u = Updater(bot_token,use_context=True)
dp = u.dispatcher
dp.add_handler(MessageHandler(Filters.text,main))
u.start_polling()
u.idle()
