  #1
first_list = "luka.nika.saba.nana"
splited_first_list = first_list.replace(".", " ")
print(splited_first_list)
                             #2
second_list = "cat dog parrot monkey"
joined_second_list = second_list.replace(" ", "⭐")
print(joined_second_list)
                             #3
third_list = "gun, ak47, m16, awp"
replaced_third_list = third_list.split(", ")
print(replaced_third_list)
                              #4
num1 = float(input("Enter num1🔢: "))
num2 = float(input("Enter num2🔢: "))
operator1 = input("Select an operator (+ - * /): ")

if operator1 == "+":
    result = num1+num2
    print(round(result, 4))
elif operator1 == "-":
    result = num1-num2
    print(round(result, 4))
elif operator1 == "*":
    result = num1*num2
    print(round(result, 4))
elif operator1 == "/":
    result = num1/num2
    print(round(result, 4))
else:
    print(f"{operator1} is an invalid operator❌")

