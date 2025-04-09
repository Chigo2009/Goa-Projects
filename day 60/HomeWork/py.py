def double_char(s):
    result = ""
    for char in s:
        result += char * 2
    return result
                                # 2
def get_age(s):
    return int(s[0])
                                # 3
def feast(beast, dish):
  first_letter_beast = beast[0]
  last_letter_beast = beast[-1]
  first_letter_dish = dish[0]
  last_letter_dish = dish[-1]
  
  if first_letter_beast == first_letter_dish and last_letter_beast == last_letter_dish:
    return True
  else:
    return False
                                    # 4

def array_plus_array(arr1, arr2):
    return sum(arr1) + sum(arr2)
                                    # 5
def solution(number):
    if number < 0:
        return 0
    total_sum = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            total_sum += i
    return total_sum