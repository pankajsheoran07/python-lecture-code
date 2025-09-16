#syntax of split
'''string.split(sep=none, maxsplit = -1)


sep (Separator) : This is the delimiter string where the split occurs.

If sep is not provided or is None (the default), the method splits the string on any sequence of whitespace (spaces, tabs \t, newlines \n) and discards empty strings from the result.

If sep is specified (e.g., ','), it performs the split exactly at that delimiter. Consecutive delimiters will result in empty strings.

maxsplit: This is an integer that specifies the maximum number of splits to perform.

The default value is -1, which means there is no limit to the number of splits.

If maxsplit is set to n, the string will be split at most n times, resulting in a list with a maximum of n + 1 elements.'''