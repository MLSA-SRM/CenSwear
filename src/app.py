import os
from dotenv import load_dotenv
import random
import re
import requests
import time 
from urllib.parse import unquote

from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

# os.chdir(os.path.dirname(os.path.abspath(__file__)))

load_dotenv()

WORDLIST_URL = os.environ['WORDLIST_URL']
filter_words = requests.get(WORDLIST_URL).json()

censor_symbols = '$#!*'

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


@app.route('/wordlist')
def wordlist():
    return '<br>'.join(filter_words)


@app.route('/filter/<string>',methods=['GET','POST'])
def filter(string):
    return filter_string(unquote(string))


if __name__ == "__main__":
    app.run(debug=True)
