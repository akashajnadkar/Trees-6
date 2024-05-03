'''
Time Complexity - O(n). We traverse through the entire tree
Space Complexity - O(n). We are using a queue with maximum length number of nodes
Works on Leetcode
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return None
        widthMap = {}
        #create a queue for nodes and width
        queue = deque()
        colQueue = deque()
        queue.append(root)
        colQueue.append(0)
        minW, maxW = 1e9, -1e9
        while queue:
            curr = queue.popleft()
            currW = colQueue.popleft()
            #add the node to its respective bucket according to width
            if currW not in widthMap:
                widthMap[currW] = []
            widthMap[currW].append(curr.val)
            #keep min max so that we have bounds for buckets
            minW = int(min(minW,currW))
            maxW = int(max(maxW,currW))
            if curr.left!=None:
                #width reduces by 1 when we add left child
                queue.append(curr.left)
                colQueue.append(currW-1)
            if curr.right != None:
                #width increases by 1 when we add right child
                queue.append(curr.right)
                colQueue.append(currW+1)
        result = []
        #iterate through all the children in the map
        for i in range(minW, maxW+1):
            if widthMap.get(i) != None:
                result.append(widthMap.get(i))
        return result
        
        
        