import requests
import json
import threading
import xmltodict as xmltodict


def display():
    config = json.loads(open('config.json').read(), encoding='unicode_escape')
    threading.Timer(3.0, display).start()
    url = 'https://api.forismatic.com/api/1.0/?method=getQuote&' + "lang=" + config["lang"] + "&" + "format=" + config[
        "format"]
    r = requests.get(url)
    if config["format"] == "json":
        value = json.loads(r.content)
        print("QUOTES: {} and  QUOTESAUTHOR: {}".format(value.get('quoteText'), value.get('quoteAuthor')))
    else:
        value = xmltodict.parse(r.content)

        output_dict = json.loads(json.dumps(value))
        flattenReturn(output_dict)


def flattenReturn(input):
    output = {key: value for key, value in input.items() if type(value) != dict}
    for value in input.values():
        if type(value) == dict:
            output.update(value)
    for key, value in output.items():
        if key == 'quote':
            result = output[key]
            print("QUOTES: {} and  QUOTESAUTHOR: {}".format(result.get('quoteText'), result.get('quoteAuthor')))


display()
