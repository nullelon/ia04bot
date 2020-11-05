import re
import random

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher, filters
from aiogram.utils import executor
from datetime import datetime
import configparser

config = configparser.ConfigParser()
config.read("settings.ini")

bot = Bot(token=config['Bot']['token'], parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

with open("students.txt", "r") as f:
    lines = f.read().splitlines()
students = dict()

for line in lines:
    fields = line.split()
    if len(fields) == 3 and fields[0].isnumeric():
        students[int(fields[0])] = fields[1:]

last_presented = list()


@dp.message_handler(commands='presented')
async def presented(message: types.Message):
    if message.from_user.id != int(config["Bot"]["admin_id"]):
        return
    last_presented.clear()
    for student in students:
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text="Да!", callback_data="present"))
        keyboard.add(types.InlineKeyboardButton(text="Нет(", callback_data="not_present"))
        await bot.send_message(text="Ты присутствуешь на паре?", chat_id=student, reply_markup=keyboard)


@dp.callback_query_handler()
async def callback_present(callback_query: types.CallbackQuery):
    if callback_query.data == "present":
        last_presented.append(callback_query.from_user.id)
        await callback_query.message.edit_text("Молодец!")
    elif callback_query.data == "not_present":
        await callback_query.message.edit_text("Ну, как хочешь...")


@dp.message_handler(commands='list')
async def list_handler(message: types.Message):
    text = 'Присутствующие:\n\n'
    for p in last_presented:
        text += f'{" ".join(students[p])}\n'
    await message.reply(text)


@dp.message_handler(commands='start')
async def list_handler(message: types.Message):
    await message.reply("Спасибо! Больше ничего не нужно.")
    await bot.send_message(
        chat_id=545484163,
        text=f"{' '.join(students[message.from_user.id])} нажал(а) кнпоку")


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


@dp.message_handler(commands='rand')
async def random_list(message: types.Message):
    fields = message.text.split()
    text = 'Бог рандома выбрал следующие бригады:\n'
    if fields[1].isnumeric() and 0 < int(fields[1]) < 32:
        l = list(range(1, int(fields[1])))
        random.shuffle(l)
        i = 0
        for number in l:
            i += 1
            text += f'{i}) Бригада {number}\n'
    else:
        text = "ты дибил да"

    await message.reply(text)


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
