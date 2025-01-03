"""
You are given an array of n integers. You want to modify the array so that it is increasing, i.e., 
every element is at least as large as the previous element.
On each move, you may increase the value of any element by one. 
What is the minimum number of moves required?
"""

n = int(input())
count=0
numere = list(map(int,input().strip().split()))

for i in range(1, n):
    if numere[i] < numere[i - 1]:
        diff = numere[i - 1] - numere[i]
        numere[i] += diff
        count += diff  

print(count)