from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='💸фарм💸'),
                                     KeyboardButton(text='🛒купить🛒')],
                                     [KeyboardButton(text='👜Корзина👜'),
                                     KeyboardButton(text='💰баланс💰')],
                                     [KeyboardButton(text='🪙монета🪙'),
                                     KeyboardButton(text='⚙️настройки⚙️')],
                                     [KeyboardButton(text='прочее...'),
                                     KeyboardButton(text='мини-игры')]],
                           resize_keyboard=True,
                           input_field_placeholder='Выберите пункт меню...')


catalog = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='🍌банан🍌', callback_data='t-shirt')],
    [InlineKeyboardButton(text='🍏яблоко🍏', callback_data='sneakers')],
    [InlineKeyboardButton(text='🍐груша🍐', callback_data='cap')]])
referal = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='👨мои рефералы👨', callback_data='moiref')],
    [InlineKeyboardButton(text='🏆конкурс рефералов🏆', callback_data='refi')]])
obmen = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='💳пополнение баланса💳', callback_data='vvod')],
    [InlineKeyboardButton(text='💰вывод средств💰', callback_data='vivod')]])
kodrefa = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='ввести код реферала', callback_data='refcod')]])
farm = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='🏆🏆🏆', callback_data='tik')],
    [InlineKeyboardButton(text='собрать трофеи', callback_data='sobrat')]])
igra = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Рулетка', callback_data='igar1')],
    [InlineKeyboardButton(text='Снайпер', callback_data='igar2')]])
kolvo = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='10', callback_data='kolvo1')],
    [InlineKeyboardButton(text='30', callback_data='kolvo2')],
    [InlineKeyboardButton(text='50', callback_data='kolvo3')]])
denga = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='2', callback_data='denga1')],
    [InlineKeyboardButton(text='5', callback_data='denga2')],
    [InlineKeyboardButton(text='15', callback_data='denga3')]])

get_number = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Отправить номер',
                                                           request_contact=True)]],
                                 resize_keyboard=True)