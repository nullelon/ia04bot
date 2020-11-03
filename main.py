import re
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher, filters
from aiogram.utils import executor
from datetime import datetime
import configparser

config = configparser.ConfigParser()
config.read("settings.ini")

bot = Bot(token=config['Bot']['token'], parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


@dp.message_handler(commands='zoom')
async def zoom(message: types.Message):
    fields = message.text.split()
    if len(fields) == 1:
        await bot.forward_message(message.chat.id, from_chat_id=-1001409457067, message_id=11)
    else:
        msg = await bot.forward_message(545484163, from_chat_id=-1001409457067, message_id=11)

        final_line = ''

        text = msg.html_text

        text = re.sub(r'\n+</a>', '</a>\n', text)

        for line in text.splitlines():
            if fields[1].lower() in line.lower():
                final_line = line

        await msg.delete()
        if final_line != '':
            await message.reply(final_line, parse_mode='HTML', disable_web_page_preview=True)
        else:
            await message.reply('Ничего не нашел...')


@dp.message_handler(commands='schedule')
async def schedule(message: types.Message):
    await message.reply(text=schedule_text())


def schedule_text():
    time = datetime.now()
    seconds = time.hour * 60 * 60 + time.minute * 60
    text = f'1 пара  08-30 - 10-05{" &lt=" if 30600 <= seconds <= 37500 else ""}\n' \
           f'2 пара  10-25 - 12-00{" &lt=" if 37500 <= seconds <= 44400 else ""}\n' \
           f'3 пара  12-20 - 13-55{" &lt=" if 44400 <= seconds <= 51300 else ""}\n' \
           f'4 пара  14-15 - 15-50{" &lt=" if 51300 <= seconds <= 58200 else ""}\n' \
           f'5 пара  16-10 - 17-45{" &lt=" if 58200 <= seconds <= 63900 else ""}'
    return text


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


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
