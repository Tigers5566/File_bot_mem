import telebot
import os
from telebot import types
import random
bot = telebot.TeleBot("Украли)")

@bot.message_handler(commands=['meme'])
def send_mem(message):     
    markup = types.InlineKeyboardMarkup(row_width=3)
    button1 = types.InlineKeyboardButton("Мемы про программистов", callback_data="mem_programmer")
    button2 = types.InlineKeyboardButton("Мемы про геймеров", callback_data="mem_gamer")
    button3 = types.InlineKeyboardButton("Мемы про школу", callback_data="mem_school")
    markup.add(button1, button2, button3)
    bot.send_message(message.chat.id, "Какой мем ты хочешь увидеть?", reply_markup=markup)
    
  


@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    if call.message:
        if call.data == "mem_programmer":
            its_meme = ["mem_for_gamer/meme_1.jpeg", "mem_for_gamer/meme_2.jpeg", "mem_for_gamer/meme_3.jpeg"]
            img_name = (random.choice(its_meme))
            with open(f'images/{img_name}', 'rb') as f:  
                bot.send_photo(call.message.chat.id, f)
        elif call.data == "mem_gamer":
            its_meme = ["mem_for_programmer/Mem_for_gamer.jpeg", "mem_for_programmer/Mem_for_gamer2.jpeg", "mem_for_programmer/Mem_for_gamer3.jpeg"]
            img_name = (random.choice(its_meme))
            with open(f'images/{img_name}', 'rb') as f:  
                bot.send_photo(call.message.chat.id, f)
        elif call.data == "mem_school":
            its_meme = ["mem_for_school/Mem_for_school.jpeg", "mem_for_school/Mem_for_school2.jpeg", "mem_for_school/Mem_for_school3.jpeg"]
            img_name = (random.choice(its_meme))
            with open(f'images/{img_name}', 'rb') as f:  
                bot.send_photo(call.message.chat.id, f)
        
bot.infinity_polling()

    
