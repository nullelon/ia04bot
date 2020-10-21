from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher, filters
from aiogram.utils import executor

bot = Bot(token='token', parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


@dp.message_handler(filters.Regexp(regexp="Бердник"))
@dp.message_handler(filters.Regexp(regexp="Букасов"))
async def lapochka_handler(message: types.Message):
    await message.reply("Лапочка❤️❤️❤️!!!")


@dp.message_handler(filters.Regexp(regexp="Женя!"))
@dp.message_handler(filters.Regexp(regexp="Староста!"))
async def headman_handler(message: types.Message):
    await message.reply("@nullelon иди сюда, котёночек ты наш любимый 😻😻😻")


@dp.message_handler(filters.Regexp(regexp="Ася!"))
async def asya_handler(message: types.Message):
    await message.reply("@agent_sever иди сюда, наша ты кошечка!!! 😻😻😻")


@dp.message_handler(filters.Regexp(regexp="электричк"))
async def electrichka_handler(message: types.Message):
    await message.reply_sticker(sticker="CAACAgIAAxkBAAEGO-hfdE0ZBsw8zvUNKI2lxKA6mHqNkwACBQADqxJqFVBIhP7h96FeGwQ")


@dp.message_handler(commands='schedule')
async def schedule(message: types.Message):
    await message.reply(text="1 пара  08-30 - 10-05\n"
                             "2 пара  10-25 - 12-00\n"
                             "3 пара  12-20 - 13-55\n"
                             "4 пара  14-15 - 15-50\n"
                             "5 пара 16-10 - 17-45")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
