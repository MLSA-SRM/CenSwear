import random
import re

from flask import Flask, redirect, render_template, request

app = Flask(__name__)

# app.config[''] = ''
# app.config[''] = ''

filter_words = [r'test_swear', r'^[a@][s\$][s\$]$', r'[a@][s\$][s\$]h[o0][l1][e3][s\$]?', r'b[a@][s\$][t\+][a@]rd', r'b[e3][a@][s\$][t\+][i1][a@]?[l1]([i1][t\+]y)?', r'b[e3][a@][s\$][t\+][i1][l1][i1][t\+]y', r'b[e3][s\$][t\+][i1][a@][l1]([i1][t\+]y)?', r'b[i1][t\+]ch[s\$]?', r'b[i1][t\+]ch[e3]r[s\$]?', r'b[i1][t\+]ch[e3][s\$]', r'b[i1][t\+]ch[i1]ng?', r'b[l1][o0]wj[o0]b[s\$]?', r'c[l1][i1][t\+]', r'^(c|k|ck|q)[o0](c|k|ck|q)[s\$]?$', r'(c|k|ck|q)[o0](c|k|ck|q)[s\$]u', r'(c|k|ck|q)[o0](c|k|ck|q)[s\$]u(c|k|ck|q)[e3]d', r'(c|k|ck|q)[o0](c|k|ck|q)[s\$]u(c|k|ck|q)[e3]r', r'(c|k|ck|q)[o0](c|k|ck|q)[s\$]u(c|k|ck|q)[i1]ng', r'(c|k|ck|q)[o0](c|k|ck|q)[s\$]u(c|k|ck|q)[s\$]', r'^cum[s\$]?$', r'cumm??[e3]r', r'cumm?[i1]ngcock', r'(c|k|ck|q)um[s\$]h[o0][t\+]', r'(c|k|ck|q)un[i1][l1][i1]ngu[s\$]', r'(c|k|ck|q)un[i1][l1][l1][i1]ngu[s\$]', r'(c|k|ck|q)unn[i1][l1][i1]ngu[s\$]', r'(c|k|ck|q)un[t\+][s\$]?', r'(c|k|ck|q)un[t\+][l1][i1](c|k|ck|q)', r'(c|k|ck|q)un[t\+][l1][i1](c|k|ck|q)[e3]r', r'(c|k|ck|q)un[t\+][l1][i1](c|k|ck|q)[i1]ng', r'cyb[e3]r(ph|f)u(c|k|ck|q)', r'd[i1]ck', r'd[i1][l1]d[o0]', r'd[i1][l1]d[o0][s\$]',
                r'd[i1]n(c|k|ck|q)', r'd[i1]n(c|k|ck|q)[s\$]', r'[e3]j[a@]cu[l1]', r'(ph|f)[a@]g[s\$]?', r'(ph|f)[a@]gg[i1]ng', r'(ph|f)[a@]gg?[o0][t\+][s\$]?', r'(ph|f)[a@]gg[s\$]', r'(ph|f)[e3][l1][l1]?[a@][t\+][i1][o0]', r'(ph|f)u(c|k|ck|q)', r'(ph|f)u(c|k|ck|q)[s\$]?', r'g[a@]ngb[a@]ng[s\$]?', r'g[a@]ngb[a@]ng[e3]d', r'g[a@]y', r'h[o0]m?m[o0]', r'h[o0]rny', r'j[a@](c|k|ck|q)\-?[o0](ph|f)(ph|f)?', r'j[e3]rk\-?[o0](ph|f)(ph|f)?', r'j[i1][s\$z][s\$z]?m?', r'[ck][o0]ndum[s\$]?', r'mast(e|ur)b(8|ait|ate)', r'n[i1]gg?[e3]r[s\$]?', r'[o0]rg[a@][s\$][i1]m[s\$]?', r'[o0]rg[a@][s\$]m[s\$]?', r'p[e3]nn?[i1][s\$]', r'p[i1][s\$][s\$]', r'p[i1][s\$][s\$][o0](ph|f)(ph|f)', r'p[o0]rn', r'p[o0]rn[o0][s\$]?', r'p[o0]rn[o0]gr[a@]phy', r'pr[i1]ck[s\$]?', r'pu[s\$][s\$][i1][e3][s\$]', r'pu[s\$][s\$]y[s\$]?', r'[s\$][e3]x', r'[s\$]h[i1][t\+][s\$]?', r'[s\$][l1]u[t\+][s\$]?', r'[s\$]mu[t\+][s\$]?', r'[s\$]punk[s\$]?', r'[t\+]w[a@][t\+][s\$]?', r'ra[mn]d[iw]\w*', r'la[uw]d[ae]', r'bhosdi\w*', r'bhen\s*k\w*\s*\w*', r'ch[uo]*t', r'(?:behen|madar|behan|beti|bhen)\w+', r'lode', r'bsdk', r'nig+er', r'hentai', r'chu+s+', ]


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
