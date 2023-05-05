"""
Given an integer array nums where the elements are sorted in ascending order, convert it to a 
height-balanced binary search tree.

Example 1:
    Input: nums = [-10,-3,0,5,9]
    Output: [0,-3,9,-10,null,5]
    Explanation: [0,-10,5,null,-3,null,9] is also accepted
Example 2:
    Input: nums = [1,3]
    Output: [3,1]
    Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.

Assumptions:
    We are given the node structure already to use
    The arrays can have positive and negative integers
    There can be more than one way to return the balanced tree

Pseudocode:
    Binary search trees usually have a node that sort of starts in the middle of the sorted nums,
    So I would first find that middle, make that the root, then split the left and right of that into the left and right subtrees
    I would continue doing this until the list is empty
    I would probably use this recursively or with some sort of queueing
    I am more comfortable with recursive structures so I will go with that

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums):
        # start with the base case 
        if not nums:
            # the list is empty, return None
            return None
        # find mid of nums and split
        mid = (len(nums)) // 2
        # instantiate root node
        root = TreeNode(nums[mid])
        # split into left and right subtrees and make them call function again
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        # when done return root which will be BST
        return root
    
# SUBMISSION LINK: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/submissions/945036323/
        