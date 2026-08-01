n = 0 # number of points
x = [] # array of x-coordinates
y = [] # array of corresponding y-coordinates

ans = 0 # max squared euclidean distance btwn 2 points

for i in range(n):
    for j in range(i, n):
        # calc distance from point i to point j
        dist = (x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2
        # check if dist is greater than current max dist
        ans = max(ans, dist)

print(ans)