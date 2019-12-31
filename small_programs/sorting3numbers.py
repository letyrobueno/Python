# Program to calculate the ascending order of three given numbers
def sort3numbers(n1, n2, n3):
    """Return the ascending order of three given numbers"""
    # 3 numbers gives 6 possible combinations since 3!=6
    if (n1 > n2):
        if (n2 > n3):
            print("The numbers in ascending order: ", n3, n2, n1)
        elif (n1 > n3):
            print("The numbers in ascending order: ", n2, n3, n1)
        else:
            print("The numbers in ascending order: ", n2, n1, n3)
    elif (n1 > n3): # here we already know that n1 <= n2
        print("The numbers in ascending order: ", n3, n1, n2)
    elif (n2 > n3):
        print("The numbers in ascending order: ", n1, n3, n2)
    else:
        print("The numbers in ascending order: ", n1, n2, n3)

# Take the value of three numbers from the user
n1 = input("Enter with a value for the first number: ")
n2 = input("Enter with a value for the second number: ")
n3 = input("Enter with a value for the third number: ")

# Convert them to int type and call the sort3numbers function
sort3numbers(int(n1), int(n2), int(n3))
