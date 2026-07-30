'''CORRECT: METHOD 2'''


'''METHOD 1'''
# apply shuffle to placeholder list

# num_cows = map(int, input().split())
# shuffle = list(map(int, input().split()))
# order = list(map(int, input().split()))
# start = [i for i in range(num_cows)]
# for _ in range(3):
#     # apply shuffle to start 3 times
#     new = [0] * num_cows
#     for i in range(len(shuffle)):
#         new[shuffle[i] - 1] = start[i]
#     start = new
# for i in range(len(start)):


'''METHOD 2'''
# find reverse shuffle then apply it 3 times
num_cows = int(input())
forward = list(map(int, input().split()))
end = list(map(int, input().split()))
backward = [0] * num_cows

# create backward shuffle (w/ 0 indexing)
for i in range(num_cows):
    backward[forward[i] - 1] = i

# apply backward shuffle 3 times
for _ in range(3):
    new = [0] * num_cows
    for i in range(num_cows):
        new[backward[i]] = end[i]
    end = new

for cow in end:
    print(cow)

