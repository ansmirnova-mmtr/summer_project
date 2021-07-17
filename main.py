from flask_ngrok import run_with_ngrok
import sqlalchemy
import os
from flask import Flask, render_template, request, url_for
import urllib.request
from tqdm.notebook import tqdm
import six
import requests
import random
from bs4 import BeautifulSoup
import pandas as pd


def make_anek():
    book = ['http://anekdotov.net/anekdot/', 'http://anekdotov.net/coronavirus/',
            'http://anekdotov.net/anekdot/student/']
    url = book[random.randint(0, 2)]
    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')
    #  print(soup.prettify())

    cousines_html_block = soup.find_all('div', class_='anekdot')
    answer = cousines_html_block[random.randint(0, len(cousines_html_block))].text
    answer.replace('анекдoтoв.nеt', '')
    return answer


app = Flask(__name__)
run_with_ngrok(app)  # starts ngrok when the app is run


@app.route('/')
def start():
    answer = make_anek()
    return render_template('index.html', answer=answer)


@app.route('/matan', methods=['POST', 'GET'])
def matan():
    result = ''
    if (request.method == 'POST' and 'kr1' in request.form and 'kr2' in request.form
            and 'cr1' in request.form and 'cr2' in request.form
            and 'exam' in request.form):
        kr1 = float(request.form['kr1'])
        kr2 = float(request.form['kr2'])
        cr1 = float(request.form['cr1'])
        cr2 = float(request.form['cr2'])
        exam = float(request.form['exam'])
        result = 0.125 * (kr1 + kr2 + cr1 + cr2) + 0.5 * exam
    return render_template('matan.html', result=result)


@app.route('/acos', methods=['POST', 'GET'])
def acos():
    result = ''
    if (request.method == 'POST' and 'contest' in request.form and 'kr' in request.form
            and 'exam' in request.form):
        contest = float(request.form['contest'])
        kr = float(request.form['kr'])
        exam = float(request.form['exam'])
        result = 0.6 * (0.9 * contest + 0.1 * kr) + 0.4 * exam
    return render_template('acos.html', result=result)


@app.route('/twims', methods=['POST', 'GET'])
def twims():
    result = ''
    if (request.method == 'POST' and 'kr1' in request.form and 'kr2' in request.form
            and 'kl1' in request.form and 'kl2' in request.form
            and 'exam' in request.form and 'dz' in request.form):
        kr1 = float(request.form['kr1'])
        kr2 = float(request.form['kr2'])
        kl1 = float(request.form['kl1'])
        kl2 = float(request.form['kl2'])
        dz = float(request.form['dz'])
        exam = float(request.form['exam'])
        result = ((3 / 14) * (kr1 + kr2) + (3 / 14) * (kl1 + kl2) + (1 / 7) * dz) * 0.7 + 0.3 * exam
    return render_template('twims.html', result=result)


@app.route('/diff', methods=['POST', 'GET'])
def diff():
    result = ''
    if (request.method == 'POST' and 'kr' in request.form and 'dz' in request.form
            and 'exam' in request.form):
        kr = float(request.form['kr'])
        dz = float(request.form['dz'])
        exam = float(request.form['exam'])
        result = 0.3 * kr + 0.3 * dz + 0.4 * exam
    return render_template('diff.html', result=result)


app.run()
