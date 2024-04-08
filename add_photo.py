from aiogram.dispatcher import FSMContext


from keybords.default.buttons import user_main_menu
from loader import dp, db
from aiogram import types



@dp.message_handler(text="Upload picture")
async def user_upload_photo(message: types.Message, state: FSMContext):
    photo = db.get_user_photo_by_chat_id(chat_id=message.chat.id)
    if photo:
        text = f"""
        Already uploaded"""
        await message.answer_photo(photo=photo[2])
    else:
        text = "Upload your favourite picture"
    await state.set_state("user-upload-photo")
    await message.answer(text=text)



@dp.message_handler(state="user-upload-photo", content_types=types.ContentTypes.PHOTO)
async def get_upload_photo(message: types.Message, state: FSMContext):
    await state.update_data(photo_id=message.photo[-1].file_id, chat_id=message.chat.id)
    data = await state.get_data()

    if db.add_photo(data):
        text = f"successfully added"
    else:
        text = "Failed try again"
    await message.answer(text=text)
    await state.finish()