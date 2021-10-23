import requests as req
import chess.engine
import chess, sys

if "--linux" in sys.argv:
    engine = chess.engine.SimpleEngine.popen_uci("./stockfish/stockfish_13_linux")
else:
    engine = chess.engine.SimpleEngine.popen_uci("./stockfish/stockfish_13_win.exe")

url = "http://142.93.143.39:5000/move"

cookies = {"token":"fb690bf83a8ff9f573aae5a2aa69b46fa90c63a62a079772a64f85a4bc8afde2"}

resp = req.post(url, data = {"move" : "kek"}, cookies=cookies)
board = chess.Board()

while True:
    start = resp.text.index('position: "') + len('position: "')
    end = resp.text[start:].index('"') + start
    FEN = resp.text[start:end]

    board.set_fen(FEN)
    result = engine.play(board, chess.engine.Limit(depth=6))
    
    resp = req.post(url, data = {"move" : str(result.move)}, cookies=cookies)
    print("Move:", str(result.move))

