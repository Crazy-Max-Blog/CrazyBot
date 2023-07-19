from aiogram.fsm.state import State, StatesGroup


class UserStates(StatesGroup):
    ENTER_NAME = State()
    ENTER_AGE = State()
    ENTER_CITY = State()
    ENTER_INFO = State()
    UPDATE_DATA = State()
    SEARCH_PEOPLE = State()

class AdminStates(StatesGroup):
    ENTER_NAME = State()
    ENTER_AGE = State()
    ENTER_CITY = State()
    ENTER_INFO = State()
    UPDATE_DATA = State()
    SEARCH_PEOPLE = State()
