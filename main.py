from email import message
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from inform import *
import markup as nav
import data as dt
import emoji

# Set Token in file named info.py
bot = Bot(token=TOKEN)
storage=MemoryStorage()
dp = Dispatcher(bot,storage=storage)

class TakeScores(StatesGroup):
    subject = State()
    scores = State()
    credit = State()
    alt_step = State()

subjects = list()
scores = list()
credits = list()

class Teachers(StatesGroup):
    last_name = State()

class Kampus(StatesGroup):
    number = State()

kampuses = {'1': 'link','2':'link2'}

kampuses_photo = {'1': 'link_for_photo','2':'link_for_photo2'}

@dp.message_handler(commands=['start'])
async def startCommand(message: types.Message):
    await message.reply(emoji.emojize("""
Привіт, студенте!
Ласкаво просимо до IKTA-Explorer!

<b>Що вміє цей бот?</b>

:round_pushpin: Швидка навігація по корпусах університету і студмістечку.

:mag_right: Пошук викладачів за прізвищем.

:bookmark_tabs: Структуровані посилання на соцмережі університету.

:memo: Автоматизований розрахунок рейтингового балу.

:computer: Посилання на ВНС.

:gift: Унікальні тематичні стікери.

Напиши /start, щоб розпочати роботу 
P.S. Обов’язково розповідай про нас своїм друзям :shushing_face:
    """, language='alias'),parse_mode="HTML", reply_markup=nav.mainMenu)


