"""
Telegram Bot, at the request of the user, sends a message
with a cleaning schedule for the apartment.
This bot uses a regular keyboard.

"""

import os
import logging
from aiogram import Bot, Dispatcher, executor, types


API_TOKEN = os.getenv('TELEGRAM_API_TOKEN')

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start_cmd_handler(message: types.Message):
    keyboard_markup = types.ReplyKeyboardMarkup(row_width=3)
    # по умолчанию row_width равен 3, поэтому здесь его можно опустить

    btns_text = ('Пн', 'Вт', 'Ср')
    keyboard_markup.row(*(types.KeyboardButton(text) for text in btns_text))
    # добавляет кнопки в виде новой строки на существующую клавиатуру
    # поведение не зависит от атрибута row_width

    more_btns_text = ('Чт', 'Пт', 'Сб', 'Вс',)
    keyboard_markup.add(*(types.KeyboardButton(text) for text in more_btns_text))
    # добавляет кнопки. Новые строки формируются в соответствии с параметром row_width

    await message.reply("Привет!\nВыбери день уборки", reply_markup=keyboard_markup)


@dp.message_handler()
async def all_msg_handler(message: types.Message):
    # нажатие KeyboardButton равносильно отправке обычного сообщения с тем же текстом
    # поэтому для обработки ответов с клавиатуры нужно использовать message_handler
    # в реальном боте лучше определить message_handler(text="...") для каждой кнопки
    # но здесь для простоты определен только один обработчик

    button_text = message.text
    logger.debug('The answer is %r', button_text)  # напечатает текст, который у нас есть

    if button_text == 'Пн':
        reply_text = "Сегодня кухня!\n"\
                     "Помыть раковину с дезинфицирующим средством\n"\
                     "Протереть бытовую технику\n"\
                     "Протереть фасад кухни\n"\
                     "Протереть подоконник"

    elif button_text == 'Вт':
        reply_text = "Сегодня прихожая!\n"\
                     "Протереть зеркало и стеклянную поверхность дверей\n"\
                     "Навести порядок в обуви\n"\
                     "Почистить все коврики пылесосом\n"\

    elif button_text == 'Ср':
        reply_text = "Сегодня ванная!\n"\
                     "Помыть ванную и раковину\n"\
                     "Протереть краны, мыльницу и все блестящие поверхности\n"\
                     "Помыть унитаз\n"\
                     "Стирка детского белья"

    elif button_text == 'Чт':
        reply_text = "Сегодня детская!\n"\
                     "Расставить аккуратно все на полочках, протереть пыль с сувениров\n"\
                     "Уборка на комп. столе Кости\n"\
                     "Протереть подоконник\n"\
                     "Стирка взрослой одежды"

    elif button_text == 'Пт':
        reply_text = "Сегодня чистим везде!\n"\
                     "Поменять постельное белье, повесить чистые полотенца в ванную\n"\
                     "Пропылесосить квартиру\n"\
                     "Протереть везде пыль\n"\
                     "Протереть подоконники"\
                     "Помыть полы"\
                     "Стирка постельного белья и полотенец"

    elif button_text == 'Сб':
        reply_text = "Сегодня окна!\n"\
                     "Помыть окна\n"\
                     "Помыть цветы и подстричь лишние листья\n"\
                     "Глажка постельного белья\n"

    elif button_text == 'Вс':
        reply_text = "Балкон!\n" \
                     "Пропылесосить балкон\n" \
                     "Выкинуть ненужное / сломаннное\n" \
                     "Навести порядок, если захламлено"

    else:
        reply_text = "Ничего не понятно, но очень интересно\n" \
                     "Попробуем еще раз?\n" \
                     "Используй команду \start в меню"

    await message.reply(reply_text, reply_markup=types.ReplyKeyboardRemove())
    # с сообщением отправляется types.ReplyKeyboardRemove(), чтобы скрыть клавиатуру


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

