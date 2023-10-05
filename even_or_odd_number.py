""" Console app to see if a number is odd or even """
def is_odd_or_even():
    num = input("Enter a number: ")
    try:
        num = int(num)
        if (num % 2) == 0:
            print("{0} is Even".format(num))
        else:
            print("{0} is Odd".format(num))
    except ValueError:
        print("The value entered is not a number")


if __name__ == "__main__":
    is_odd_or_even()
