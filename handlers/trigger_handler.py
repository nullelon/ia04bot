from aiogram import types
from aiogram.dispatcher import filters

from misc import dp


@dp.message_handler(filters.Regexp(regexp="Женя!"))
@dp.message_handler(filters.Regexp(regexp="Староста!"))
async def headman_handler(message: types.Message):
    await message.reply("@nullelon іди сюди, кошаче 😻")


@dp.message_handler(filters.Regexp(regexp="Ася!"))
async def asya_handler(message: types.Message):
    await message.reply("@agent_sever іди сюди, наша ти киця олюблена!!! 😻😻😻")


@dp.message_handler(filters.Regexp(regexp="электричк"))
async def electrichka_handler(message: types.Message):
    await message.reply_sticker(sticker="CAACAgIAAxkBAAEGO-hfdE0ZBsw8zvUNKI2lxKA6mHqNkwACBQADqxJqFVBIhP7h96FeGwQ")


@dp.message_handler(filters.Regexp(regexp="пойду поем"))
async def smachnogo_handler(message: types.Message):
    await message.reply("Смачного ❤️❤️❤️!")
