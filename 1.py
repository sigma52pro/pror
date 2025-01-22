import random
from io import StringIO
from telebot import TeleBot
from telebot import formatting
from telebot import custom_filters
from telebot import types
from telebot import util
import config
import jokes
import messages
import my_fillters
import currencies
from comands import default_commands
from currencies import default_currency_key
bot = TeleBot(config.BOT_TOKEN)
bot.add_custom_filter(custom_filters.TextMatchFilter())
# bot.add_custom_filter(custom_filters.TextContainsFilter())
bot.add_custom_filter(custom_filters.ForwardFilter())
bot.add_custom_filter(custom_filters.IsReplyFilter())
bot.add_custom_filter(my_fillters.IsUserAdminOfBot())
bot.add_custom_filter(my_fillters.ContainsWordFillter())
bot.add_custom_filter(my_fillters.HasEntitiesFilter())
bot.add_custom_filter(my_fillters.ContainsOneOfWordsFilter())


chat_id = 6820204471
bot.send_message(chat_id, messages.stat_text, parse_mode='HTML')


@bot.message_handler(commands=['start'])
def handle_command_start(message: types.Message):
    # start_text = "<i>Привет!</i> Я работаю."
    bot.send_message(
        message.chat.id,
        messages.stat_text,
        parse_mode='HTML'
    )


@bot.message_handler(commands=['help'])
def handle_command_help(message: types.Message):
    bot.send_message(
        message.chat.id,
        messages.help_message
    )


@bot.message_handler(commands=['joke'])
def send_random_joke(message: types.Message):
    bot.send_message(
        message.chat.id,
        # (random.choice(jokes.jokes)),
        formatting.hcite(jokes.get_random_joke_text()),
        parse_mode='HTML'
    )


@bot.message_handler(commands=['joke2'])
def send_random_two_part_joke(message: types.Message):
    setup, delivery = jokes.get_two_text()
    text = formatting.format_text(
        formatting.escape_html(setup),
        formatting.hspoiler(delivery)
    )
    bot.send_message(
        message.chat.id,
        # (random.choice(jokes.jokes)),
        text=text,
        parse_mode='HTML'
    )


@bot.message_handler(commands=['dog_file'])
def send_dog_photo_from_disk(message: types.Message):
    photo_file = types.InputFile('pics/787ce43c509d69fc6b74bfea41e9734f.jpg')
    bot.send_photo(
        message.chat.id,
        photo=photo_file
    )


@bot.message_handler(commands=['dog_doc'])
def send_dog_as_doc(message: types.Message):
    photo_file = types.InputFile('pics/787ce43c509d69fc6b74bfea41e9734f.jpg')
    bot.send_document(
        chat_id=message.chat.id,
        document=photo_file
    )


@bot.message_handler(commands=['dog'])
def send_dog_pic_file_id(message: types.Message):
    bot.send_photo(
        message.chat.id,
        photo=config.DOG_PIC_FILE_ID
    )


@bot.message_handler(commands=['dogs_doc'])
def send_dogs_photo_as_file(message: types.Message):
    bot.send_document(
        chat_id=message.chat.id,
        document=config.DOG_URL
    )


@bot.message_handler(commands=['dogs'])
def send_dogs_photo(message: types.Message):
    bot.send_photo(
        chat_id=message.chat.id,
        photo=config.DOG_URL,
        reply_to_message_id=message.id
    )


@bot.message_handler(commands=['file'])
def send_text_file(message: types.Message):
    file_doc = types.InputFile('text.txt')
    bot.send_document(
        chat_id=message.chat.id,
        document=file_doc
    )


@bot.message_handler(commands=['text'], is_forwarded=True)
def hadle_forwareded_text_comands(message: types.Message):
    bot.send_message(
        chat_id=message.chat.id,
        text=messages.forward_comands
    )


@bot.message_handler(commands=['text'])
def send_text_doc_from_memory(message: types.Message):
    file = StringIO()
    file.write('Hello world!\n')
    file.write('Your random number')
    file.write(str(random.randint(1, 100)))
    file.seek(0)
    file_text_doc = types.InputFile(file)
    bot.send_document(
        chat_id=message.chat.id,
        document=file_text_doc,
        visible_file_name='Your random number.txt'
    )


