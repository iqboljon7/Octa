import asyncio
import logging

from aiogram import Bot, Dispatcher, types, F, Router
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from req import rqs

bot = Bot(token="5959142337:AAFFb8f-oHKEPiNvuJZIABaNOjmb-bXBg3c")
class req(StatesGroup):
    brdate = State()
    ser_num = State()
dispatcher = Dispatcher()

dp = Router()
dispatcher.include_router(dp)



@dp.message(Command("start"))
async def cmd_start(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer("Send the date of birth of the person whose information you want to find in the format day.month.year")
    await state.set_state(req.brdate)

@dp.message(req.brdate)
async def birthday(msg: types.Message,state: FSMContext):
    await state.update_data(brdate=msg.text)
    await msg.answer("Now enter your passport number and serial number. For example: AD12345667")
    await state.set_state(req.ser_num)

@dp.message(req.ser_num)
async def serial_number(msg: types.Message, state: FSMContext):
    await state.update_data(ser_num=msg.text)
    data = await state.get_data()
    await msg.answer(rqs(data['brdate'],data['ser_num'][:2], data['ser_num'][2:]))

async def main():
    await dispatcher.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())

    