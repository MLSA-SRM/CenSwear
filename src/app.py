import os
from dotenv import load_dotenv
import random
import re
import requests
from urllib.parse import unquote

from flask import Flask, json, redirect, render_template, request, url_for, jsonify, abort
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address


app = Flask(__name__)

limiter = Limiter(app,key_func=get_remote_address)

# os.chdir(os.path.dirname(os.path.abspath(__file__)))

load_dotenv()

WORDLIST_URL = os.environ['WORDLIST_URL']
filter_words = requests.get(WORDLIST_URL).json()

censor_symbols = '*'


def filter_string(msg, sec_run=False):
    if sec_run:
        space_indexes = [m.start() for m in re.finditer(' ', msg)]
        msg = msg.replace(' ', '')
        for word in filter_words:
            if word.endswith(r'\w*') and sec_run:
                continue
            search = re.search(r'\s*{}'.format(word), msg, re.IGNORECASE)
            if search:
                print('Run2', msg, search.group(), word)
                cen = ''.join(
                    random.choice(censor_symbols) for a in range(len(search.group())))
                msg = re.sub(r'({})'.format(word),
                             cen,
                             msg,
                             flags=re.IGNORECASE)
        for i in space_indexes:
            msg = msg[:i] + ' ' + msg[i:]

        return msg

    # print(msg)
    else:
        censor_indexes = []
        for word in filter_words:
            search = re.search(r'\s*({})'.format(word), msg, re.IGNORECASE)
            if search:
                print('Run_1 Start:', msg, search.group(), word,
                      search.start(1), search.end(1))
                censor_indexes.append((search.start(1), search.end(1)))
        for i in censor_indexes:
            msg = msg[:i[0]] + ''.join(random.choice(censor_symbols)
                                       for c in range(i[1]-i[0])) + msg[i[1]:]

        print('Run_1 End:', msg)
        return filter_string(msg, sec_run=True)


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/aboutus')
def aboutus():
    return render_template('about.html')

@app.route('/wordlist')
def wordlist():
    return '<br>'.join(filter_words)

@limiter.limit('120 per minute')
@app.route('/filter', methods=['GET', 'POST'])
def filter():
    if request.method == 'POST':
        if not request.json or not 'text' in request.json:
            abort(400)
        string = request.json.get("text", "")
    else:
        string = request.args.get("text", "")
    return jsonify({'result': filter_string(string)}), 200


if __name__ == "__main__":
    app.run(debug=True)
