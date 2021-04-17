from . import app

wordlist_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'wordlist.json')
filter_words = json.load(open(wordlist_path))

def filter_string(msg, sec_run=False):
    space_indexes = [m.start() for m in re.finditer(' ', msg)]
    if sec_run:
        msg = msg.replace(' ', '')
    for word in filter_words:
        if word.endswith(r'\w*') and sec_run:
            continue
        search = re.search(r'\s*{}'.format(word), msg, re.IGNORECASE)
        if search:
            print(msg, search.group(), word)
            cen = ''.join(
                random.choice(list('-')) for a in range(len(search.group())))
            msg = re.sub(r'({})'.format(word),
                         cen,
                         msg,
                         flags=re.IGNORECASE)
    # print(msg)
    if sec_run:
        for i in space_indexes:
            msg = msg[:i] + ' ' + msg[i:]
        return msg
    else:
        return filter_string(msg, sec_run=True)


@app.route('/')
def index():
    return render_template('landingPage.html')


@app.route('/wordlist')
def wordlist():
    return '<br>'.join(filter_words)


@app.route('/filter/<string>')
def filter(string):
    return filter_string(string)


if __name__ == "__main__":
    app.run(debug=True)
