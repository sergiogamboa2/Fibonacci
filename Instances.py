import os
print('Hello, ' + os.getlogin() + '! How are you?')

import sys

def function1():
    nterms = int(input("Please enter the how many numbersto calculate: "))

    # first two terms
    n1, n2 = 0, 1
    count = 0

    # check if the number of terms is valid
    if nterms <= 0:
        print("Please enter a positive integer")
    elif nterms == 1:
        print("Fibonacci sequence upto", nterms, ":")
        print(n1)
    else:
        print("Fibonacci sequence:")
        while count < nterms:
            print(n1)
            nth = n1 + n2
            # update values
            n1 = n2
            n2 = nth
            count += 1

def function2():
    def Fibonacci(n):
        if n < 0:
            print("Incorrect input")

        elif n == 1:
            return 0

        elif n == 2:
            return 1
        else:
            return Fibonacci(n - 1) + Fibonacci(n - 2)
    inputFibo = int(input("Type a number to calculate its Fibonacci order: "))
    print(Fibonacci(inputFibo))

def main():
    jobs = {"1": function1, "2": function2}
    choosenOption = input("Please enter #1 for a series of numbers or #2 for a single number to be calculated: ")
    jobs[choosenOption]()

if __name__ == "__main__":
    main()