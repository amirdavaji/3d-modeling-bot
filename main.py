
from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import os

API_TOKEN = '7672272547:AAFN6vMIVXO6W09r1DYtmf2IFtFSKx0Sqf0'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

keyboard = InlineKeyboardMarkup(row_width=2)
keyboard.add(
    InlineKeyboardButton("ساخت مدل سه‌بعدی", callback_data='make_model'),
    InlineKeyboardButton("ویرایش مدل", callback_data='edit_model'),
    InlineKeyboardButton("گرفتن شات از مدل", callback_data='screenshot'),
    InlineKeyboardButton("تبدیل فایل‌های مدل", callback_data='convert_model'),
    InlineKeyboardButton("تنظیم کیفیت", callback_data='set_quality')
)

quality_keyboard = InlineKeyboardMarkup(row_width=3)
quality_keyboard.add(
    InlineKeyboardButton("بالا", callback_data='quality_high'),
    InlineKeyboardButton("متوسط", callback_data='quality_medium'),
    InlineKeyboardButton("پایین", callback_data='quality_low')
)

@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message):
    await message.answer("به ربات مدل‌سازی دوجی خوش آمدید!", reply_markup=keyboard)

@dp.callback_query_handler(lambda c: True)
async def handle_callbacks(callback_query: types.CallbackQuery):
    data = callback_query.data
    if data == 'make_model':
        await callback_query.message.answer("لطفاً عکس یا توضیح متنی برای مدل‌سازی بفرستید.")
    elif data == 'edit_model':
        await callback_query.message.answer("فایل OBJ مدل و دستور ویرایش را ارسال کنید.")
    elif data == 'screenshot':
        await callback_query.message.answer("از کدام مدل شات گرفته شود؟ فایل OBJ را بفرستید.")
    elif data == 'convert_model':
        await callback_query.message.answer("لطفاً فایل مدل را ارسال کنید تا تبدیل شود.")
    elif data == 'set_quality':
        await callback_query.message.answer("لطفاً کیفیت مدل را انتخاب کنید:", reply_markup=quality_keyboard)
    elif data.startswith("quality_"):
        await callback_query.message.answer(f"کیفیت انتخاب شد: {data.split('_')[1]}")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
