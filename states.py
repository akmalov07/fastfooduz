from aiogram.fsm.state import State, StatesGroup

class ContactState(StatesGroup):
    waiting_for_message = State()


class CategoryState(StatesGroup):
    nomi = State()
    tasdiqlash = State()
    
    
class DeleteCategoryState(StatesGroup):
    nomi = State()
    tasdiqlash = State()


class ProductState(StatesGroup):
    category_selection = State()
    nomi = State()
    narxi = State()
    rasm_url = State()
    tasdiqlash = State()
    

class DeleteProductState(StatesGroup):
    nomi = State()
    tasdiqlash = State()