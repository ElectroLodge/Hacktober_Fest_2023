# Python3 code to demonstrate
# checking a number is palindrome
# using math.log() + recursion + list comprehension
import math
   
# the recursive function to reverse
def rev(num):
    return int(num != 0) and ((num % 10) * \
             (10**int(math.log(num, 10))) + \
                          rev(num // 10))
