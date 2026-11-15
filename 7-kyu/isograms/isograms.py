def is_isogram(string):
    string_lower = string.lower()
    for char in string_lower:
        if string_lower.count(char) > 1:
            return False
​
    return True
        