from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher, filters
from aiogram.utils import executor
from datetime import datetime

bot = Bot(token='token', parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


@dp.message_handler(filters.Regexp(regexp="Бердник"))
@dp.message_handler(filters.Regexp(regexp="Букасов"))
async def lapochka_handler(message: types.Message):
    await message.reply("Лапуня❤️❤️❤️!!!")


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


@dp.message_handler(commands='schedule')
async def schedule(message: types.Message):
    await message.reply(text=scheduleText())


def scheduleText():
    time = datetime.now()
    seconds = time.hour * 60 * 60 + time.minute * 60
    text = f'1 пара  08-30 - 10-05{" <-" if 30600 <= seconds <= 37500 else ""}\n' \
           f'2 пара  10-25 - 12-00{" <-" if 37500 <= seconds <= 44400 else ""}\n' \
           f'3 пара  12-20 - 13-55{" <-" if 44400 <= seconds <= 51300 else ""}\n' \
           f'4 пара  14-15 - 15-50{" <-" if 51300 <= seconds <= 58200 else ""}\n' \
           f'5 пара  16-10 - 17-45{" <-" if 58200 <= seconds <= 63900 else ""}'
    return text


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
