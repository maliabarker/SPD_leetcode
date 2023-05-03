"""
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns three possible results:

-1: Your guess is higher than the number I picked (i.e. num > pick).
1: Your guess is lower than the number I picked (i.e. num < pick).
0: your guess is equal to the number I picked (i.e. num == pick).
Return the number that I picked.

Example 1:
    Input: n = 10, pick = 6
    Output: 6

Example 2:
    Input: n = 1, pick = 1
    Output: 1

Example 3:
    Input: n = 2, pick = 1
    Output: 1

Assumptions:
    The number picked has to be between 1 and n (has to exist in the search and positive)
    The guess() function only returns 0, 1, or -1
    All associated numbers are integers (no decimals)

Psuedocode:
    The brute force solution would be to iterate through each number between 1 and n and guess each time. This would be O(n)
    We could make this better by doing a binary search, which would give us O(log(n)) time complexity. Let's implement that
    We would start by initializing our low, high, and mid values which would be 0, n, and 0+n//2
    Then we would make our guess with the middle value.
    We would start a while loop with the following conditions:
        our guess can't be equal to zero (this means it would be the correct guess)
        and our low can't be greater than our high (this means we searched the whole list)
    In the while loop, we would check if the guess is higher than the actual number (-1) or lower than the actual number (1)
    If it is lower (guess=1)
        We make the new low point the value of mid and increase it by one 
        Then we create a new mid point (new low + high // 2)
        Then we guess again
    Else if it is higher (guess=1)
        We make the new high point the value of mid and decrease it by one
        Then we create a new mid point (low + new high // 2)
        Then we guess again
    Once the loop is broken or x==0, we return our guess which is the value of mid
"""

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:
def guess(num, guess):
    if num == guess:
        return 0
    elif num > guess:
        return -1
    elif num < guess:
        return 1
    
class Solution:
    def guessNumber(self, n: int) -> int:
        mid = n//2
        low = 0
        high = n
        x = guess(mid)
        print(low, high, mid)
        while x!=0 and high > low:
            print(x)
            # not found, continue search
            if(x==1):
                # guess is lower than num, need a higher number
                low = mid+1
                mid = (low + high) // 2
                print(low, high, mid)
                x = guess(mid)
            elif (x==-1):
                # guess is higher than num, need a lower number
                high = mid-1
                mid = (low + high) // 2
                print(low, high, mid)
                x = guess(mid)
        return mid
    
# SOLUTION LINK: https://leetcode.com/problems/guess-number-higher-or-lower/submissions/944029094/