@dp.message_handler()
async def helpCommand(message: types.Message):
    # Main functions reply
    if message.text == "help":
        await bot.send_message(message.from_user.id, "Це перелік ресуррсів що тобі пропонуються на вибір", reply_markup=nav.mainMenu)
    elif message.text == 'Студент НУЛП':
        await bot.send_message(message.from_user.id, """
       Посилання на портал Студент НУЛП :\n https://student.lpnu.ua/  """, reply_markup=nav.mainMenu)
        await message.answer_photo('https://drive.google.com/file/d/1BhnrMQT2dRDQGI0jWLYq-cRv5JcjIDAN/view?usp=share_link')
    elif message.text == 'ВНС':
        await bot.send_message(message.from_user.id, """Віртуальне навчальне середовище (ВНС)- твій основий ресурс для виконання робіт, знаходження лекційного матеріалу :\n http://vns.lpnu.ua/
        """, reply_markup=nav.mainMenu)
        await message.answer_photo("https://drive.google.com/file/d/1wN0s0eHqFYKw5rGVrcbSeCEbEU3Udzx6/view?usp=share_link")
    elif message.text == 'Гуртожитки':
        await message.answer_photo("https://drive.google.com/file/d/1n_sx1yZuPsml-RHaXLkRTaYCEHY9CPjg/view?usp=share_link")
        await bot.send_message(message.from_user.id, """Вибери Гуртожиток:""", reply_markup=nav.hostelsMenu)
        
    elif message.text == 'Корпуси':
        await message.answer_photo("https://drive.google.com/file/d/1vv6mYa77oLK9KDL-mukSzyRJX4VNx2bH/view?usp=share_link")
        await message.reply("Введи номер корпусу:")
        await Kampus.number.set()   
    elif message.text == 'Викладачі':
        await message.answer_photo("https://drive.google.com/file/d/1H6pC6d5Z41vPGdaG6rLBRnXEFuvsB_rj/view?usp=share_link")
        await message.reply("Введи прізвище викладача:")
        await Teachers.last_name.set()
    elif message.text == 'Стікери':
        await message.answer_photo("https://drive.google.com/file/d/1ErbsuYBYfW2ujLkA_72pv7xXaOZg21MU/view?usp=share_link")
        await bot.send_message(message.from_user.id, emoji.emojize("""
    \n<a href="https://t.me/addstickers/iktaexplorer">IKTA Explorer</a> :bomb:  
    \n<a href="https://t.me/addstickers/based_quotes">How_Talk_in_NULP</a> :school_satchel: 
    """, language='alias'),parse_mode="HTML",  reply_markup=nav.mainMenu)
        
    # Reply Hostels
    #SUCCESS
    elif message.text == 'Гуртожиток 1':
        await bot.send_location(message.from_user.id, "49.8288113","24.0175364", reply_markup=nav.hostelsMenu)
        await message.answer_photo('https://drive.google.com/file/d/1uDuze4G27t4P_2mqayQJOjpyj_lP50ie/view?usp=share_link')
    #SUCCESS
    elif message.text == 'Гуртожиток 3':
        await bot.send_location(message.from_user.id, "49.8296352","24.0157652", reply_markup=nav.hostelsMenu)
        await message.answer_photo('https://drive.google.com/file/d/139gRCGvt1vLY_aeKIzA8BMA-WfI_oCLn/view?usp=share_link')
    elif message.text == 'Гуртожиток 4':
        await bot.send_location(message.from_user.id, "49.8236164","24.0132401", reply_markup=nav.hostelsMenu)
        await message.answer_photo('https://drive.google.com/file/d/1MWR7B9uagMc0nPQeCtiCQZy6O2o4VN5S/view?usp=sharing')
    elif message.text == 'Гуртожиток 5':
        await bot.send_location(message.from_user.id, "49.8264939","24.0128066", reply_markup=nav.hostelsMenu)
        await message.answer_photo('https://media.lpnu.ua/system/files/styles/photo_watermark/private/photo/2017/dec/04/02/gurt08252016082.jpg?itok=t0aPCq9j')
    #SUCCESS
    elif message.text == 'Гуртожиток 7':
        await bot.send_location(message.from_user.id, "49.8279839","24.0142475", reply_markup=nav.hostelsMenu)
        await message.answer_photo('https://drive.google.com/file/d/1zWXKZPkhGvV0XvV-3TuetA3-CceYPrM0/view?usp=share_link')
    #SUCCESS
    elif message.text == 'Гуртожиток 8':
        await bot.send_location(message.from_user.id, "49.8245075","24.0120803", reply_markup=nav.hostelsMenu)
        await message.answer_photo('https://drive.google.com/file/d/1rJ6yXd1pQ0oHCl4QNeYdM5gKqSc6Bs1x/view?usp=share_link')
    #SUCCESS
    elif message.text == 'Гуртожиток 9':
        await bot.send_location(message.from_user.id, "49.8285511","24.0157886", reply_markup=nav.hostelsMenu)
        await message.answer_photo('https://drive.google.com/file/d/1s7TVr_vYRVBlpkp4dMw9Lt9E1I8XYr1B/view?usp=share_link')
    #SUCCESS
    elif message.text == 'Гуртожиток 10':
        await bot.send_location(message.from_user.id, "49.8246399","24.013808", reply_markup=nav.hostelsMenu)
        await message.answer_photo('https://drive.google.com/file/d/1JzUvWeQot6_CNPkQSUxqnusyNUo9faTx/view?usp=share_link')
    #SUCCESS
    elif message.text == 'Гуртожиток 11':
        await bot.send_location(message.from_user.id, "49.825896","24.012377", reply_markup=nav.hostelsMenu)
        await message.answer_photo('https://drive.google.com/file/d/1hKqXRtvBM3eKExWDuSo3gdrb89I4o9bS/view?usp=share_link')
    #SUCCESS
    elif message.text == 'Гуртожиток 12':
        await bot.send_location(message.from_user.id, "49.8168266","24.0111546", reply_markup=nav.hostelsMenu)
        await message.answer_photo('https://drive.google.com/file/d/1ySxjXeKmMr7JQDxtHjZkg2OZQPutYiE2/view?usp=share_link')
    #SUCCESS
    elif message.text == 'Гуртожиток 14':
        await bot.send_location(message.from_user.id,"49.81755065018007", "24.01184216930707")
        await message.answer_photo('https://drive.google.com/file/d/1KzrimieA53wVEaekXutxxFo_0PAJz-lF/view?usp=sharing')
    elif message.text == 'Гуртожиток 15':
        await bot.send_location(message.from_user.id, "49.8178711","24.0131052", reply_markup=nav.hostelsMenu)
        await message.answer_photo('http://photos.wikimapia.org/p/00/02/85/58/90_full.jpg')
    #SUCCESS
    elif message.text == 'Гуртожиток 17':
        await bot.send_location(message.from_user.id, "49.8003","23.9947877", reply_markup=nav.hostelsMenu)
        await message.answer_photo('https://drive.google.com/file/d/1dP_eBtlf4MGA0IfC51UyRCVYAKW5XpKq/view?usp=share_link')
    elif message.text == 'Головне Меню':
        await bot.send_message(message.from_user.id, """Повертаємося в головне меню!!!""", reply_markup=nav.mainMenu)
    # Social Networks reply
    elif message.text == 'Соціальні мережі':
        
        await message.answer_photo("https://drive.google.com/file/d/1PgY1wMWyOeaHbqoRs0SwTJHj-rC5WPK-/view?usp=share_link")
        await bot.send_message(message.from_user.id, emoji.emojize(
           """
Офіційні канали НУЛП 
<a href="https://facebook.com/lvivpolytechnic">Facebook</a> :mortar_board:
<a href="https://instagram.com/lpnu_official">Instagram</a> :camera:
<a href="https://www.linkedin.com/school/lviv-polytechnic-national-university">Linkedin</a> :briefcase: 
<a href="https://twitter.com/LvPolytechnic">Twitter</a>:bird: 
<a href="https://t.me/lpnu_official">Telegram NULP</a> 
Соцмережі ІКТА
<a href="https://tiktok.com/@lpnu_official">Tik Tok</a> :video_camera:
<a href="https://youtube.com/channel/UCYC38Wwv1IsozuymZitUKrw">You Tube</a> :movie_camera: 
<a href="https://t.me/nulp_wiki">Wiki NULP</a>:globe_with_meridians:
<a href="https://t.me/profikta">Telegram IKTA</a> :gift_heart: 
<a href="https://t.me/students_nulp">Колегія та профком студентів і аспірантів НУ “ЛП”</a> :mortar_board:
<a href="https://t.me/nulp_ikta">Телеграм чат студентів ІКТА</a> :school_satchel: 
Чати спеціальностей
    <a href="https://t.me/nulp_mt">МТ</a>:signal_strength: 
    <a href="https://t.me/nulp_kb">КБ</a> :computer: 
    <a href="https://t.me/nulp_ki">КІ</a> :iphone: 
    <a href="https://t.me/iot_nulp2021">ІР</a> :earth_americas: 
""", language='alias'),parse_mode="HTML",disable_web_page_preview=True ,reply_markup=nav.mainMenu)
        
    #Grades calculator
    elif message.text == 'Калькулятор':
        await message.answer_photo("https://drive.google.com/file/d/1OK757q7deiV8RR-8mLI7sX2vOJR98JRD/view?usp=share_link")
        markup = types.ReplyKeyboardRemove(selective=False)
        await bot.send_message(message.from_user.id, message.from_user.first_name + '!')
        await bot.send_message(message.from_user.id, 'Нумо розрахуємо твій бал!')
        await bot.send_message(message.from_user.id, 'Введи назву предмета...')
        await TakeScores.subject.set()

    
    
