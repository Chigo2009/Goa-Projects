def are_anagrams(string1, str2):
    string1 = string1.lower()
    str2 = str2.lower()
    return sorted(string1) == sorted(str2)


