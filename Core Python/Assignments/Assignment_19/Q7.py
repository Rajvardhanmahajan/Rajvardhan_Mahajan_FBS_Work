# 7. Use a nested list comprehension to find all of the numbers from
# 1–1000 that are divisible by any single digit.

result = list(set([
    num
    for num in range(1, 1001)
    for digit in range(1, 10)
    if num % digit == 0
]))

print(sorted(result))