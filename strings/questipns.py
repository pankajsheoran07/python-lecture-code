import numpy as np
#1. Longest Substrining Without Repeating Characters

# Given a string, find the length of the longest substring without together repeating characters. 
# Example:
# "abcabcbb" → 3
'''n1 = "ldkx vjiennncnp qwertiii"
n2 = ''
list1 = []
max_len  = 0
for i in n1:
    if i in n2:
        n2 = n2[n1.index(i)+1:]
    n2+=i
    if len(n2) > max_len:
        max_len = len(n2)
        list1 = [n2]
    elif len(n2) == max_len:
        list1.append(n2)
print(list1)'''

# Write a Python program that takes a string as input and finds all substrings of length ≥ 2 that do not contain any repeating characters.
# The program should print the list of such substrings in the order they appear in the original string.
    
'''# n1 = "ldkx vjieinnnncnp qwertiii"
# substrings = []

# for start in range(len(n1)):
#     seen = set()
#     current = ""
#     for end in range(start, len(n1)):
#         ch = n1[end]
#         if ch in seen:  # stop if repeat found
#             break
#         seen.add(ch)
#         current += ch
#         if len(current) >= 2:
#             substrings.append(current)  

# print(substrings)
# print(f"Total substrings found: {len(substrings)}")'''

# '''2. Group Anagrams

# Given an array of strings, group the anagrams together.
# Example:
# ["eat","tea","tan","ate","nat","bat"] → [["eat","tea","ate"], ["tan","nat"], ["bat"]]
# '''
n1 = input('enter your words with space in it: ')
l1 = n1.split()
print(l1)