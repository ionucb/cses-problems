"""
Your task is to calculate the number of trailing zeros in the factorial n!.
For example, 20!=2432902008176640000 and it has 4 trailing zeros.
"""

n = int(input())
count = 0

while n >= 5:
    n //= 5
    count += n

print(count)