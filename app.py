# coding=utf-8
from flask import (
    Flask,
    render_template,
    url_for,
    request,
    redirect,
    session,
)

from hscard_version import version
import json
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

f = open('data.json', 'r', encoding='UTF-8')
data = f.read()
f.close()
data2 = json.loads(data)


@app.route('/')
def index():
    for v in version:
        print(v)
    return render_template('index.html', ver=version)


@app.route('/version/<v_name>')
def ver(v_name):
    ll = []
    dt = {}

    for i in data2:
        try:
            if i['set'] == v_name:
                ll.append(i['name'])
                dt[i['name']] = i['id']

        except:
            pass
    length = len(ll)
    # print(dt)
    session['version'] = v_name
    return render_template('version.html', ll=ll, length=length, dt=dt,v_name=v_name)


# @app.route('/KARA')
# def KARA():
#     ll = []
#     dt = {}
#
#     for i in data2:
#         try:
#             if i['set'] == 'KARA':
#                 ll.append(i['name'])
#                 dt[i['name']] = i['id']
#
#         except:
#             pass
#     length = len(ll)
#     # print(dt)
#     session['version'] = 'KARA'
#
#     return render_template('KARA.html', ll=ll, length=length, dt=dt)


@app.route('/card/<cardid>')
def card(cardid):
    if session.get('version'):
        path = 'images/' + session['version'] + '/' + cardid
    return render_template('card.html', cardid=cardid, path=path, data2=data2)


if __name__ == '__main__':
    config = dict(
        debug=True,
        host='0.0.0.0',
        port=3000,
    )
    app.run(**config)
