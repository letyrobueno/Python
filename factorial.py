# Program to calculate the factorial of a number n, i.e., n!=n * (n-1) * ... * 2 * 1.
def factorial(n):
    """Return the factorial of a number n"""
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

# Take the value of n from the user
n = input("Enter with a value for n: ")

# Convert it to int type and call the factorial function
fact = factorial(int(n))

# Print fact
print("The factorial of ", n, " is ", fact)