#ввід назви предмета
@dp.message_handler(state=TakeScores.subject)
async def subject(message: types.Message, state: FSMContext):
    
    answer_subject = message.text
    subjects.append(answer_subject)
    
    await bot.send_message(message.from_user.id, 'Введи свій бал...')
    await TakeScores.next()
    

class Error(Exception):
    pass

class ScoreIsGreater(Error):
    pass

class ScoreIsNotInt(Error):
    pass
class ScoreIsNotPositive(Error):
    pass

@dp.message_handler(state=TakeScores.scores)
#ввід поточного балу з предмету
async def score(message: types.Message, state: FSMContext):
    try:        
        answer_score = float(message.text)
        if(answer_score > 100):
            raise ScoreIsGreater
        elif(answer_score.is_integer == False):
            raise ScoreIsNotInt
        elif(answer_score < 0):
            raise ScoreIsNotPositive
        else:
            scores.append(answer_score)
            await bot.send_message(message.from_user.id, 'Введи кількість кредитів для предмету...')
            await TakeScores.next()
    except ScoreIsGreater: 
        await bot.send_message(message.from_user.id, 'Ніфіга ви розумник,але більше 100 балів бути не може!')
        await TakeScores.scores.set()
    except ScoreIsNotInt:
        await bot.send_message(message.from_user.id, 'Не правильний ввід,введіть ціле число')
    except ScoreIsNotPositive:
        await bot.send_message(message.from_user.id, 'Введіть додатнє число.')
    
    


