def solution(text, ending):
    return text.endswith(ending)

                                     # 2

def even_or_odd(string):
    even_sum = 0
    odd_sum = 0
    
    for digit in string:
        number = int(digit)
        if number % 2 == 0:  
            even_sum += number
        else: 
            odd_sum += number
    
    if even_sum > odd_sum:
        return "Even is greater than Odd"
    elif odd_sum > even_sum:
        return "Odd is greater than Even"
    else:
        return "Even and Odd are the same"
    
                                        # 3

def even_numbers(array, number):
    even_nums = []
    
    for num in array:
        if num % 2 == 0:
            even_nums.append(num)
    
    start_index = len(even_nums) - number
    result = even_nums[start_index:]
    
    return result        


                                           # 4

def vowel_indices(word):
    vowel_positions = []
    vowels = "aeiouyAEIOUY"
    
    position = 1
    for character in word:
        if character in vowels:
            vowel_positions.append(position)
        position += 1
    
    return vowel_positions    
                  
                                      # 5

def geometric_sequence_elements(a, r, n):
    sequence = []
    
    for i in range(n):  
        term = a * (r ** i)
        sequence.append(str(term))
    
    return ', '.join(sequence)