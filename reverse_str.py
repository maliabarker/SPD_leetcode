"""
Write a function that reverses a string. The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:
    Input: s = ["h","e","l","l","o"]
    Output: ["o","l","l","e","h"]
Example 2:
    Input: s = ["H","a","n","n","a","h"]
    Output: ["h","a","n","n","a","H"]

Assumptions:
    We are given the string as an array already
    We cannot create a new array or copy the array, we need to modify in place
    We return the array, not the string itself

Psuedocode:
    Because we want to modify everything in place, we want to try to swap the items in the list
    We can do this by instantiating a left and right pointer that points to the beginning of the list and the end of the list
    Then we can enter a while loop that will break if left and right overlap / meet (left > right)
        In this loop we swap the left and right letters
        Then we move both pointers in by one by incrementing left and decrementing right
        This will continue to swap the characters until there are no more left to swap
"""

class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

# SUBMISSION LINK: https://leetcode.com/problems/reverse-string/submissions/945043579/