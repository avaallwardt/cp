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


