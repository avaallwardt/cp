n = int(input())
ramps = [()] * n
ans = [0, 1000]

for i in range(n):
    z = input().split()
    ramp = z[0]
    x, y = map(int, z[1:])
    if ramp == 'on':
        ans[0] += x
        ans[1] += y
    elif ramp == 'off':
        ans[0] -= y
        ans[1] -= x
    else:
        ans[0] = max(ans[0], x)
        ans[1] = min(ans[1], y)
    ramps[i] = (ramp, x, y)

end = ans
start = list(ans)

for i in range(n):
    ramp, x, y = ramps[i]
    if ramp == 'on':
        start[0] -= x
        start[1] -= y
    elif ramp == 'off':
        start[0] += y
        start[1] += x
    # else:
    #     ans[0] = max(ans[0], x)
    #     ans[1] = min(ans[1], y)
    # if it's none, we don't need to do anything bc we've already narrowed the interval as small as possible 

start1, start2 = start
end1, end2 = end
print(start1, start2)
print(end1, end2)

