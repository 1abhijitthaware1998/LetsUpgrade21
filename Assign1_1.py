##Question 1 
##Write a python program that takes two numbers as the input and print the result of Addition, Subtraction, Multiplication, Division of the two numbers 

def my_fun(num1, num2):
            print("")
            print("add of two numbers is : ", num1+num2)
            print("sub of two numbers is : ", num1-num2)
            print("mul of two numbers is : ", num1*num2)
            print("div of two numbers is : ", num1/num2)

my_fun(num1 = int(input("Enter num1: ")), num2 = int(input("Enter num2: ")))
print("")

##Question 2 
##Write a python program that takes two numbers as the input such as X and Y and print the result of X^Y(X to the power of Y).

n = 1
num1 = int(input("Enter the num1: "))
num2 = int(input("Enter the num2: "))
print("")
for i in range(0, num2):
    n = n*num1

print(num1, "to the power of", num2, "is", n)