from flask import Flask, render_template, url_for
from json import load

app = Flask(__name__)


@app.route('/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/list_prof/<mode>')
def list_prof(mode):
    with open('data/professions.json', encoding='utf8') as input_json:
        prof_mas = load(input_json)['professions']
    print(prof_mas)
    return render_template('list_professions.html', title='professions', massive=prof_mas, mode=mode)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
