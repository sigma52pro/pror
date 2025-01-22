import requests


jokes = ['Есть много шуток о безработных. К сожалению, ни одна из них не работает.',
         'Сделал сайт для сирот. У него нет домашней страницы.',
         'Хорошие мамы позволяют вам облизать венчики миксера. Великие мамы сначала его выключают.',
         'Я воспитывался как единственный ребенок в семье. Это очень расстраивало мою старшую сестру.',
         'Неловкие ситуации, токсичные взаимоотношения в семье становятся частым источником анекдотов.']
JOKE_API_BASE_URL ='https://v2.jokeapi.dev/joke/Programming,Pun'
#JOKE_URL = 'https://v2.jokeapi.dev/joke/Programming,Pun?blacklistFlags=nsfw,religious,political,racist,sexist,explicit&type=single'
#JOKE_TWO_URL = 'https://v2.jokeapi.dev/joke/Programming,Pun?blacklistFlags=nsfw,religious,political,racist,sexist,explicit'


def get_joke(joke_type: str | None = None) -> dict | None:
    url = JOKE_API_BASE_URL
    params ={
        'lang':'en',
        'blacklistFlags':'nsfw,religious,political,racist,sexist,explicit',
        'type':'single',
    }
    if joke_type:
        params['type'] = joke_type
    response =requests.get(url,params=params)

    if response.status_code != 200:
        return
    json_data: dict = response.json()
    if json_data.get('error'):
        return

    return json_data

def get_random_joke_text():
    json_data =get_joke('single')
    if not json_data:
        return 'Error'

    return json_data['joke']


def get_two_text():
    json_data = get_joke('twopart')
    if not json_data:
        return 'Error'

    return json_data['setup'],json_data['delivery']


def get_two_part_joke_texts():
    return None