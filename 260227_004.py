import sys

t = int(sys.stdin.readline())
words = []

for _ in range(t):
    words.append(sys.stdin.readline().rstrip())

for i in range(t):
    print(f"{words[i][0]}{words[i][-1]}")
