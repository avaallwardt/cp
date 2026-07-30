'''CORRECT: ATTEMPT 1'''


'''
logic
- j will move right 1, then back 1
- then j will move left 2, then back 2
- if j reaches b (or passes), then stop, but only add the dist j travelled to b
- print total distance travelled
- so basically we need to find the point where j will pass bessie
'''

j, b = map(int, input().split())
travel = 1
total = 0
i = 0 # move right first
while(True):
    if j == b:
        break
    elif ((i % 2 == 0) and (j < b) and (j + travel >= b)) or ((i % 2 == 1) and (j > b) and (j - travel <= b)):
        total += abs(j-b)
        break
    else:
        total += travel * 2
        travel *= 2
        i += 1

print(total)