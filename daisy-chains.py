'''correct: attempt 1 1'''

# attempt 1
# runtime: O(n^2) where n^2 is number of contiguous subarrays, n is number of petals
# could do O(n^3) approach where iterate through each contiguous subarray (worst-case O(n)) looking for avg value if dont store value counts for each petal value in an array counts that has O(1) lookup by index (where index represents a given petal count)
n = int(input())
petals = list(map(int, input().split()))

ans = 0

for left in range(n):
    
    running_sum = 0
    counts = [0] * 1005
    
    for right in range(left, n):
        
        running_sum += petals[right]
        num_petals = right - left + 1
        counts[petals[right]] += 1
        
        if running_sum % num_petals == 0:
            avg = running_sum // num_petals
            if counts[avg] > 0:
                ans += 1

print(ans)

