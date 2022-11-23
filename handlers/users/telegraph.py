from aiogram import types
from loader import dp
from utils import photo_link,text_recognition
from loader import bot

@dp.message_handler(content_types='photo')
async def photo_handler(msg:types.Message):
    photo=msg.photo[-1]
    link = await photo_link(photo)
    await msg.answer("Tez orada natija jo'natiladi iltimos kutib turing...")
    result=await text_recognition(link)

    await msg.answer(result)
    res_doc=open("result.doc","rb")
    await bot.send_document(msg.chat.id,document=res_doc)
    # await msg.reply_document(document='result.txt',caption="doc")

