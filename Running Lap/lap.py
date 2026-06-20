# Pseudocode — sum of first n numbers:
# INPUT n
# total = 0
# FOR each number FROM 1 TO n:
#     total = total + number
# OUTPUT total

# The same logic in Python:
n = 4
total = 0
for number in range(1, n + 1):
    total += number
print(total)   # Output: 10

# Time complexity in the three solutions (n = 4):

# Formula way — 1 step, always:
total = n * (n + 1) // 2       # 1 operation, no loop
# Steps = 1

# Loop way — n steps:
for round_num in range(1, n + 1):   # loop runs n times
    total += round_num
# Steps = 4  (for n = 4)

# Nested loop way — roughly n*n steps:
for round_num in range(1, n + 1):   # outer loop: n times
    for point in range(1, round_num + 1):   # inner loop: up to n times
        total += 1
# Steps = 10  (for n = 4)


# Space complexity — counting extra variables:

# Formula way  : 1 extra variable (total)
total = n * (n + 1) // 2

# Loop way     : 2 extra variables (total, round_num)
total = 0
for round_num in range(1, n + 1):
    total += round_num

# Nested loop  : 3 extra variables (total, round_num, point)
total = 0
for round_num in range(1, n + 1):
    for point in range(1, round_num + 1):
        total += 1

# All three use the same fixed number of variables — constant space