'''CORRECT: both method 1 (num items in list at any given time) and method 2 (prefix sums)'''

'''Method 1:
- separate lists for start times, end times, and buckets
- create a new list holding number buckets needed at any given time
'''

num_cows = int(input())

# create lists to store the start times, end times, and buckets needed for each of the num_cows cows
start_times = [0] * num_cows
end_times = [0] * num_cows
buckets = [0] * num_cows

# fill those lists
for i in range(num_cows):
    start_times[i], end_times[i], buckets[i] = map(int, input().split())

# create slots for buckets needed at all the possible times from 0 to max end_times (so now index of given time is the time-1, i.e. time 1 is at index 0)
slots = [0] * max(end_times)

# for each of the num_cows cows, add the number of buckets needed during its interval
for i in range(num_cows):
    for j in range(start_times[i], end_times[i] + 1, 1):
        slots[j-1] += buckets[i]

# find max number of buckets needed at any given time
ans = max(slots)

print(ans)


''' Method 2
- prefix sum
- build slots list as take in input about the n cows
'''

n = int(input())
slots = [0] * 1005 # make it > 1005 so we 
for _ in range(n):
    s, t, b = map(int, input().split())
    slots[s] += b
    slots[t+1] -= b # now the prefix sum from s to t will include b then b will be subtracted after t
    # takes less time than putting p in all slots from s to t because only place b in slots s and t-1 (neg b) (2 total slots) rather than all slots s to t (t-s+1 total slots)

# calculate max prefix sum in slots list
total = 0
ans = 0
for i in range(1005):
    total += slots[i] # total represents the current prefix sum from index 0 to i
    ans = max(ans, total)

print(ans)

