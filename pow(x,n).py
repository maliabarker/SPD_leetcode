"""
Implement pow(x, n), which calculates x raised to the power n (i.e., x^n).
Example 1:
Input: x = 2.00000, n = 10
Output: 1024.00000

Example 2:
Input: x = 2.10000, n = 3
Output: 9.26100

Assumptions
    n will always be a whole integer
    n can be positive or negative
    x can be a float or integer
    the returned number can be a float or integer
    We cannot use += or -=

Psuedocode
    I can do this recursively with the following base and recursion cases
    base case
        if n is 0, return 1 because anything to the power of 0 is one
    recursive case
        if n is negative
            return reciprocal with 1 / another function call to myPow except pass 
            in the exponent as positive
        else
            calculate the power by multiplying x by another function call and decrement 
            n each time (until it hits 0)
            return the resulting multiplied number
    
    This will easily hit a max recursion depth with high exponents and is not great for 
    memory or time allocation, so let's look at doing this with a while loop instead.

    If n == 0 return 1 because anything to the power of 0 is 1
    Else if n is negative 
        make x equal its reciprocal (1 / x)
        make n positive
    Instantiate a result that will be multiplied
    While n is greater than 0
        To get around the issue that we can't use -= to decrement n, let's use floor divison (//)
        Floor division will halve the value of n, which will decrement it with better time 
        complexity as well
        First, check if n is odd or even by using modulus. 
        If it is odd (result will equal 1)
            Mutliply the running result by x
        Else
            Multiply x by itself, which will keep track of the extra power in the next running 
            result tracker
        Halve n using n //= 2
    return the result
"""

# WITH RECURSION (this hits max recursion depth with a really large exponent)
def myPow(x, n):
    # get reciprocal of base (1/base)
    # raise base to absolute value of exponent
    # return reciprocal (1/base_to_pow)
    # example: 2.5^-3 = 1 / (2.5^3) = 1 / (2.5 x 2.5 x 2.5) = 0.064
    if n == 0:
        return 1
    if n < 0:
    # create reciprocal (1/base^exponent)
    # make the exponent positive to do the actual power implementation
        result_neg_pow = 1 / (myPow(x, -n))
        return result_neg_pow
    # actual power implementation
    result_pos_pow = x * myPow(x, n - 1)
    return result_pos_pow

# WITHOUT RECURSION
def myPow(x, n):
    if n == 0:
        return 1
    elif n < 0:
        x = 1 / x
        n = -n
    result = 1
    while n > 0:
        if n % 2 == 1:
            result *= x
        x *= x
        n //= 2
    return result

# SOLUTION LINK: https://leetcode.com/problems/powx-n/submissions/941761475/