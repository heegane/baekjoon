import sys

N = int(input())

arr = [0 for i in range(10001)]

for _ in range(N):
    data = int(sys.stdin.readline().rstrip())
    arr[data] += 1

for i in range(10001):
    if arr[i] == 0:
        continue
    else:
        for _ in range(arr[i]):
            sys.stdout.write(str(i) + "\n")
