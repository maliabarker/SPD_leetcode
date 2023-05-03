"""
Given an integer num, return a string representing its hexadecimal representation. 
For negative integers, two's complement method is used.
All the letters in the answer string should be lowercase characters, and there should 
not be any leading zeros in the answer except for the zero itself.
Note: You are not allowed to use any built-in library method to directly solve this problem.

Example 1:
    Input: num = 26
    Output: "1a"
Example 2:
    Input: num = -1
    Output: "ffffffff"

Assumptions:
    We cannot use any built in library/tools for this
    We use lowercase letter for this

Psuedocode
    For this, we want to have some sort of reference for the numbers to letters conversion, 
    so I will create a dictionary that has letters numbers 10 - 15 corresponding to letters a - f 
    We want to start with our base case, which is if the num==0, we return 0
    We want to convert any negative numbers into numbers we can convert to hexadecimal (positive int)
    To do this, we use two's complement, which will convert the number to binary, then take to inverse, and convert this inverse binary back to a number
    To implement two's complement, we can use the leftshift of 32 bits (1 << 32) and add the number to this. This will make it positive
    Then we implement the conversion
    To do this we initialize an empty string for the hexadecimal string and initialize a current number to keep track of our calculations
    While the current number is greater than 0
        we find the remainder using modulus operator of dividing by 16 
        then we find the hexadecimal representation of the remainder and add it to the front of the string
        we move on by making the current number the result of dividing by 16 (using nearest integer //)
        we continue this until the current number reaches 0
    Return the hexadecimal string
"""

class Solution:
    def toHex(self, num: int) -> str:
        nums_to_letters = {
            10: 'a',
            11: 'b',
            12: 'c',
            13: 'd',
            14: 'e',
            15: 'f'
        }
        if num == 0:
            return '0'
        if num < 0:
            num = (1 << 32) + num
        hexadecimal_str = ''
        current_num = num
        while current_num > 0:
            remainder = current_num % 16
            current_num = current_num // 16
            if remainder >= 10:
                hexadecimal_str = str(nums_to_letters[remainder]) + hexadecimal_str
            else:
                hexadecimal_str = str(remainder) + hexadecimal_str
        return hexadecimal_str
    
# SOLUTION LINK: https://leetcode.com/problems/convert-a-number-to-hexadecimal/submissions/944040060/