from flask import Flask
from markupsafe import escape
import requests
from faker import Faker

app = Flask(__name__)

@app.route('/requirements')
def req():
    with open('requirements.txt') as a:
        return a.read().splitlines()

@app.route('/generate-users/<coun>')
def gene(coun):
    fake = Faker()
    fdic = {}
    l = escape(coun)
    for _ in range(int(l)):
        m = fake.email()
        n = fake.name()
        fdic[n] = m
    return fdic

@app.route('/mean')
def my():
    sc, h, w = 0, 0, 0
    with open('hw.csv') as a:
        for i in a:
            i = i.split(',')
            if len(i) == 3 and i[0].isdigit():
                sc += 1
                h += float(i[1])
                w += float(i[2])
    return {'Average Height': str(h/sc*2.54), 'Average Weight': str(w/sc*0.453592)}

@app.route('/space')
def cos():
    r = requests.get('http://api.open-notify.org/astros.json')
    return {'Astronauts in orbit': str(r.json()["number"])}



if __name__ == '__main__':
    app.run()
