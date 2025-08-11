#  Longest Substring Without Repeating Characters
# Write a function that takes a string and returns the length of the longest substring without repeating characters.
# Example: "abcabcbb" → 3 ("abc")

def length_of_longest_substring(s):
    char_map = {}
    left = 0
    max_length = 0

    for right in range(len(s)):
        if s[right] in char_map:
            left = max(left, char_map[s[right]] + 1)
        char_map[s[right]] = right
        max_length = max(max_length, right - left + 1)

    return max_length



user_input = input("Enter a string: ")
print("Length of longest substring without repeating characters:", length_of_longest_substring(user_input))