num = int(input("Enter a number = "))
factorial = 1
for i in range(1, num+1):
    factorial *= i
print(f"Factorial of {num} is {factorial}")


n = int(input("Enter a number = "))
def factorial(n):
    return 1 if(n==0 or n==1) else n*factorial(n-1)

print(f"Factorial of {n} is {factorial(n)}")