@dp.message_handler(state=TakeScores.credit)
#ввід кредитів за предмет
async def credit(message: types.Message, state: FSMContext):
    try:
        answer_credit = float(message.text)
        if(answer_credit.is_integer == False):
            raise ScoreIsNotInt
        elif(answer_credit < 0):
            raise ScoreIsNotPositive
        else:
            credits.append(answer_credit)
            await bot.send_message(message.from_user.id, 'Продовжимо, чи хочеш побачити результат ?', reply_markup=nav.markup)
            await TakeScores.next()
    except ScoreIsNotInt: 
        await bot.send_message(message.from_user.id, 'Неправильний ввід ви маєте ввести ціле число.')
    except ScoreIsNotPositive:
        await bot.send_message(message.from_user.id, 'Введіть додатнє число.')

@dp.message_handler(state=TakeScores.alt_step)
async def process_alt_step(message: types.Message, state: FSMContext):
    answer = message.text
    if answer.lower() == 'результат':
        #await bot.send_message(message.from_user.id, 'Processing...')
        total_crdts = sum(credits)
        result = 0
        i = 0
        while i < len(subjects):
            subject_scr = (scores[i]*credits[i])/total_crdts
            result += subject_scr
            await bot.send_message(message.from_user.id, 'На предметі {} ти отримав {}'.format(subjects[i], subject_scr))
            i += 1
        await bot.send_message(message.from_user.id,'Твій загальний бал {}.'.format(result),reply_markup=nav.mainMenu)
        subjects.clear()
        scores.clear()
        credits.clear()
        await state.finish()
    elif answer.lower() == 'продовжити':
        await bot.send_message(message.from_user.id, 'Введи назву іншого предмета...')
        await TakeScores.subject.set()


@dp.message_handler(state=Teachers.last_name)
async def teachersSearch(message: types.Message, state: FSMContext):
    ReplyKeyboardRemove()
    second_name = str(message.text)
    lower_second_name = second_name.lower()
    info = dt.teachers.get(lower_second_name)
    
    if message.text.lower() == 'вихід':
        await message.reply('Ви повернулися в головне меню.',reply_markup=nav.mainMenu)
        await state.finish()
    elif info == None:
        await bot.send_message(message.from_user.id,'Ви ввели неправильне прізвище,повторіть спробу,або введіть вихід для повернення до головного меню.')
        await Teachers.last_name.set()
    else:
        for key, value in dt.teachers.items():
            if key.lower() == lower_second_name:
                if isinstance(value, list):
                    for element in value:
                        await bot.send_message(message.from_user.id,element)
                    await state.finish()
                else:
                    await bot.send_message(message.from_user.id,value)
                    await state.finish()


@dp.message_handler(state=Kampus.number)
async def kampusesSearch(message: types.Message, state: FSMContext):
    # Finish our conversation
    campus = str(message.text.lower())
    address = dt.campus_adresses.get(campus)
    link_photo = dt.campus_photos.get(campus)
    geo = dt.campus_geo.get(campus)
    latitude = geo[0]
    longtitude = geo[1]
    print("asdas")
    if message.text.lower() == 'вихід':
        await message.reply('Ви повернулися в головне меню.',reply_markup=nav.mainMenu)
        await state.finish()
    elif address == None:
        await bot.send_message(message.from_user.id,'Такого корпусу не існує,введіть інший номер,або введіть вихід для того,щоб повернутися в головне меню.')
        await Kampus.number.set()
    else:
        if(link_photo == ''):
            await message.reply('Фото не знайдено.')
            await message.reply_location(latitude=latitude,longitude=longtitude)
            await state.finish()
        else:
            await message.reply_photo(link_photo,address)
            await message.reply_location(latitude=latitude,longitude=longtitude)
            await state.finish()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