# noinspection PyTypeChecker,PyArgumentList
@bot.message_handler(commands=['me'])
def send_text_from_user(message: types.Message):
    file = StringIO()
    file.write('User info:\n')
    file.write('Usre id: ')
    file.write(str(message.from_user.id))
    file.write("\n")
    file.write('First name: ')
    file.write(message.from_user.first_name or "N/A")
    file.write("\n")
    file.write('Last name: ')
    file.write(message.from_user.last_name or "N/A")
    file.write("\n")
    file.write('username: ')
    file.write(message.from_user.username or "N/A")
    file.write("\n")
    file.seek(0)
    # file_text_doc = types.InputFile(file)
    file_text_doc = types.InputFile(file, 'user_info.txt')
    bot.send_document(
        chat_id=message.chat.id,
        document=file_text_doc,
        visible_file_name="your info.txt",
        caption=messages.user_info_caption
    )


@bot.message_handler(commands=["secret"], is_bot_admin=True)
def admin_secret(message: types.Message):
    bot.send_message(
        message.chat.id,
        text=messages.secret_admin
    )


@bot.message_handler(commands=["secret"], is_bot_admin=False)
def not_admin_secret(message: types.Message):
    bot.send_message(
        message.chat.id,
        text=messages.secret_not_admin
    )


@bot.message_handler(commands=["md"])
def send_markdown_message(message: types.Message):
    bot.send_message(
        chat_id=message.chat.id,
        text=messages.markdown_text,
        parse_mode='MarkdownV2'
    )


@bot.message_handler(commands=["html"])
def send_html_message(message: types.Message):
    bot.send_message(
        chat_id=message.chat.id,
        text=messages.html_text,
        parse_mode='HTML'
    )


def handle_no_commands_argument(message: types.Message):
    return not util.extract_arguments(message.text)


@bot.message_handler(commands=["cvt"],func=handle_no_commands_argument)
def handle_cvt_no_argument(message: types.Message):
    bot.send_message(
        chat_id=message.chat.id,
        text=messages.cvt_how_to,
        parse_mode='HTML'
    )

@bot.message_handler(commands=["cvt"])
def handle_cvt_currency(message: types.Message):
    arguments = util.extract_arguments(message.text)
    amount, _, currency = arguments.partition(" ")

    if not amount.isdigit():
        error_text = formatting.format_text(
            messages.invalid_argument_text,
            formatting.hcode(arguments),
            messages.cvt_how_to,
        )
        bot.send_message(
            chat_id=message.chat.id,
            text=error_text,
            parse_mode="HTML",
        )
        return

    currency = currency.strip()
    default_currency = "RUB"

    user_data = bot.current_states.get_data(
        chat_id=message.chat.id,
        user_id=message.from_user.id,
    )
    if user_data and default_currency_key in user_data:
        default_currency = user_data[default_currency_key]

    currency_from, currency_to = currencies.get_currencies_names(
        currency=currency,
        default_to=default_currency,
    )
    ratio = currencies.get_currency_ratio(
        from_currency=currency_from,
        to_currency=currency_to,
    )
    if ratio == currencies.ERROR_VALUE:
        bot.send_message(
            chat_id=message.chat.id,
            text=messages.error_fetching_currencies_text,
        )
        return
    if ratio in {
        currencies.ERROR_CURRENCY_NOT_FOUND,
        currencies.ERROR_CURRENCY_INVALID,
    }:
        bad_currency = currency_from
        if ratio == currencies.ERROR_CURRENCY_INVALID:
            bad_currency = currency_to
        bot.send_message(
            chat_id=message.chat.id,
            text=messages.error_no_such_currency.format(
                currency=formatting.hcode(bad_currency),
            ),
            parse_mode="HTML",
        )
        return

    from_amount = int(amount)
    result_amount = from_amount * ratio
    bot.send_message(
        chat_id=message.chat.id,
        text=messages.format_currency_convert_message(
            from_currency=currency_from,
            to_currency=currency_to,
            from_amount=from_amount,
            to_amount=result_amount,
        ),
        parse_mode="HTML",
    )


