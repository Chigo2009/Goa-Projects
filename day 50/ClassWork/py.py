def is_isogram(word):
    return len([char for char in set(word.lower())]) == len(word)

print(is_isogram("Dermatoglyphics")) 
print(is_isogram("aba"))  
print(is_isogram("moOse"))  
print(is_isogram(""))  
