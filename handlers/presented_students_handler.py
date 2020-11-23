from aiogram import types

from misc import dp, config, bot

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
        keyboard.add(types.InlineKeyboardButton(text="Да!", callback_data="present_yes"))
        keyboard.add(types.InlineKeyboardButton(text="Нет(", callback_data="present_no"))
        try:
            await bot.send_message(text="Ты присутствуешь на паре?", chat_id=student, reply_markup=keyboard)
        except:
            print(f"Не могу написать {student}")


@dp.message_handler(commands='list')
async def list_handler(message: types.Message):
    text = 'Присутствующие:\n\n'
    for p in last_presented:
        text += f'{" ".join(students[p])}\n'
    await message.reply(text)


def set_user_present(user_id, is_present):
    if is_present:
        last_presented.append(user_id)
