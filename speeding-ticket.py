'''CORRECT: ATTEMPT 1'''

# n = num of speed limit segments, m = num of bessie segments
n, m = map(int, input().split())
limits = []
bessie = []
ans = 0 # store max speed over the limit

# create list of length 100 for speed limit on each point of interval
for _ in range(n):
    interval, limit = map(int, input().split())
    limits.extend([limit] * interval)

# create list of length 100 for bessie's speed on each point of interval
for _ in range(m):
    interval, speed = map(int, input().split())
    bessie.extend([speed] * interval)

# find where bessie's speed > speed limit for each of the 100 points
for i in range(len(limits)):
    if bessie[i] > limits[i] and bessie[i] - limits[i] > ans:
        ans = bessie[i] - limits[i]

print(ans)

