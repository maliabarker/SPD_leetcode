"""
Given an integer array nums, move all 0's to the end of it while maintaining 
the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.

Example 1:
    Input: nums = [0,1,0,3,12]
    Output: [1,3,12,0,0]

Example 2:
    Input: nums = [0]
    Output: [0]

Assumptions:
    We cannot create a new array or a copy of the array, we have to change everything in place.
    All elements in array are integers

Psuedocode
    We can change things in place by simply changing the value of the elements in the list
    We want to do this by keeping two pointers, the current number and the 'next' number
    These numbers will point to the index in the array
    We can initialize the current number as the first index (0)
    Then, we can loop over every number in the array and keep the loop pointer as 'next'
    For next_pointer in range(len(numbers_array))
        If the current pointer is zero and the next is not zero
            we swap them and then increment our current pointer to the next value
        If the current pointer is not zero
            we simply implement our current pointer to the next value
        And if neither of these conditionals are met, it means we'll wait until the next pointer is not zero so we can swap
"""

class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        current = 0
        for next in range(len(nums)):
            if nums[current] == 0 and nums[next] != 0:
                # swap & increment
                nums[current], nums[next] = nums[next], nums[current]
                current += 1
            elif nums[current] != 0:
                current += 1

# LINK SOLUTION: https://leetcode.com/problems/move-zeroes/submissions/944048698/