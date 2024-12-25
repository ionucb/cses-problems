"""
You are given a DNA sequence: a string consisting of characters A, C, G, and T. 
Your task is to find the longest repetition in the sequence. 
This is a maximum-length substring containing only one type of character.
"""

dna_sequence = input()

max_length = 1
current_length = 1

for i in range(1, len(dna_sequence)):
    if dna_sequence[i] == dna_sequence[i - 1]:
        current_length += 1
        max_length = max(max_length, current_length)
    else:
        current_length = 1

print(max_length)
