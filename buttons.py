from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from  aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

menuMain = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🇷🇺Rus tili"),
            KeyboardButton(text="🇺🇿Ozbek tili")
        ]
      
    ],
    resize_keyboard=True
)
# Tilni ruschaga o'girish
menuTilozgarish = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📄Информация")
        ],
        [
            KeyboardButton(text="👨‍💻Информация о персонале")
        ],
        [
            KeyboardButton(text="Чем я могу помочь😇")
        ],
        [
            KeyboardButton(text="Вопросы📝"),
            KeyboardButton(text="Tilni ozgartirish🇺🇿")
        ]
    ],
    resize_keyboard=True
)

# Buttonlar o'zbekcha
menuButtonsdd = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📄Malumot")
        ],
        [
            KeyboardButton(text="👨‍💻Xodimlar haqida malumot")
        ],
        [
            KeyboardButton(text="Nima yordam bera olaman😇")
        ],
        [
            KeyboardButton(text="Savollar📝"),
            KeyboardButton(text="Смена языка🇷🇺")
        ]
    ],
   resize_keyboard=True
)
# Ruschasiga orqaga tugmasi
menuRorqa = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🔙Назад")
        ]
    ],
   resize_keyboard=True
)

# Orqaga tugmasi🔙
menuBack = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🔙Orqaga")
        ]
    ],
   resize_keyboard=True
)


# Yordam bera olish haqidagi ma'lumot
menuMalumot = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Pul yordami💸"),
        ],
        [
            KeyboardButton(text="Oyinchoq🧸"),
            KeyboardButton(text="Ko'ngil(волонтйор)bo'lmoqchiman")
        ],
        [
            KeyboardButton(text="Oziq-ovqat🍕"),
            KeyboardButton(text="Boshqa🤔")
        ],
        [
            KeyboardButton(text="🔚Orqaga")
        ]
    ],
    resize_keyboard=True
)


# Clik va payme
menuYordam = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Payme💵"),
            KeyboardButton(text="Click💵")
        ],
        [
            KeyboardButton(text="🔙Orqaga")
        ]
    ],
    resize_keyboard=True
)


# Payme tugmasi
menuPay = InlineKeyboardMarkup(
    inline_keyboard=[
        [
           InlineKeyboardButton(text="Payme", url="https://payme.uz/home/main")
        ]
    ],
    resize_keyboard=True
)


# Clik tugmasi
menuClik = InlineKeyboardMarkup(
    inline_keyboard=[
        [
           InlineKeyboardButton(text="Click", url="https://payme.uz/home/main")
        ]
    ],
    resize_keyboard=True
)

# menuRUSCHA button

menuRu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Денежная помощь💸"),
        ],
        [
            KeyboardButton(text="Игрушка🧸"),
            KeyboardButton(text="Я хочу быть Bолонтйор")
        ],
        [
            KeyboardButton(text="Еда🍕"),
            KeyboardButton(text="Другой🤔")
        ],
        [
            KeyboardButton(text="🔚Назад")
        ]
    ],
    resize_keyboard=True
)

# menu xodimlar

menuXodim = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Bo'lim mudiri🤵"),
            KeyboardButton(text="Shifokor👩‍⚕️")
        ],
        [
            KeyboardButton(text="Psixolog👱"),
            KeyboardButton(text="Ijtimoiy xodim🤝")
        ],
        [
            KeyboardButton(text="🔙Orqaga")
        ]
    ],
    resize_keyboard=True
)

# orqaga
menuO = ReplyKeyboardMarkup(
    keyboard=[
        [
           KeyboardButton(text="🔙Orqaga")
        ]
    ],
    resize_keyboard=True
)