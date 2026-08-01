x, y, m = map(int, input().split())

max_y = m // y
ans = 0

for i in range(max_y + 1):
    tot_y = i * y
    num_x = (m - tot_y) // x
    ans = max(ans, tot_y + num_x * x)

print(ans)