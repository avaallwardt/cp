n = int(input())
rooms = []
ans = 0

for _ in range(n):
    rooms.append(int(input()))

for i in range(n):
    # start at room i
    cows_done = 0
    total = 0
    for j in range(i, n):
        cows_done += 