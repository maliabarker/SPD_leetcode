"""
The Fibonacci numbers, commonly denoted F(n) form a sequence, 
called the Fibonacci sequence, such that each number is the sum 
of the two preceding ones, starting from 0 and 1. That is,
F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).

Example 1:
    Input: n = 2
    Output: 1
    Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
Example 2:
    Input: n = 3
    Output: 2
    Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
Example 3:
    Input: n = 4
    Output: 3
    Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.

Assumptions
    I am assuming n will always be a positive integer

Psuedocode
    I would do this recursively, so I would need to state 
    a base case and recursive case
    The base case would be if n is less then or equal to one, 
    the resulting fibonacci sequence is going to equate to 1
    The recursive case would be calling the fibonnaci function again 
    with the inputs of n-1 and n-2

    if n is less than or equal to 1
        return n
    else return the sum of fibonacci function with n-1 and 
    fibonacci function with n-2
"""

# RECURSIVE METHOD
def fib(n):
    if n <= 1: # base case 
        return n
    return fib(n-1) + fib(n-2) # recursive case

# SOLUTION LINK: https://leetcode.com/problems/fibonacci-number/submissions/941764246/