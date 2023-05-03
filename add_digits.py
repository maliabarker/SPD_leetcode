"""
Given an integer num, repeatedly add all its digits until the result 
has only one digit, and return it.

Example 1:
    Input: num = 38
    Output: 2
    Explanation: The process is
    38 --> 3 + 8 --> 11
    11 --> 1 + 1 --> 2 
    Since 2 has only one digit, return it.

Example 2:
    Input: num = 0
    Output: 0

Assumptions:
    We assume that num is a positive integer
    We assume we can use python built in functions such as sum()

Psuedocode
    For this, I would split the number into separate integers by converting to a string then splitting then converting each back into an integer
    Then, I would enter a loop while the length of the numbers list is greater than 1
        For each iteration, I would sum the numbers, then split this sum using the same method above
    Return the first index of the numbers list   
"""

class Solution:
    def addDigits(self, num: int) -> int:
        nums = [int(i) for i in str(num)]
        while len(nums) > 1:
            new_num = sum(nums)
            nums = [int(i) for i in str(new_num)]
            print(nums)
        return nums[0]
    
# SOLUTION LINK: https://leetcode.com/problems/add-digits/submissions/944051255/