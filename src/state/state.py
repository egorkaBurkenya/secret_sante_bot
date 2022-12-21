from aiogram.dispatcher.filters.state import StatesGroup, State

class Registration(StatesGroup):
    WatingPassword = State()
    WatingName = State()
    WatingPhoto = State()
    WatingWishlist = State()
    WatingHateList = State()

class Hub(StatesGroup):
    Main = State()

class _UserState(StatesGroup):
    Registration = Registration()
    Hub = Hub()