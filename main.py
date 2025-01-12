import asyncio
import logging
import wikipedia
from base import ReadObunachilar, InsertUserlar, ReadObunachilars
from stets import TarjimoneyState, TarjimoneyState1, TarjimoneyState2, WikipedState
from aiogram.types import Message, CallbackQuery, FSInputFile
from buttons import tarjimon_klaviyatura, asosiy, asosiy2
from konfig import token, admins
from googletrans import Translator
from gtts import gTTS
from aiogram import Bot, Dispatcher, F
from aiogram.fsm.context import FSMContext
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart, Command

logging.basicConfig(level=logging.INFO)
bot = Bot(token=token,default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()
    
translator = Translator()

@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    first_name = message.from_user.first_name
    a = []
    for i in ReadObunachilars():
        a.append(i[1])
    if first_name in a:
        pass
    else:
        InsertUserlar(first_name=first_name)
    await message.answer(f"Assalomu aleykum Жавохир\nbotga xush kelibsiz 👋\n\nBu bot yordamida siz\nWikipediya yoki kerakli so'zlaringizni\ntarjima qila olasiz...", reply_markup=asosiy)


@dp.message(F.text == "Ortga")
async def OrtgaBot(mess: Message):
    await mess.answer(f"Bosh sahifaga qaytdingiz", reply_markup=asosiy)



@dp.message(F.text == "users", F.from_user.id.in_(admins))
async def Obunachilar(message: Message):
        for ii in ReadObunachilar():
            obunachilar = ii[0]
            await message.answer(f"Obunachilaringiz soni: {obunachilar}")


@dp.callback_query(F.data == "wiki")
async def WikipedBot(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Endi siz Wikipediyadan\nfoydalana olasiz", reply_markup=asosiy2)
    await state.set_state(WikipedState.wikipedd)


@dp.message(F.text, WikipedState.wikipedd)
async def echo(message: Message):
    xabar = message.text
    try:
        wikipedia.set_lang('uz')
        malumot = wikipedia.summary(f"{xabar}")
        await message.reply(text=f"{malumot}")
    except:
        await message.answer("uzur topa olmadim ma'lumot")



@dp.callback_query(F.data == "tarjima")
async def Tarjimaqil(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Endi siz har qanday\nso'zni tarjimaqila olasiz", reply_markup=tarjimon_klaviyatura)


@dp.callback_query(F.data == "avto")
async def Tarjimaqil(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Siz endi har qanday so'zni o'zbekchaga\ntarjima qila olasiz", reply_markup=asosiy2)
    await state.set_state(TarjimoneyState.tarjim)


@dp.message(TarjimoneyState.tarjim)
async def TranslateAndVoice(message):
    word = message.text

    translation = translator.translate(word, dest="avto")
    translated_text = translation.text

    tts = gTTS(text=translated_text, lang='avto')
    tts.save("tarjima.mp3")

    async def AudioCommand():
        a = FSInputFile(path="tarjima.mp3", filename=f"{message.text}.mp3")
        await message.answer_audio(a)

    await AudioCommand()
    await message.answer(f"Tarjimasi : {translated_text}")


@dp.callback_query(F.data == "en")
async def Tarjimaqil(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Siz endi o'zbekcha so'zni\ninglizchaga o'gira olasiz", reply_markup=asosiy2)
    await state.set_state(TarjimoneyState1.tarjim1)


@dp.message(TarjimoneyState1.tarjim1)
async def TranslateAndVoice(message):
    word = message.text

    translation = translator.translate(word, dest="en")
    translated_text = translation.text

    tts = gTTS(text=translated_text, lang='en')
    tts.save("tarjima.mp3")

    async def AudioCommand():
        a = FSInputFile(path="tarjima.mp3", filename=f"{message.text}.mp3")
        await message.answer_audio(a)

    await AudioCommand()
    await message.answer(f"Tarjimasi : {translated_text}")



@dp.callback_query(F.data == "ru")
async def Tarjimaqil(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Siz endi o'zbekcha so'zni\nruschaga o'gira olasiz", reply_markup=asosiy2)
    await state.set_state(TarjimoneyState2.tarjim2)


@dp.message(TarjimoneyState2.tarjim2)
async def TranslateAndVoice(message):
    word = message.text

    translation = translator.translate(word, dest="ru")
    translated_text = translation.text

    tts = gTTS(text=translated_text, lang='ru')
    tts.save("tarjima.mp3")

    async def AudioCommand():
        a = FSInputFile(path="tarjima.mp3", filename=f"{message.text}.mp3")
        await message.answer_audio(a)

    await AudioCommand()
    await message.answer(f"Tarjimasi : {translated_text}")



async def main():
    for i in admins:
        await bot.send_message(chat_id=i, text="Bot ishga tushdi")
        await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except:
        print("Tugadi")









# from googletrans import Translator
# import asyncio
# import logging
# # from test import TransBot
# from konfig import token
# # from aiogram import types
# from aiogram import Bot, Dispatcher, F
# # from aiogram.utils.keyboard import InlineKeyboardBuilder
# from aiogram.filters.command import Command, CommandStart
# from aiogram.client.default import DefaultBotProperties
# from aiogram.enums import ParseMode
# # from aiogram.fsm.context import FSMContext
# from aiogram.types import Message, FSInputFile, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove


# logging.basicConfig(level=logging.INFO)
# bot = Bot(token=token,default=DefaultBotProperties(parse_mode=ParseMode.HTML))
# dp = Dispatcher()

# translator = Translator


# @dp.message(CommandStart())
# async def cmd_start(message: Message):
#     # await message.answer(f"Assalomu aleykum {message.from_user.first_name}\n\nTranslet botga hush kelibsiz 👋\nBu bot yordamida siz har qanday so'zni\no'zbekchaga tarjima qila olasiz")
#     await message.answer(
#         f"Assalomu aleykum {message.from_user.first_name}\n\n"
#         "Translet botga hush kelibsiz 👋\n"
#         "Bu bot yordamida siz har qanday so'zni\n"
#         "o'zbekchaga tarjima qila olasiz.\n"
#         "Foydalanish uchun, faqat tarjima qilmoqchi bo'lgan so'zni yuboring."
#     )



# # @dp.message(F.text)
# # async def Tarjima(mess: Message):
# #     xabar = TransBot(text=mess.text)
# #     await mess.answer(xabar)


# @dp.message()
# async def translate_message(message: Message):
#     text = message.text
#     try:
#         translation = translator.translate(text, src='auto', dest='uz')
#         await message.answer(translation.text)
#     except Exception as e:
#         await message.answer(f"Tarjima qilishda xato: {e}")





# async def main():
#     await dp.start_polling(bot)

# if __name__ == "__main__":
#     try:
#         asyncio.run(main())
#     except:
#         print("Tugadi")