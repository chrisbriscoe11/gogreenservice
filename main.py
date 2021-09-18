import requests

from flask import Flask, json, request

api = Flask(__name__)

x = 0
y = 0
z = 0
posscore = 0
negscore = 0


def count_words(url, word):
    r = requests.get(url).text
    return r.count(word)


def main(page):
    global x, y, z, posscore, negscore
    url = 'https://en.wikipedia.org/wiki/' + page

    poswords = ['green', 'energy efficient', 'electric cars', 'environmental', 'friendly', 'environmentally friendly',
                'good', 'efficient', 'LEDs', 'tree', 'vegan', 'reduce waste', 'home automation', 'net zero emissions',
                'net zero carbon', 'reusable', 'recycle', 'Earth', 'ride share', 'public transport', 'net zero',
                'biofuel',
                'natural', 'carbon neutral', 'vegetarian', 'soylent', 'energy conservation', 'health', 'smart',
                'energy clean']

    negwords = ['global warming', 'oil', 'climate change', 'co2', 'coal', 'gas', 'jeans', 'jean', 'plastic straws',
                'wet wipes', 'natural gas', 'deforestation', 'harmful', 'evil', 'bad', 'negative', 'wasteful', 'dairy',
                'guns', 'trash', 'tampons', 'pads', 'bottled water', 'fast fashion', 'single use', 'weed killer',
                'weed killers', 'importing goods', '60 watt lightbulbs', 'paper towels', 'banking documents',
                'lead paint', 'damage', 'damaging', 'republican', 'carbon negative', 'health concern',
                'health concerns']

    for word in poswords:
        count = count_words(url, word)
        x = x + count
        print('\nUrl: {}\ncontains {} occurrences of word: {}'.format(url, count, word))
    print('positive score:', x)

    for word in negwords:
        count = count_words(url, word)
        y = y + count
        print('\nUrl: {}\ncontains {} occurrences of word: {}'.format(url, count, word))
        z = x + y
    posscore = str(round(((x / z) * 100), 2)) + "%"
    negscore = str(round(((y / z) * 100), 2)) + "%"

    print('\npositive score:', x)
    print('negative score:', y)
    print('total score:', z)
    print('thumbs up score:', posscore)
    print('thumbs down score:', negscore)


@api.route('/wordscores', methods=['GET'])
def get_wordscores():
    page = request.args.get('page')
    main(page)
    return json.dumps({"positiveScore": x, "negativeScore": y, "totalScore": z, "thumbsUpScore": posscore,
                       "thumbsDownScore": negscore})


if __name__ == '__main__':
    api.run()
