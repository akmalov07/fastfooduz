import asyncio
from aiogram import F, types
from aiogram.filters import Command
from config import bot, dp, ADMIN_ID
from database import create_tables, insert_category
from keyboards import main_menu, language_keyboard, branches_keyboard, main_menu_admin, admin_ha_yoq_keyboard, kategory_keyboards
from states import ContactState, CategoryState
from aiogram.fsm.context import FSMContext

import logging
logging.basicConfig(level=logging.INFO)


@dp.message(Command("start"))
async def start_command(message: types.Message):
    
    if message.from_user.id == ADMIN_ID:
        await message.answer("👑 Assalomu alaykum, Admin! Bot boshqaruv paneliga xush kelibsiz.", reply_markup=main_menu_admin)
    else:
        await message.answer(
            text=f"🔥 Assalomu alaykum, {message.from_user.full_name}\nFastFood botimizga xush kelibsiz!",
            reply_markup=main_menu
        )
        
@dp.message(F.text == "⬅️ Orqaga")
async def go_back(message: types.Message, state: FSMContext):
    if message.from_user.id == ADMIN_ID:
        await message.answer("👑 Asosiy menyuga qaytdingiz.", reply_markup=main_menu_admin)
    else:
        await message.answer("🏠 Asosiy menyuga qaytdingiz.", reply_markup=main_menu)
    await state.clear()
        
@dp.message(F.text == "➕ Category qo'shish")
async def add_category_admin(message: types.Message, state: FSMContext):
    await message.answer("Iltimos, yangi kategoriyaning nomini kiriting:")
    await state.set_state(CategoryState.nomi)
    

@dp.message(CategoryState.nomi)
async def get_category_name(message: types.Message, state: FSMContext):
    category_name = message.text
    await state.update_data(nomi=category_name)    
    await message.answer(f"Siz kiritgan kategoriya nomi: {category_name}\nTasdiqlaysizmi?", reply_markup=admin_ha_yoq_keyboard)
    await state.set_state(CategoryState.tasdiqlash)
    

@dp.message(CategoryState.tasdiqlash)
async def confirm_category(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    category_name = user_data.get("nomi")
    
    if message.text == "✅ Ha":
        insert_category(category_name)  
        await message.answer(f"✅ Kategoriya '{category_name}' muvaffaqiyatli qo'shildi!", reply_markup=main_menu_admin)
    else:
        await message.answer("❌ Kategoriya qo'shish bekor qilindi.", reply_markup=main_menu_admin)
    
    await state.clear()


# category o'chirish
# product qo'shish
# product o'chirish
# kamida 5 ta category qo'shish, har birini ichida kamida 4-5 ta dan product qo'shish


@dp.message(F.text == "🍔 Menyu")
async def menu_section(message: types.Message):
    await message.answer("📋 Siz FastFood botimiz menyusiga kirdingiz! Kerakli menyuni tanlang:", reply_markup=kategory_keyboards)

@dp.message(F.text == "🛒 Mening Savatim")
async def basket_section(message: types.Message):
    await message.answer("🧺 Siz Savat bo‘limidasiz!")

@dp.message(F.text == "⚙️ Sozlamalar")
async def settings_section(message: types.Message):
    await message.answer("🌐 Qaysi tilni tanlaysiz?", reply_markup=language_keyboard)

@dp.callback_query(F.data.startswith("lang_"))
async def language_selected(callback: types.CallbackQuery):
    lang = callback.data.split("_")[1]
    text = "🇺🇿 O'zbek tili tanlandi!" if lang == "uz" else "🇷🇺 Русский язык выбран!"
    await callback.message.edit_text(text)

@dp.message(F.text == "🏪 Filliallarimiz")
async def branches_section(message: types.Message):
    await message.answer("🏪 Bizning filiallarimiz:", reply_markup=branches_keyboard)
    await message.answer_location(latitude=41.34515614076059, longitude=69.20549917037076)

@dp.message(F.text == "📞 Aloqa")
async def contact_section(message: types.Message, state: FSMContext):
    await message.answer("📩 Admin bilan bog‘lanish uchun xabaringizni yozing:")
    await state.set_state(ContactState.waiting_for_message)

@dp.message(ContactState.waiting_for_message)
async def get_contact_message(message: types.Message, state: FSMContext):
      # bu yerda admin telegram ID si yoziladi
    await bot.send_message(ADMIN_ID, f"📨 Yangi xabar: {message.from_user.full_name}\n\n{message.text}")
    await message.answer("✅ Xabaringiz yuborildi, tez orada siz bilan bog‘lanamiz!")
    await state.clear()


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    create_tables()
    asyncio.run(main())
