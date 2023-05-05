"""
You are given the root of a binary search tree (BST) and an integer val.
Find the node in the BST that the node's value equals val and return the 
subtree rooted with that node. If such a node does not exist, return null.

Example 1:
    Input: root = [4,2,7,1,3], val = 2
    Output: [2,1,3]

Example 2:
    Input: root = [4,2,7,1,3], val = 5
    Output: []

Assumptions:
    We already have the tree/node structure given to us
    We are given a binary search tree as root
    All values (including value to find) is a positive integer
    If the val is not found we just return None

Psuedocode:
    This is just a simple binary search using the structure of a binary search tree 
    I would do this iteratively with a while loop instead of recursively (by calling 
    the function again with the next subtree to search as root)
    To do this I was instantiate a current pointer, which is what will be iterated
    Then I would enter the while loop, which will break if we reach a leaf and next is None
    I would set up three conditions;
        If node value is the value to find, return that node
        If node value is greater than the value to find, go left to move onto smaller integers
        If node value if less than the value to find, go right to move onto larger integers
    If we reach the end of the loop and nothing is found, this means the value does not exist in the tree and we return None
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root, val):
        current = root
        while current is not None:
            if current.val == val:
                return current
            elif current.val > val:
                current = current.left
            elif current.val < val:
                current = current.right
        return None
    
# SUBMISSION LINK: https://leetcode.com/problems/search-in-a-binary-search-tree/submissions/945028958/