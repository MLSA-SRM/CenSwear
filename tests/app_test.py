from src.app import app, WORDLIST_URL, censor_symbols
import json
import os
import re
import requests
tester = app.test_client()

def test_index():
    response = tester.get("/", content_type="html/text")
    assert response.status_code == 200
    assert b"demo-area" in response.data
    assert b"demo-input" in response.data
    assert b"features-section" in response.data


def test_about():
    response = tester.get("/about", content_type="html/text")
    assert response.status_code == 200
    assert b"Developers who made the api" in response.data

def test_filter():
    response = tester.post('/filter', json={'text':'test_swear'}) #Test if swear words are getting censored as expected.
    assert response.status_code == 200
    assert re.match(f'[{censor_symbols}]*', str(response.json['result']))

    response = tester.post('/filter', json={'text':'clean_text'}) #Test for clean strings.
    assert response.status_code == 200
    assert response.json['result'] == 'clean_text'

    response = tester.post('/filter', json={'text':'test_swe ar'}) #Test for secondry run where whitespaces are ignored.
    assert response.status_code == 200
    assert re.match(f'[{censor_symbols} ]*', str(response.json['result']))
