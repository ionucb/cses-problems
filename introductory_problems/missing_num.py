"""
You are given all numbers between 1,2,...,n except one. 
Your task is to find the missing number.
"""

n=int(input())
numere = input().split()
sum = 0
n_sum = n*(n+1)/2

for numar in numere:
    sum += int(numar)

print(int(n_sum-sum))