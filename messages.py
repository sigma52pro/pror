from telebot import formatting
stat_text = "<i>Привет!</i> Я работаю."


help_message = """Привет вот доступные команды:
/start - начало работы с ботом 
/help - помощь (это сообщение)
/joke - случайная шутка
/jpy_to_rub 100 - конвертировать 100 JPY в RUB
/cvt 100 JPY - конвертировать 100 JPY в RUB
/cvt 100 JPY IDR - конвертировать 100 JPY в IDR
/set_my_currency RUB - установить целевую валюту
Примечание:это бот отправит то же сообщениие что и вы 
"""
forward_comands = "Не пересылайте команды.Это может быть опасно!"
cat = 'Какой класный кот'
whatsup_message_text = 'Хорошо,а у вас?'
goodbye_message_text = "До новых встреч!"
secret_admin = 'Вот ваше секретное слово:банан'
secret_not_admin = 'Вам сюда нельзя.Вы не админ'
user_info_caption ="Ваша информация в файле "
cvt_help_message = "Пожалуста, укажите аргумент для конвертации,например"
error_no_such_currency = "Неизвестная валюта {currency}, укажите существующую."
set_my_currency_help_message_text = formatting.format_text(
    "Пожалуйста, укажите выбранную валюту. Например:",
    formatting.hcode("/set_my_currency RUB"),

)
set_my_currency_success_message_text = formatting.format_text(
    "Успешно установлена валюта по умолчанию:",
    "{currency}",
)
convert_jpy_to_rubjpy_to_rub_how_to = formatting.format_text(
    cvt_help_message,
    formatting.hcode("/jpy_to_rub 100"),
)

cvt_how_to = formatting.format_text(
    cvt_help_message,
    formatting.hcode("/cvt 100 JPY"),
)


invalid_argument_text = "Неправильный аргумнет:"

def format_currency_convert_message(
    from_currency,
    to_currency,
    from_amount,
    to_amount
):
    return formatting.format_text(
        formatting.hcode(f"{from_amount:,}"),
        f"{from_currency.upper()} это примерно",
        formatting.hcode(f"{to_amount:,.2f}"),
        to_currency.upper(),
        separator=" "
    )

def formating_jpy_to_rub(jpy_amount,rub_amount):
    return format_currency_convert_message(
        from_currency="JPY",
        to_currency="RUB",
        from_amount=jpy_amount,
        to_amount=rub_amount
    )
    # return formatting.format_text(
    #     formatting.hcode(f"{jpy_amount:,}"),
    #     "JPY это примерно",
    #     formatting.hcode(f"{rub_amount:,.2f}"),
    #     "RUB",
    #     separator=" "
    # )




markdown_text = """*bold \*text*
_italic \_text_
__underline__
~strikethrough~
||spoiler||
*bold _italic bold ~italic bold strikethrough ||italic bold strikethrough spoiler||~ __underline italic bold___ bold*
[inline URL](http://www.example.com/)
[inline mention of a user](tg://user?id=6820204471)
![👍](tg://emoji?id=5368324170671202286)
`inline fixed-width code`
```
pre-formatted fixed-width code block
```
```python
pre-formatted fixed-width code block written in the Python programming language

@bot.message_handler(commands=["md"])
def send_markdown_message(message: types.Message):
    bot.send_message(
        chat_id=message.chat.id,
        text=messages.markdown_text,
        parse_mode='MarkdownV2'
        )
```
>Block quotation started
>Block quotation continued
>The last line of the block quotation
**>The expandable block quotation started right after the previous block quotation
>It is separated from the previous block quotation by an empty bold entity

>Expandable block quotation continued

>Hidden by default part of the expandable block quotation started

>Expandable block quotation continued

>The last line of the expandable block quotation with the expandability mark||"""

html_text = """<b>bold</b>, <strong>bold</strong>
<i>italic</i>, <em>italic</em>
<u>underline</u>, <ins>underline</ins>
<s>strikethrough</s>, <strike>strikethrough</strike>, <del>strikethrough</del>
<span class="tg-spoiler">spoiler</span>, <tg-spoiler>spoiler</tg-spoiler>
<b>bold <i>italic bold <s>italic bold strikethrough <span class="tg-spoiler">italic bold strikethrough spoiler</span></s> <u>underline italic bold</u></i> bold</b>
<a href="http://www.example.com/">inline URL</a>
<a href="tg://user?id=6820204471">inline mention of a user</a>
<tg-emoji emoji-id="5368324170671202286">👍</tg-emoji>
<code>inline fixed-width code</code>
<pre>pre-formatted fixed-width code block</pre>
<pre><code class="language-python">
#pre-formatted fixed-width code block written in the Python programming language
@bot.message_handler(commands=["md"])
def send_markdown_message(message: types.Message):
    bot.send_message(
        chat_id=message.chat.id,
        text=messages.markdown_text,
        parse_mode='MarkdownV2'
    )
</code></pre>
<blockquote>Block 
quotation started\nBlock quotation continued\nThe last line of the block quotation</blockquote>
<blockquote>

Block quotation started
Block quotation continued
The last line of the block quotation
</blockquote>
<blockquote expandable>Expandable block quotation started\nExpandable block quotation continued\nExpandable block quotation continued\nHidden by default part of the block quotation started\nExpandable block quotation continued\nThe last line of the block quotation</blockquote>"""


def start_text():
    return None


def help_text():
    return None