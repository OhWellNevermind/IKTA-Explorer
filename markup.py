from gc import callbacks
from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
# ---Main menu button---
btnMain = KeyboardButton(text='Головне Меню', callback_data="mainMenu")

# ---Main menu---
btnVns = KeyboardButton(text='ВНС', callback_data="vns")
btnStudent = KeyboardButton(text='Студент НУЛП', callback_data="studentprofile")
btnHostels = KeyboardButton(text='Гуртожитки', callback_data="hostels")
btnKampus = KeyboardButton(text='Корпуси', callback_data="campus")
btnSocial = KeyboardButton(text='Соціальні мережі', callback_data="sn")
btnTeacher = KeyboardButton(text='Викладачі', callback_data="teacher")
btnSticker = KeyboardButton(text='Стікери',callback_data ="stickers")
btnCalculator = KeyboardButton(text='Калькулятор',callback_data="calculator")
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(
    btnVns, btnStudent, btnHostels, btnKampus, btnSocial,btnTeacher,btnSticker, btnCalculator)

# ---Hostels menu---
btnHostel1 = KeyboardButton(text='Гуртожиток 1', callback_data='hostle_1')
btnHostel3 = KeyboardButton(text='Гуртожиток 3', callback_data='hostle_3')
btnHostel4 = KeyboardButton(text='Гуртожиток 4', callback_data='hostle_4')
btnHostel5 = KeyboardButton(text='Гуртожиток 5', callback_data='hostle_5')
btnHostel7 = KeyboardButton(text='Гуртожиток 7', callback_data='hostle_7')
btnHostel8 = KeyboardButton(text='Гуртожиток 8', callback_data='hostle_8')
btnHostel9 = KeyboardButton(text='Гуртожиток 9', callback_data='hostle_9')
btnHostel10 = KeyboardButton(text='Гуртожиток 10', callback_data='hostle_10')
btnHostel11 = KeyboardButton(text='Гуртожиток 11', callback_data='hostle_11')
btnHostel12 = KeyboardButton(text='Гуртожиток 12', callback_data='hostle_12')
btnHostel14 = KeyboardButton(text='Гуртожиток 14', callback_data='hostle_14')
btnHostel15 = KeyboardButton(text='Гуртожиток 15', callback_data='hostle_15')
btnHostel17 = KeyboardButton(text='Гуртожиток 17', callback_data='hostle_17')
hostelsMenu = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(
    btnHostel1, btnHostel3, btnHostel4, btnHostel5, btnHostel7, btnHostel8, btnHostel9, btnHostel10, btnHostel11, btnHostel12, btnHostel14, btnHostel15, btnHostel17, btnMain)

itembtn1 = types.KeyboardButton('Результат')
itembtn2 = types.KeyboardButton('Продовжити')
markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(itembtn1,itembtn2)
