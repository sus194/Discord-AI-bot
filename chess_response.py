
import subprocess

def make_move(fen):
    print(fen)
    
    stockfish_process = subprocess.Popen(
        ["stockfish"],
        universal_newlines=True,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
    )

    stockfish_process.stdin.write("setoption name UCI_AnalyseMode value true\n")
    stockfish_process.stdin.flush()
    stockfish_process.stdin.write(f"position fen {fen}\n")
    stockfish_process.stdin.flush()
    stockfish_process.stdin.write("go depth 20\n")
    stockfish_process.stdin.flush()

    
    while True:
        text = stockfish_process.stdout.readline().strip()
        if text.startswith("bestmove"):
            best_move = text.split()[1]
            return best_move
