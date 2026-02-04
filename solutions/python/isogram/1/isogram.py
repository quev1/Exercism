def is_isogram(string):
    string_normalized = string.lower().replace(" ", "").replace("-", "")
    return len(string_normalized) == len(set(string_normalized))