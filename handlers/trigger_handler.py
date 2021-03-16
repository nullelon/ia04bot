from aiogram import types
from aiogram.dispatcher import filters

from misc import dp


@dp.message_handler(filters.Regexp(regexp="Женя!"))
@dp.message_handler(filters.Regexp(regexp="Староста!"))
async def headman_handler(message: types.Message):
    text = "@nullelon іди сюди, кошаче 😻"
    if message.reply_to_message is not None:
        await message.bot.send_message(message.chat.id, text, reply_to_message_id=message.reply_to_message.message_id)
    else:
        await message.reply(text)


@dp.message_handler(filters.Regexp(regexp="Ася!"))
async def asya_handler(message: types.Message):
    text = "@agent_sever іди сюди, наша ти киця олюблена!!! 😻😻😻"
    if message.reply_to_message is not None:
        await message.bot.send_message(message.chat.id, text, reply_to_message_id=message.reply_to_message.message_id)
    else:
        await message.reply(text)


@dp.message_handler(filters.Regexp(regexp="электричк"))
async def electrichka_handler(message: types.Message):
    await message.reply_sticker(sticker="CAACAgIAAxkBAAEGO-hfdE0ZBsw8zvUNKI2lxKA6mHqNkwACBQADqxJqFVBIhP7h96FeGwQ")


@dp.message_handler(filters.Regexp(regexp="пойду поем"))
async def smachnogo_handler(message: types.Message):
    await message.reply("Смачного ❤️❤️❤️!")
