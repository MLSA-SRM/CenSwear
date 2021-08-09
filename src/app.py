import os
from dotenv import load_dotenv
import random
import re
import requests
from urllib.parse import unquote

from flask import Flask, json, redirect, render_template, request, url_for, jsonify, abort
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from six import class_types


app = Flask(__name__)

limiter = Limiter(app, key_func=get_remote_address)

load_dotenv()

WORDLIST_URL = os.environ['WORDLIST_URL']
CLEAN_WORDLIST_URL = os.environ.get('CLEAN_WORDLIST_URL')

if CLEAN_WORDLIST_URL:
    clean_wordlist = requests.get(CLEAN_WORDLIST_URL).text.split()
else:
    print('Clean Wordlist URL not provided.')
    clean_wordlist = []

wordlist = requests.get(WORDLIST_URL).json()

censor_symbols = '*'

print('Clean List:',len(clean_wordlist))
print('Filter List:',len(wordlist))

def first_run(s):
    censor_indices = []
    for word in wordlist:
        search = re.search(r'\b({})\b'.format(word), s, re.IGNORECASE)
        if search:
            print(search)
            censor_indices.append((search.start(1), search.end(1)))
            cen = ''.join(
                random.choice(censor_symbols) for a in range(len(search.group())))
            s = re.sub(r'({})'.format(word),
                       cen,
                       s,
                       flags=re.IGNORECASE)

    return s


def second_run(s):
    space_indices = [m.start() for m in re.finditer(' ', s)]
    s = s.replace(' ', '')
    for word in wordlist:
        if word.endswith(r'\w*'):
            continue
        search = re.search(r'{}'.format(word), s, re.IGNORECASE)
        if search:
            print(search)
            cen = ''.join(
                random.choice(censor_symbols) for a in range(len(search.group())))
            s = re.sub(r'({})'.format(word),
                       cen,
                       s,
                       flags=re.IGNORECASE)
    for i in space_indices:
        s = s[:i] + ' ' + s[i:]

    return s


def third_run(s, base):
    clean_indices = get_clean_indices(base)

    for i in clean_indices:
        s = s[:i] + base[i] + s[i+1:]
    return s


def censor(s, indices):
    for i in indices:
        s = s[:i[0]] + ''.join(random.choice(censor_symbols)
                               for c in range(i[1]-i[0])) + s[i[1]:]
    return s


def get_clean_indices(s):
    clean_indices = []
    words = s.split()
    words = list(set(words))
    for i in words:
        if len(i) < 3:
            continue
        if i.lower() in clean_wordlist:
            for m in re.finditer(i.lower(), s):
                clean_indices.extend(list(range(m.start(), m.end())))
    print(clean_indices)
    return clean_indices


def filter_string(s):
    base = s
    s = first_run(s)
    s = second_run(s)
    s = third_run(s, base)
    
    return s


@ app.route('/')
def index():
    return render_template('home.html')


@ app.route('/about')
def aboutus():
    return render_template('about.html')


@ limiter.limit('120 per minute')
@ app.route('/filter', methods=['GET', 'POST'])
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
