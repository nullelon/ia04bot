import re
from aiogram import types
from misc import dp, config, bot
from students import students

users_answers = dict()
options = list()
answer_texts = list()
question = ''

# /poll (Ты хочешь записать в очередь на ОС?) [Да;Нет] {Окей, я записал тебя!; Понял, спасибо за ответ!}
r = re.compile(r"^/poll \((.+)\) \[(.+)] \{(.+)}$")


@dp.message_handler(commands='exec')
async def presented(message: types.Message):
    if message.from_user.id != int(config["Bot"]["admin_id"]):
        return
    exec(message.text[6:])


@dp.message_handler(commands='poll')
async def presented(message: types.Message):
    if message.from_user.id != int(config["Bot"]["admin_id"]):
        return

    regex = r.match(message.text)

    if regex is not None:
        options.clear()
        users_answers.clear()
        answer_texts.clear()

        global question
        question = regex.group(1)
        for option in regex.group(2).split(";"):
            options.append(option.strip())
        for answer in regex.group(3).split(";"):
            answer_texts.append(answer.strip())

        if len(answer_texts) != len(options):
            await message.reply("Кол-во аргуметов в [] и {} должно быть одинаковое!")
            return

        for student in students:
            keyboard = types.InlineKeyboardMarkup()
            for option in options:
                keyboard.add(types.InlineKeyboardButton(text=option, callback_data=f"poll_{options.index(option)}"))
            try:
                await bot.send_message(text=question, chat_id=student, reply_markup=keyboard)
            except:
                print(f"Не могу написать {student}")
    else:
        await message.reply("Шаблон: /poll (Вопрос) "
                            "[o1;o2] {a1;a2}\n\non - вариант ответа\nan - ответ бота на выбор on варианта")


@dp.message_handler(commands='list')
async def list_handler(message: types.Message):
    if question == '':
        await message.reply("Вопрос еще не задавали!")
        return
    fields = message.text.split()
    filter = ''
    filter_text = ''
    if len(fields) > 1:
        filter = ' '.join(fields[1:])
        filter_text = f'с фильтром "{filter}"'

    text = f'Ответы на опрос "{question}" {filter_text}:\n\n'
    for answered_id in users_answers:
        student = ' '.join(students[answered_id])
        answer_of_student = options[int(users_answers[answered_id])]
        if filter in answer_of_student:
            text += f'{student} - {answer_of_student}\n'
    await message.reply(text)


async def poll_handle(callback_query: types.CallbackQuery):
    answer = callback_query.data.split("_")[1]
    users_answers[callback_query.from_user.id] = answer
    if int(answer) in answer_texts:
        await callback_query.message.edit_text(answer_texts[int(answer)])
    else:
        await callback_query.message.edit_text('Ммм оаоаоаоа')
