import telebot
from telebot import types

TOKEN = "7672272547:AAFN6vMIVXO6W09r1DYtmf2IFtFSKx0Sqf0"
bot = telebot.TeleBot(TOKEN)

# Main Menu
def main_menu():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Convert Model")
    btn2 = types.KeyboardButton("Model from Image")
    btn3 = types.KeyboardButton("Model from Text")
    btn4 = types.KeyboardButton("Set Model Quality")
    keyboard.add(btn1, btn2, btn3)
    keyboard.add(btn4)
    return keyboard

# Quality Menu
def quality_menu():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("High Quality")
    btn2 = types.KeyboardButton("Medium Quality")
    btn3 = types.KeyboardButton("Low Quality")
    back = types.KeyboardButton("Back to Menu")
    keyboard.add(btn1, btn2, btn3)
    keyboard.add(back)
    return keyboard

@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(message.chat.id, "Welcome to Doji 3D Bot!", reply_markup=main_menu())

@bot.message_handler(func=lambda m: m.text == "Set Model Quality")
def quality_handler(message):
    bot.send_message(message.chat.id, "Choose model quality:", reply_markup=quality_menu())

@bot.message_handler(func=lambda m: m.text in ["High Quality", "Medium Quality", "Low Quality"])
def set_quality_handler(message):
    quality = message.text
    bot.send_message(message.chat.id, f"Model quality set to: {quality}", reply_markup=main_menu())

@bot.message_handler(func=lambda m: m.text == "Convert Model")
def convert_model_handler(message):
    bot.send_message(message.chat.id, "Please upload your 3D model file (OBJ, FBX, GLTF)...")

@bot.message_handler(func=lambda m: m.text == "Model from Image")
def model_from_image_handler(message):
    bot.send_message(message.chat.id, "Please upload an image to generate a 3D model...")

@bot.message_handler(func=lambda m: m.text == "Model from Text")
def model_from_text_handler(message):
    bot.send_message(message.chat.id, "Please enter a description for the 3D model...")

@bot.message_handler(func=lambda m: m.text == "Back to Menu")
def back_to_menu(message):
    bot.send_message(message.chat.id, "Returning to main menu...", reply_markup=main_menu())

@bot.message_handler(func=lambda m: True)
def default_handler(message):
    bot.send_message(message.chat.id, "Invalid command! Please use the buttons.", reply_markup=main_menu())

if __name__ == "__main__":
    bot.polling()
