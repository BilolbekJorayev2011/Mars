from aiogram import types, Bot, executor, Dispatcher
from data import Api_token
import logging
from buttons import menuMain, menuBack, menuButtonsdd, menuMalumot, menuYordam, menuPay, menuClik, menuTilozgarish,menuRorqa, menuRu, menuXodim, menuO


bot = Bot(Api_token)
dp = Dispatcher(bot)

# --> Kimdur kirganlik haqida ma'lumot beruvchi
logging.basicConfig(level=logging.INFO)



@dp.message_handler(commands=["start"])
async def tart(message:types.Message):
    username = message.from_user.full_name
    logging.info(message)
    await message.answer(f"Salom {username}", reply_markup=menuMain)


@dp.message_handler(text='🇺🇿Ozbek tili')
async def strt(message:types.Message):
    await message.answer("Kerakli bolimni tanlang",reply_markup=menuButtonsdd)

@dp.message_handler(text='Смена языка🇷🇺')
async def sta(message:types.Message):
    await message.answer("Kerakli bolimni tanlang",reply_markup=menuTilozgarish)

@dp.message_handler(text='Tilni ozgartirish🇺🇿')
async def sfatyv(message:types.Message):
    await message.answer("Kerakli bo'limni tanlang",reply_markup=menuButtonsdd)

@dp.message_handler(text="📄Malumot")
async def rasm_handler(message :types.Message):
    await message.answer_photo("https://t.me/uzb_xabarlar_kunuz/166",reply_markup=menuButtonsdd)
    await message.answer_photo("https://t.me/uzb_xabarlar_kunuz/164","https://t.me/uzb_xabarlar_kunuz/164",reply_markup=menuBack)

@dp.message_handler(text='📄Malumot')
async def indfo_snjtarter(message:types.Message):
    await message.answer("Orqaga", reply_markup=menuBack)

# Informasiya tugmasi
@dp.message_handler(text='📄Информация')
async def indfo_starter(message:types.Message):
    await message.answer_photo("https://t.me/uzb_xabarlar_kunuz/166",reply_markup=menuButtonsdd)
    await message.answer_photo("https://t.me/uzb_xabarlar_kunuz/164","https://t.me/uzb_xabarlar_kunuz/164",reply_markup=menuRorqa)
# nazad tugmasi
@dp.message_handler(text=['🔙Назад'])
async def stesdat(message:types.Message):
    await message.answer("Выберите нужный раздел",reply_markup=menuRu)

@dp.message_handler(text=['🔚Назад'])
async def stakit(message:types.Message):
    await message.answer("Выберите нужный раздел",reply_markup=menuTilozgarish)

# Back orqaga tugmasi
@dp.message_handler(text=['🔙Orqaga'])
async def stat(message:types.Message):
    await message.answer("Kerakli bolimni tanlang",reply_markup=menuMalumot)

# End orqaga tugmasi
@dp.message_handler(text='🔚Orqaga')
async def bbb(message:types.Message):
    await message.answer("Kerakli bolimni tanlang",reply_markup=menuButtonsdd)

# Pul yordami tugmasi
@dp.message_handler(text='Pul yordami💸')
async def sbjbart(message:types.Message):
    await message.answer("Click yoki Payme orqali yordam berishingiz mumkin.",reply_markup=menuYordam)

# Payme tugmasi
@dp.message_handler(text='Payme💵')
async def stnnmrt(message:types.Message):
    await message.answer("Payme",reply_markup=menuPay)

# Clik tugmasi
@dp.message_handler(text='Click💵')
async def staiinjt(message:types.Message):
    await message.answer("Click💵",reply_markup=menuClik)

# Xodimlar haqida malumot
@dp.message_handler(text='👨‍💻Xodimlar haqida malumot')
async def staiit(message:types.Message):
    await message.answer("Click💵",reply_markup=menuXodim)

# Ortga
@dp.message_handler(text='🔙Orqaga')
async def staiit(message:types.Message):
    await message.answer("Kerakli bo'limni tanlang",reply_markup=menuButtonsdd)

# Rustili tugmasi
@dp.message_handler(text='🇷🇺Rus tili')
async def sbdjsddsj(message:types.Message):
    await message.answer("Выберите нужный раздел",reply_markup=menuTilozgarish)

@dp.message_handler(text='Nima yordam bera olaman😇')
async def sbdjsddsj(message:types.Message):
    await message.answer("Nima yordam bera olishim mumkin",reply_markup=menuMalumot)

@dp.message_handler(text='Oyinchoq🧸')
async def sbdjfjsddsj(message:types.Message):
     await message.answer("Mumkin bo'lmagan o'yinchoqlar❌. \n👉1. Yumshoq tukli o'yinchoqlar.\n👉2. Sochi bor O'yinchoqlar.\n\n Mumkin bo'lgan o'yinchoqlar✅.\n👉1. Lego.\n👉2. Birgalikda bo'yaladigan raskraskalar.\n👉3.Tvister\n 👉4. Qum (suniy).\n 👉5. Kachela ichkariga qo'yiladigan.\n\n☎️ Tel: +99870 202-00-42\n☎️ Tel: +99893 423-00-09",reply_markup=menuO)

@dp.message_handler(text='🔙Orqaga')
async def sbdjsfddsj(message:types.Message):
    await message.answer("Kerakli bo'limini tanlang",reply_markup=menuYordam)


  
  
  
  
 




if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
