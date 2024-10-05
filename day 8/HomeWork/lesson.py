age = int(input("Enter your age: "))
print("Your age is less than 19: " , age < 19 ,"  Your age is more than 13: " , age > 13)
testscore = int(input("Enter your test score: "))
is_A = print("Your grade is A: " , testscore >= 9)
is_B = print("Your grade is B: " , testscore   >= 8 and age < 9)
is_C = print("Your grade is C: " , testscore >= 7 and age < 8)
is_D = print("Your grade is D: " , testscore >= 6 and age < 7)
is_F = print("Your grade is F: ", testscore < 6)
variable1 = True
variable2 = False
print(variable1 and variable2)
print(variable1 or variable2)
num1=(5)
num2=(10)
print("Answer is: ",num1 == num2)
print("Answer is: ",num1 < num2)
print("Answer is: ",num1 > num2)
print("Answer is: ",num1 <= num2)
print("Answer is: ",num1 >= num2)
print("Answer is: ",num1 != num2)
a = int(input("Enter your number: "))
b = int(input("Enter your number: "))
c = int(input("Enter your number: "))
is_a_greatest = ("Greatest number: ",c < a > b )
print(is_a_greatest)
is_b_middle = ("Middle number: ",c < b < a )
print(is_b_middle)
is_c_least= ("Least number: ",b > c < a)
print(is_c_least)



score = 100
if 50 <= score :
    is_pass = True
    print( is_pass  )
elif 75 <= score and score < 90:
    is_high_pass = True
    print(is_high_pass)  
elif 100  == score:
    is_perfect= True
    print(is_perfect)
elif 50 < score:
    is_failed = True
    print(is_failed)

