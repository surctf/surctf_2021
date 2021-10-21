# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect

app = Flask(__name__)

flag = 'surctf_mechanistically'.replace('_', '-')
symbols = [chr(i) for i in range(97, 123)]
symbols.append('-')

var_template = '/'
var_templates = []
for i in flag:
    var_template = f'{var_template}{i}/'
    var_templates.append(var_template)


@app.route('/')
@app.route(var_templates[0])
@app.route(var_templates[1])
@app.route(var_templates[2])
@app.route(var_templates[3])
@app.route(var_templates[4])
@app.route(var_templates[5])
@app.route(var_templates[6])
@app.route(var_templates[7])
@app.route(var_templates[8])
@app.route(var_templates[9])
@app.route(var_templates[10])
@app.route(var_templates[11])
@app.route(var_templates[12])
@app.route(var_templates[13])
@app.route(var_templates[14])
@app.route(var_templates[15])
@app.route(var_templates[16])
@app.route(var_templates[17])
@app.route(var_templates[18])
@app.route(var_templates[19])
@app.route(var_templates[20])
def index():
    return render_template('index.html', symbols=symbols, s=request.url)


@app.route(var_templates[21])
def flag_page():
    return "<h1>UH TY, ETO MOYA SECRET PAPKA</h1>"


@app.errorhandler(404)
def not_found(e):
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
