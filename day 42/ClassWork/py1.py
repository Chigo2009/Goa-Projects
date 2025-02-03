input_string = "123456789"
result = ""

for digit in input_string:
    if int(digit) < 5:
        result += '0'
    else:
        result += '1'

print(result) 
