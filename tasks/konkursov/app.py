# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect, url_for, make_response
from db_helper import rand_konkurs, get_konkurs


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        konkurs_hash = request.cookies.get('konkurs')
        if not konkurs_hash:
            konkurs = None
        else:
            konkurs = get_konkurs(konkurs_hash)
        resp = make_response(render_template('index.html', konkurs=konkurs))
        return resp
    elif request.method == 'POST':
        konkurs_hash = rand_konkurs()
        resp = make_response(redirect(url_for('index')))
        resp.set_cookie('konkurs', konkurs_hash)
        return resp


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=1338)
