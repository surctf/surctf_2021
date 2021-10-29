# -*- coding: utf-8 -*-

from flask import Flask, render_template, url_for, request

app = Flask(__name__)

correct_adr = "Ул. 30 лет Победы 37/1"


def check(adr):
    global correct_adr
    if adr == correct_adr:
        return True


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    out = None
    if request.method == 'POST':
        form = request.form
        answer = form.get('address')
        if check(answer):
            out = "Ответ правильный, Ваш флаг: surctf_fezwect_gde_ti_ya_tebya_ne_mogu_nayti"
        else:
            out = "Ответ неверный"
    return render_template('index.html', out=out)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1339)