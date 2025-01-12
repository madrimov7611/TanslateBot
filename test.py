import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from konfig import token as token
from aiogram.types import Message, FSInputFile
from gtts import gTTS
from googletrans import Translator

logging.basicConfig(level=logging.INFO)

bot = Bot(token=token)
dp = Dispatcher()

translator = Translator()

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
    await message.answer(f"Ingliz tilidagi tarjimasi : {translated_text}")

@dp.message(Command("start"))
async def StartCommand(message: Message):
    await message.answer("So'zni kiriting")

@dp.message()
async def TranslateCommand(message: Message):
    await TranslateAndVoice(message)

if __name__ == '__main__':
    dp.run_polling(bot)
