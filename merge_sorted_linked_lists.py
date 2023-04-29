"""
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list. The list should be made by splicing 
together the nodes of the first two lists.
Return the head of the merged linked list.

Example 1:
    Input: list1 = [1,2,4], list2 = [1,3,4]
    Output: [1,1,2,3,4,4]
Example 2:
    Input: list1 = [], list2 = []
    Output: []
Example 3: 
    Input: list1 = [], list2 = [0]
    Output: [0]

Assumptions
    We assume that we are modifying the list(s) and not creating a new list
    We assume that we are returning the modified list

Psuedocode
    I could do this either with a while loop and iterate over each node until one 
    of the lists is empty (then add the rest of the remaining nodes in the non-empty list)
    OR I could do this recursively and call the merge function on the remaining nodes

    To do this recursively I would first check the base case
        If list1 is empty, return list2
        Else if list2 if empty, return list1
    And then I would do the recursive case
        First I would compare the head nodes of each list
        If list1.val is less than list2.val
            Keep the head node of list1 as the first node and make the next node another 
	        call to the merge function, passing in the new head node of list1 as list1.next
            and keeping list2 the same
            return list1, which will have all sorted nodes following
        Else
            Keep the head node of list2 as the first node and make the next node another 
	        call to the merge function, passing in the new head node of list2 as list2.next
            and keeping list1 the same
            return list2, which will have all sorted nodes following

"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
	# base case if one of the lists is empty
	if not list1:
		return list2
	elif not list2:
		return list1

	# recursive case
	# compare the head nodes of both lists
	elif list1.val <= list2.val:
		# if list1 is less than list2, use list1 val as first item and continue merging lists after this node
		list1.next = mergeTwoLists(list1.next, list2)
		return list1
	else:
		# if list2 is less then list 1, use list2 val as first item and continue merging lists after this node
		list2.next = mergeTwoLists(list1, list2.next)
		return list2
	
# SOLUTION LINK: https://leetcode.com/problems/merge-two-sorted-lists/submissions/941753422/