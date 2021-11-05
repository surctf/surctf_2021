# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect

app = Flask(__name__)

flag = 'surctf_mechanical_way_is_not_a_legit_solution_but_you_could_try'.replace('_', '-')
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
@app.route(var_templates[21])
@app.route(var_templates[22])
@app.route(var_templates[23])
@app.route(var_templates[24])
@app.route(var_templates[25])
@app.route(var_templates[26])
@app.route(var_templates[27])
@app.route(var_templates[28])
@app.route(var_templates[29])
@app.route(var_templates[30])
@app.route(var_templates[31])
@app.route(var_templates[32])
@app.route(var_templates[33])
@app.route(var_templates[34])
@app.route(var_templates[35])
@app.route(var_templates[36])
@app.route(var_templates[37])
@app.route(var_templates[38])
@app.route(var_templates[39])
@app.route(var_templates[40])
@app.route(var_templates[41])
@app.route(var_templates[42])
@app.route(var_templates[43])
@app.route(var_templates[44])
@app.route(var_templates[45])
@app.route(var_templates[46])
@app.route(var_templates[47])
@app.route(var_templates[48])
@app.route(var_templates[49])
@app.route(var_templates[50])
@app.route(var_templates[51])
@app.route(var_templates[52])
@app.route(var_templates[53])
@app.route(var_templates[54])
@app.route(var_templates[55])
@app.route(var_templates[56])
@app.route(var_templates[57])
@app.route(var_templates[58])
@app.route(var_templates[59])
@app.route(var_templates[60])
@app.route(var_templates[61])
def index():
    return render_template('index.html', symbols=symbols, s=request.url)


@app.route(var_templates[62])
def flag_page():
    return "<h1>UH TY, ETO MOYA SECRET PAPKA</h1>"


@app.errorhandler(404)
def not_found(e):
    return redirect("/")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1336)
