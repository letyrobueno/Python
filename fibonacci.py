# Recursive program to calculate Fibonacci numbers, i.e., F(0) = 0; F(1) = 1; F(n) = F(n-1) + F(n-2), for n>1
# Not the best resolution: it calculates the Fibonacci of some numbers multiple times.
# Time complexity: given by the recurrence T(n) = T(n-1) + T(n-2) + 4, which results in O(2^n) (exponential time)
def fibonacci_rec(n):
    """Return the Fibonacci number of n"""
    if (n < 2):
        return n
    else:
        return(fibonacci_rec(n-1) + fibonacci_rec(n-2))

# Iterative program to calculate Fibonacci numbers, i.e., F(0) = 0; F(1) = 1; F(n) = F(n-1) + F(n-2), for n>1
# Time complexity: linear, since the loop runs from 1 to n, so it runs in O(n) time
def fibonacci_iter(n):
    """Return the Fibonacci number of n"""
    j = 0
    i = 1

    for k in range(1,n):
        t = i + j
        i = j
        j = t
    return j


# Take the value of n from the user
n = input("Enter with a value for n: ")

# Convert it to int type and call the factorial function
fib = fibonacci_iter(int(n))
# fib = fibonacci_rec(int(n))

# Print fact
print("The Fibonacci of ", n, " is ", fib)