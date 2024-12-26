"""
Your task is to calculate the number of bit strings of length n.
For example, if n=3, the correct answer is 8, 
because the possible bit strings are 000, 001, 010, 011, 100, 101, 110, and 111.
Print the result modulo 10^9+7.
"""

MOD = 10**9 + 7
n = int(input())
result = pow(2, n, MOD)
print(result)
