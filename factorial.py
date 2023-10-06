def factorial(n):
    """Calculate the factorial of a number using recursion."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Get user input for the number
number = int(input("Enter a number to calculate its factorial: "))

# Check if the number is non-negative
if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    result = factorial(number)
    print(f"The factorial of {number} is: {result}")
