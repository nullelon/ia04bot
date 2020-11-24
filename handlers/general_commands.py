import random
import re
from datetime import datetime

import pytz
from aiogram import types
from misc import dp, bot
from students import students


@dp.message_handler(commands='zoom')
async def zoom(message: types.Message):
    fields = message.text.split()
    if len(fields) == 1:
        await message.reply("Чей именно зум нужно найти?")
    else:
        msg = await bot.forward_message(545484163, from_chat_id=-1001409457067, message_id=11)

        text = re.sub(r'\n+</a>', '</a>\n', msg.html_text)
        final_line = ''
        for line in text.splitlines():
            if fields[1].lower() in line.lower():
                final_line = line

        await msg.delete()
        if final_line != '':
            await message.reply(final_line, parse_mode='HTML', disable_web_page_preview=True)
        else:
            await message.reply('Ничего не нашел...')


@dp.message_handler(commands='rand')
async def random_list(message: types.Message):
    fields = message.text.split()
    additional_text = ""
    if len(fields) > 2:
        additional_text = " ({})".format(" ".join(fields[2:]))  # everything that comes after /rand N
    text = 'Бог рандома выбрал следующие бригады{}:\n'.format(additional_text)
    if fields[1].isnumeric() and 0 < int(fields[1]) < 32:
        l = list(range(1, int(fields[1]) + 1))
        random.shuffle(l)
        i = 0
        for number in l:
            i += 1
            text += f'{i}) Бригада {number}\n'
    else:
        text = "ты дибил да"

    await message.reply(text)


@dp.message_handler(commands='rands')
async def random_list(message: types.Message):
    text = 'Бог рандома выбрал следующих жертв:\n'
    keys = list(students.keys())
    random.shuffle(keys)
    i = 0
    for key in keys:
        i += 1
        text += f'{i}) {" ".join(students[key])}\n'
    await message.reply(text)


@dp.message_handler(commands='schedule')
async def schedule(message: types.Message):
    time = datetime.now(tz=pytz.timezone("Europe/Kiev"))
    seconds = time.hour * 60 * 60 + time.minute * 60
    text = f'1 пара  08-30 - 10-05{" &lt=" if 30600 <= seconds <= 37500 else ""}\n' \
           f'2 пара  10-25 - 12-00{" &lt=" if 37500 <= seconds <= 44400 else ""}\n' \
           f'3 пара  12-20 - 13-55{" &lt=" if 44400 <= seconds <= 51300 else ""}\n' \
           f'4 пара  14-15 - 15-50{" &lt=" if 51300 <= seconds <= 58200 else ""}\n' \
           f'5 пара  16-10 - 17-45{" &lt=" if 58200 <= seconds <= 63900 else ""}'
    await message.reply(text=text)
