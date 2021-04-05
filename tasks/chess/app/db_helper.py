import sqlite3, bcrypt, hashlib, random

class UsersDB:
    def __init__(self, path):
        self.path = path

    def init(self):
        with self._get_con() as c:
            c.execute('''CREATE TABLE USERS
                          ([id] INTEGER PRIMARY KEY,
                          [name] text, 
                          [pwd] integer, 
                          [token] text,
                          [wins] integer)''')
        return 0

    def add_user(self, name, pwd):
        if self.get_user_by_name(name):
            return (1, "Пользователь с таким именем уже существует!")

        if len(pwd) < 8:
            return (1, "Придумай пароль получше!")

        pwd = bcrypt.hashpw(pwd.encode("utf-8"), bcrypt.gensalt())

        token = "%s_%s-%s" % (name, pwd, random.randint(0, 500000))
        token = hashlib.sha256(token.encode("utf-8")).hexdigest()
        
        with self._get_con() as c:
            c.cursor().execute("INSERT INTO USERS(name, pwd, token, wins) VALUES (?, ?, ?, ?)", (name, pwd, token, 0))

        return (0, token)

    def increment_user_wins(self, token):
        with self._get_con() as c:
            user = c.cursor().execute("UPDATE USERS SET wins=wins+1 WHERE token=?", (token, ))

    def get_user_by_name(self, name):
        keys = ("id", "name", "pwd", "token", "wins")

        with self._get_con() as c:
            user = c.cursor().execute("SELECT * FROM USERS WHERE name=?", (name, )).fetchone()
        return dict(( (keys[i], user[i]) for i in range(len(keys)) )) if user else user

    def get_user_by_token(self, token):
        keys = ("id", "name", "pwd", "token", "wins")

        with self._get_con() as c:
            user = c.cursor().execute("SELECT * FROM USERS WHERE token=?", (token, )).fetchone()
        return dict(( (keys[i], user[i]) for i in range(len(keys)) )) if user else user

    def login_user(self, name, pwd):
        user = self.get_user_by_name(name)
        if not user:
            return (1, "Пользователя с таким именем не существует")

        if not bcrypt.checkpw(pwd.encode("utf-8"), user["pwd"]):
            return (1, "Неверный пароль")

        return (0, user["token"])

    def table_exist(self):
        with self._get_con() as c:
            exist = c.cursor().execute("SELECT name FROM sqlite_master WHERE type='table' AND name='USERS';").fetchone()

        return bool(exist)

    def _get_con(self):
        return sqlite3.connect(self.path)

class GamesDB:
    def __init__(self, path):
        self.path = path

    def init(self):
        with self._get_con() as c:
            c.execute('''CREATE TABLE GAMES
                          ([token] text, 
                          [fen] text)''')
        return 0

    def new_game(self, token):
        FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
        game = self.get_game(token)
        if not game:
            with self._get_con() as c:
                c.cursor().execute("INSERT INTO GAMES(token, fen) VALUES (?, ?)", (token, FEN))
        else:
            with self._get_con() as c:
                c.cursor().execute("UPDATE GAMES SET fen=? WHERE token=?", (FEN, token))

        game = self.get_game(token)
        return game

    def update_game(self, token, fen):
        with self._get_con() as c:
            c.cursor().execute("UPDATE GAMES SET fen=? WHERE token=?", (fen, token))

    def get_game(self, token):
        keys = ("token", "fen")

        with self._get_con() as c:
            game = c.cursor().execute("SELECT * FROM GAMES WHERE token=?", (token, )).fetchone()
        return dict(( (keys[i], game[i]) for i in range(len(keys)) )) if game else game

    def table_exist(self):
        with self._get_con() as c:
            exist = c.cursor().execute("SELECT name FROM sqlite_master WHERE type='table' AND name='GAMES';").fetchone()

        return bool(exist)

    def _get_con(self):
        return sqlite3.connect(self.path)


