"""
Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower 
and upper cases, more than once.

Example 1:
    Input: s = "hello"
    Output: "holle"
Example 2:
    Input: s = "leetcode"
    Output: "leotcede"

Assumptions:
    The vowels can be upper or lower case
    All characters in the string are ASCII characters
    We return the string

Psuedocode:
    To do this, we would need to first convert the string to an array so it is easier to iterate
    Then, I would initialize an array of vowels so I can check the characters against it
    Then, I would set up a left and right pointer for the array
    While the left pointer is less than the right pointer
        check if both characters at the pointers are vowels
            If they are, swap them and increment left, decrement right
        if not check if left is not a vowel
            if not a vowel increment
        check if right is not a vowel
            if not a vowel decrement
    Once that is done, convert the list back to a string and return it
"""

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']
        s_arr = list(s)
        left = 0
        right = len(s) - 1
        while left < right:
            if s_arr[left] in vowels and s_arr[right] in vowels:
                s_arr[left], s_arr[right] = s_arr[right], s_arr[left]
                left += 1
                right -= 1
            elif s_arr[left] not in vowels:
                left += 1
            elif s_arr[right] not in vowels:
                right -= 1
        return ''.join(s_arr)
    
# SOLUTION LINK: https://leetcode.com/problems/reverse-vowels-of-a-string/submissions/945050102/

