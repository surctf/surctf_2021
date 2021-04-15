from flask import Flask, request, render_template_string
import random

greetings = ["Салам", "Шалом", "Добрый день", "Хай", "Алоха"]
SECRET_FLAG = "surctf_jinja_jinja_ninja_ninja"

INPUT_FORM = '''<form action="/" method="GET">
<label for="name"> Имя: <br></label>
<input type="text" id="name" name="name" placeholder="Вася"/>
<button type="sumbit"> Подобрать приветствие </button>
</form>'''

GREETINGS_TEMPLATE = "<p> Приветствие: '%s, %s'"

app = Flask(__name__)
app.secret_key = "secret_pecret"

@app.route("/", methods=["GET"])
def index():
    name = request.args.get("name")
    
    if name:
        if "." in name:
            return "Хаха блин, ты реально думаешь, что это так ломается, блин кекXDXDXDXD))))))00))0))0)"

        return render_template_string(INPUT_FORM + (GREETINGS_TEMPLATE % (random.choice(greetings), name)))

    return INPUT_FORM

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1337, debug=True, threaded=True)