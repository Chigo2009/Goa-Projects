def convert_vowels_to_numbers(text):
    vowels = 'aeiouAEIOU'
    result = ''
    
    for char in text:
        if char in vowels:
            result += '1'
        else:
            result += '0'
    
    return result

#2

#3 


#4 
def check_string_ending(full_text, ending):
    return full_text.endswith(ending)

#5 
def find_duplicate_element(array):
    for item in array:
        if array.count(item) == 2:
            return item
    
    return None