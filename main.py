import asyncio
import logging
# dummy comment

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

@dp.message(Command("nth"))
async def cmd_start(message: types.Message):
    await message.answer("nothing")

@dp.message(Command("start"))
async def cmd_start(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer("Send the date of birth of the person whose information you want to find in the format day.month.year")
    await state.set_state(req.brdate)

@dp.message(req.brdate)
async def birthday(msg: types.Message,state: FSMContext):
    m=msg.text
    if m[2]==m[5]==".":
        a,b,c = msg.text.split(".")
        try:
            if int(a) and int(b) and int(c):
                await state.update_data(brdate=msg.text)
                await msg.answer("Now enter your passport number and serial number. For example: AD12345667")
                await state.set_state(req.ser_num)
            else:
                await msg.answer("you entered information in wrong format")
        except:
            await msg.answer("you entered information in wrong format")
    else:
        await msg.answer("you entered information in wrong format")

@dp.message(req.ser_num)
async def serial_number(msg: types.Message, state: FSMContext):
    xabar=msg.text
    if xabar[0]=="A" and len(xabar)==9:
        try:
            if int(xabar[2:]):
                await state.update_data(ser_num=msg.text)
                data = await state.get_data()
                await msg.answer(rqs(data['brdate'],data['ser_num'][:2], data['ser_num'][2:]))
            else:
                await msg.answer("you entered information in wrong format")
        except:
            await msg.answer("you entered information in wrong format")
    else:
        await msg.answer("you entered information in wrong format")
async def main():
    await dispatcher.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())

    
