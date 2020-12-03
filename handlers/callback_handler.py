from aiogram import types

from misc import dp
from handlers.presented_students_handler import poll_handle
# from handlers.tasks_handler import task_callback, tasks_callback


@dp.callback_query_handler()
async def callback_present(callback_query: types.CallbackQuery):
    callback_fields = callback_query.data.split('_')
    if callback_fields[0] == "poll":
        if len(callback_fields) == 2:
            await poll_handle(callback_query)
    # elif callback_fields[0] == "task":
    #     await task_callback(callback_fields, callback_query)
    # elif callback_fields[0] == "tasks":
    #     await tasks_callback(callback_fields, callback_query)
    await callback_query.answer()
