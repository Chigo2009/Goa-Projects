def to_alternating_case(string):
    result = ''
    for char in string:
        if char.islower():
            result += char.upper()
        elif char.isupper():
            result += char.lower()
        else:
            result += char  
    return result

                                        # 3

def correct(s):
    result = ''
    for char in s:
        if char == '5':
            result += 'S'
        elif char == '0':
            result += 'O'
        elif char == '1':
            result += 'I'
        else:
            result += char
    return result

                                         # 4

def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]
                                          # 5

def bonus_time(salary, bonus):
    if bonus:
        return "$" + str(salary * 10)
    else:
        return "$" + str(salary)
                                          # 6

def final_grade(exam, projects):
    if exam > 90 or projects > 10:
        return 100
    elif exam > 75 and projects >= 5:
        return 90
    elif exam > 50 and projects >= 2:
        return 75
    else:
        return 0
                                           # 7

def min_max(lst):
    return [min(lst), max(lst)]