@bot.message_handler(commands=["jpy_to_rub"])
def convert_jpy_to_rub(message: types.Message):
    arguments = util.extract_arguments(message.text)
    if not arguments:
        bot.send_message(
            chat_id=message.chat.id,
            text=messages.cvt_jpy_to_rub_how_to,
            parse_mode="HTML",
        )
        return

    if not arguments.isdigit():
        text = formatting.format_text(
            formatting.format_text(
                messages.invalid_argument_text,
                formatting.hcode(arguments),
                separator=" ",
            ),
            messages.cvt_jpy_to_rub_how_to,
        )
        bot.send_message(
            chat_id=message.chat.id,
            text=text,
            parse_mode="HTML",
        )
        return

    jpy_amount = int(arguments)
    ratio = currencies.get_jpy_to_rub_ratio()
    rub_amount = jpy_amount * ratio

    bot.send_message(
        chat_id=message.chat.id,
        text=messages.format_jpy_to_rub_message(
            jpy_amount=jpy_amount,
            rub_amount=rub_amount,
        ),
        parse_mode="HTML",
    )


@bot.message_handler(
    commands=["set_my_currency"],
    func=handle_no_commands_argument,
)
def handle_no_args_to_set_my_currency(message: types.Message):
    bot.send_message(
        chat_id=message.chat.id,
        text=messages.set_my_currency_help_message_text,
        parse_mode="HTML",
    )


def set_selected_currency(
    message: types.Message,
    data_key: str,
    set_currency_success_message: str,
):
    currency = util.extract_arguments(message.text) or ""
    if not currencies.is_currency_available(currency):
        bot.send_message(
            chat_id=message.chat.id,
            text=messages.error_no_such_currency.format(
                currency=formatting.hcode(currency),
            ),
            parse_mode="HTML",
        )
        return

    if (
        bot.get_state(
            user_id=message.from_user.id,
            chat_id=message.chat.id,
        )
        is None
    ):
        bot.set_state(
            user_id=message.from_user.id,
            chat_id=message.chat.id,
            state=0,
        )

    bot.add_data(
        user_id=message.from_user.id,
        chat_id=message.chat.id,
        **{data_key: currency},
    )
    bot.send_message(
        chat_id=message.chat.id,
        text=set_currency_success_message.format(
            currency=formatting.hcode(currency.upper()),
        ),
        parse_mode="HTML",
    )


@bot.message_handler(commands=["set_my_currency"])
def handle_set_my_currency(message: types.Message):
    set_selected_currency(
        message=message,
        data_key=currencies.default_currency_key,
        set_currency_success_message=messages.set_my_currency_success_message_text,
    )


def current_chat_is_not_user_chat(message: types.Message):
    return message.chat.id != message.from_user.id





@bot.message_handler(commands=["chat_id"])
def handle_chat_id_request(message: types.Message):
        text = formatting.format_text(
            formatting.format_text(
                "Айди чата:",
                formatting.hcode(str(message.chat.id)),
                separator=" ",
            ),
            formatting.format_text(
                "Айди отправителя:",
                formatting.hcode(str(message.from_user.id)),
                separator=" ",
            ),
        )
        if message.reply_to_message:
            text = formatting.format_text(
                text,
                formatting.format_text(
                    "Отвечено на сообщение от",
                    formatting.hcode(str(message.reply_to_message.from_user.id)),
                )
            )
        bot.send_message(
            message.chat.id,
            text=text,
            parse_mode="HTML"
        )










@bot.message_handler(text=custom_filters.TextFilter(
    contains=['погода'],
    ignore_case=True
))
def handle_requwest(message: types.Message):
    bot.send_message(
        message.chat.id,
        text=formatting.mbold('Хорошая погода!'),
        parse_mode='MarkdownV2'
    )


def cat_caption(message: types.Message):
    return message.caption and 'кот' in message.caption.lower()


