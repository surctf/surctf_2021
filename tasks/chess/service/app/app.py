from flask import Flask, request, render_template, redirect, url_for, flash, make_response
from db_helper import UsersDB, GamesDB
from functools import wraps
import chess, chess.engine, sys
import random, os

users_db = UsersDB("data.db")
games_db = GamesDB("data.db")

if not users_db.table_exist():
    users_db.init()
if not games_db.table_exist():
    games_db.init()

if "win" not in sys.platform.lower():
    engine = chess.engine.SimpleEngine.popen_uci(os.path.join(os.path.dirname(__file__),"stockfish/stockfish_13_linux"))
else:
    engine = chess.engine.SimpleEngine.popen_uci(os.path.join(os.path.dirname(__file__), "stockfish/stockfish_13_win.exe"))

ENGINE_DEPTH = 3

app = Flask(__name__)
app.secret_key = "omgitsosecret"

def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if (request.cookies.get("token") and 
            users_db.get_user_by_token(request.cookies.get("token"))):
            return func(*args, **kwargs)
        
        return redirect(url_for("login"))

    return wrapper

def guest_only(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not (request.cookies.get("token") and 
            users_db.get_user_by_token(request.cookies.get("token"))):
            return func(*args, **kwargs)
        
        return redirect(url_for("game"))

    return wrapper

@app.route("/", methods=["GET"])
@app.route("/game", methods=["GET"])
@login_required
def game():
    token = request.cookies.get("token")

    user = users_db.get_user_by_token(token)
    game = games_db.get_game(token)
    if not game:
        game = games_db.new_game(token)

    board = chess.Board(game["fen"])

    return render_template("game.html", user=user, board_fen=board.fen())

@app.route("/move", methods=["POST"])
@login_required
def move():
    token = request.cookies.get("token")

    user = users_db.get_user_by_token(token)
    game = games_db.get_game(token)
    board = chess.Board(game["fen"])

    try:
        move = request.form.get("move")
        move = chess.Move.from_uci(move)
    except ValueError:
        flash("Неверный формат записи хода!")
        return render_template("game.html", user=user, board_fen=board.fen())

    if move in board.legal_moves:
        board.push(move)
        if board.is_game_over():
            users_db.increment_user_wins(user["token"])
            user = users_db.get_user_by_token(token)

            game = games_db.new_game(token)
            board = chess.Board(game["fen"])
            flash("Вы выйграли, началась новая игра!")

        else:
            result = engine.play(board, chess.engine.Limit(depth=ENGINE_DEPTH))
            board.push(result.move)
            if board.is_game_over():
                game = games_db.new_game(token)
                board = chess.Board(game["fen"])
                flash("Вы проиграли, началась новая игра!")
            else:
                games_db.update_game(token, board.fen())
    else:
        flash("Так сходить нельзя!")

    return render_template("game.html", user=user, board_fen=board.fen())

@app.route("/register", methods=["GET", "POST"])
@guest_only
def register():
    if request.method == 'POST':
        name = request.form.get("name")
        pwd = request.form.get("pwd")

        ret, err = users_db.add_user(name, pwd)
        if ret:
            flash(err)
            return render_template("register.html")

        token = err
        resp = make_response(redirect("/game"))
        resp.set_cookie("token", token)
        return resp

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
@guest_only
def login():
    if request.method == "POST":
        name = request.form.get("name")
        pwd = request.form.get("pwd")

        ret, err = users_db.login_user(name, pwd)
        if ret:
            flash(err)
            return render_template("login.html")

        token = err
        resp = make_response(redirect("/"))
        resp.set_cookie("token", token)
        return resp

    return render_template("login.html")

@app.route("/logout", methods=["GET", "POST"])
@login_required
def logout():
    resp = make_response(redirect("/login"))
    resp.set_cookie("token", '')
    return resp

