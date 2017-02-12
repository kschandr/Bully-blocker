#bullyblocker.py

from flask import Flask, render_template
import requests
import json

app = Flask(__name__, template_folder = '.')

@app.route('/')
def render():
    return render_template('index.html')

@app.route('/bullyblocker')
def homepage():
    params = {
            'api_key' : 'trSXSGm9BOHM',
            }
    r = requests.get('https://www.parsehub.com/api/v2/projects/tbE9pS_fnY3s/last_ready_/data',
            params = params)
    return render_template('index.html', data1 = json.loads(r.text)['data1'])

if __name__=='__main__':
    app.run(host ='0.0.0.0', debug = True)
