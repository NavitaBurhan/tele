from os import environ

from telebot.types import (
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

from _bot import bot

bot_name = environ.get('bot_name', 'Asisten DigitalOcean')


def start(d: Message):
    markup = InlineKeyboardMarkup(row_width=2)
    markup.add(
        InlineKeyboardButton(
            text='➕ Tambah akun',
            callback_data='add_account'
        ),
        InlineKeyboardButton(
            text='⚙️ Kelola akun',
            callback_data='manage_accounts'
        ),
        InlineKeyboardButton(
            text='💧 Buat droplets',
            callback_data='create_droplet'
        ),
        InlineKeyboardButton(
            text='🛠️ Kelola droplets',
            callback_data='manage_droplets'
        ),
    )
    t = f'Selamat Datang <b>{bot_name}</b> 👋\n\n' \
        '<b>Dev: @skynest_ofc</b> 👨‍💻\n' \
        '<b>Support: @skynest_official</b> 🛡️'
    bot.send_message(
        text=t,
        chat_id=d.from_user.id,
        parse_mode='HTML',
        reply_markup=markup
    )
