'''
    Factorial Number using Recursive Function

'''
# Calculatin Factorial of Given number by user

def factorial1(n):
    if (n == 1):
        return 1
    else:
        return n * factorial1(n - 1)

num1 = int(input("Enter Factorial Number : "))
k = factorial1(num1)
print(f"Factorila of {num1} is {k}")

print("Follow : https://github.com/javid14395")