'''correct: attempt 1'''

n, k = map(int, input().split())
a = [0] * n
for i in range(n):
    a[i] = int(input())

# or a = [int(input()) for _ in range(n)] # since we want to take in n inputs, each on a new line, so call input() n separate times

a.sort()

left = 0
ans = 0

for right in range(n):
    while(a[right] - a[left] > k):
        left += 1
    ans = max(ans, right - left + 1)

print(ans)