@bot.message_handler(content_types=['photo'], contains_word='кот')
def handle_photo(message: types.Message):
    bot.send_message(
        chat_id=message.chat.id,
        text=messages.cat,
        reply_to_message_id=message.id
    )


@bot.message_handler(content_types=['photo'])
def handle_photo(message: types.Message):
    photo_file_id = message.photo[-1].file_id
    caption_text = 'Классное фото'
    if message.caption:
        caption_text += " Подпись:\n" + message.caption
    # bot.send_message(chat_id=message.chat.id,text='Какое класное фото!',reply_to_message_id=message.id)
    bot.send_photo(
        message.chat.id,
        photo=photo_file_id,
        reply_to_message_id=message.id,
        caption=caption_text
    )


@bot.message_handler(content_types=['sticker'])
def handle_sticker(message: types.Message):
    # bot.send_message(chat_id=message.chat.id,text='Крутой стикер!',reply_to_message_id=message.id)
    bot.send_sticker(
        chat_id=message.chat.id,
        sticker=message.sticker.file_id,
        reply_to_message_id=message.id,
    )


def hi_text(message: types.Message):
    return message.text and 'привет' in message.text.lower()


@bot.message_handler(contains_word='привет')
def hi_message_text(message: types.Message):
    bot.send_message(
        chat_id=message.chat.id,
        text='Привет!'
    )


content_type_ru = {
    'text': 'текст',
    'photo': 'фото',
    'sticker': 'стикер',
    'file': 'файл',
    'document': 'докумет'
}

@bot.message_handler(contains_word="как дела")
def reply_whats_up(message: types.Message):
    bot.send_message(
        message.chat.id,
        text=messages.whatsup_message_text,
    )

@bot.message_handler(contains_one_of_words=["пока", "до свидания"])
def reply_bye(message: types.Message):
    bot.send_message(
        message.chat.id,
        text=formatting.mbold(messages.goodbye_message_text),
        parse_mode="MarkdownV2",)


@bot.message_handler(is_reply=True)
def reply_echo_text(message: types.Message):
    message_type = message.reply_to_message.content_type
    if message_type in content_type_ru:
        message_type = content_type_ru[message_type]
    text = ('Вы <b>ответили</b> на это <u>сообщение</u>,'
            f'тип - {formatting.escape_html(message_type)}.')
    bot.send_message(
        message.chat.id,
        text=text,
        reply_to_message_id=message.reply_to_message.id,
        parse_mode='HTML'
    )


@bot.message_handler(has_entities=True, contains_word="проверка")
def echo_and_show_entities(message: types.Message):
    named_entities = {entity.type for entity in message.entities}
    text = formatting.format_text(
        message.text,
        f"Entities: {', '.join(named_entities)}",
        separator="\n\n",
    )
    bot.send_message(
        chat_id=message.chat.id,
        text=text,
        entities=message.entities,
    )

@bot.message_handler(has_entities=True)
def echo_and_show_entities_2(message: types.Message):
        entity_names = {
            formatting.hcode(entity.type)
            for entity in message.entities
        }
        text = formatting.format_text(
            message.html_text,
            formatting.format_text(
                "Entities:",
                ", ".join(entity_names),
                separator=" ",
            ),
            separator="\n\n",
        )
        bot.send_message(
            chat_id=message.chat.id,
            text=text,
            parse_mode="HTML",
        )


@bot.message_handler(contains_word='проверка')
def copy_message(message: types.Message):
    bot.copy_message(
        chat_id=message.chat.id,
        from_chat_id=message.chat.id,
        message_id=message.id
    )


@bot.message_handler()
def echo_messange(message: types.Message):
    text = message.text
    # if 'как дела' in text.lower():
    #     text = 'Хорошо!А у вас как дела?'
    # elif 'пока' in text.lower() or 'до свидания' in text.lower():
    #     text = 'До новых встреч!'
    # if message.entities:
    #     print('message entities:')
    #     for entity in message.entities:
    #         print(entity)
    bot.send_message(
        message.chat.id,
        text=text,
        entities=message.entities
    )


if __name__ == '__main__':
    bot.set_my_commands(default_commands)
    bot.infinity_polling(skip_pending=True)
