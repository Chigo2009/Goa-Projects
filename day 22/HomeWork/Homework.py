def custom_split(string, delimiter):
    result = []
    word = ""
    for char in string:
        if char == delimiter:
            if word:
                result.append(word)
                word = ""
        else:
            word += char
    if word:
        result.append(word)
    return result


input_string = "Hello world, how are you?"
delimiter = " "
split_result = custom_split(input_string, delimiter)
print(split_result)

def custom_join(list_of_strings, delimiter):
    result = ""
    for i, word in enumerate(list_of_strings):
        if i != 0:
            result += delimiter
        result += word
    return result

# გამოყენება
words = ["Hello", "world", "how", "are", "you?"]
delimiter = " "
joined_string = custom_join(words, delimiter)
print(joined_string)

def custom_replace(string, old, new):
    result = ""
    i = 0
    while i < len(string):
        if string[i:i+len(old)] == old:
            result += new
            i += len(old)
        else:
            result += string[i]
            i += 1
    return result

# გამოყენება
input_string = "Hello world, world is great."
old_substring = "world"
new_substring = "earth"
replaced_string = custom_replace(input_string, old_substring, new_substring)
print(replaced_string)

def mini_calculator():
    print("Select operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    choice = input("Enter choice (1/2/3/4): ")
    
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    if choice == '1':
        print(f"{num1} + {num2} = {num1 + num2}")
    elif choice == '2':
        print(f"{num1} - {num2} = {num1 - num2}")
    elif choice == '3':
        print(f"{num1} * {num2} = {num1 * num2}")
    elif choice == '4':
        if num2 != 0:
            print(f"{num1} / {num2} = {num1 / num2}")
        else:
            print("Cannot divide by zero")
    else:
        print("Invalid Input")

       