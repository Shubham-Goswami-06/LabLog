import sys

def clear_last_lines(n):
    for _ in range(n):
        sys.stdout.write("\033[F")  # move cursor to start of previous line
        sys.stdout.write("\033[K")  # erase that line
    sys.stdout.flush()