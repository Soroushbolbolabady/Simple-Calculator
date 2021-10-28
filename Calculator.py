

# inputs
num1 = int(input("Please enter your first number : "))
num2 = int(input("Plaease enter your second number :"))
operation = int(input("1.sum , 2.sub , 3.multi , 4.div : "))



# operator
def sum(num1 , num2):
    return num1 + num2

def multi(num1 , num2):
    return num1 * num2

def div(num1 , num2):
    return num1 / num2

def sub(num1 , num2):
    return num1 - num2
    

if operation == 1 :
    print(sum(num1 , num2))
elif operation == 2 :
    print(sub(num1 , num2))
elif operation == 3 :
    print(multi(num1 , num2))
elif operation == 4 :
    print(div(num1 , num2))
else:
    print("Enter Number 1-4")