from aiogram import types

from misc import dp
from handlers.presented_students_handler import set_user_present
from handlers.tasks_handler import task_callback, tasks_callback


@dp.callback_query_handler()
async def callback_present(callback_query: types.CallbackQuery):
    callback_fields = callback_query.data.split('_')
    if callback_fields[0] == "present":
        if len(callback_fields) == 2:
            is_present = callback_fields[1] == 'yes'
            set_user_present(callback_query.from_user.id, is_present)
            if is_present:
                await callback_query.message.edit_text("Молодец!")
            else:
                await callback_query.message.edit_text("Ну, как хочешь...")
    elif callback_fields[0] == "task":
        await task_callback(callback_fields, callback_query)
    elif callback_fields[0] == "tasks":
        await tasks_callback(callback_fields, callback_query)
    await callback_query.answer()
