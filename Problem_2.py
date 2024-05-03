'''
Time Complexity - O(n).
Space Complexity - O(n)
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        #Using BFS approach
        # if root == None:
        #     return ""
        # s=""
        # queue = deque()
        # queue.append(root)
        # while queue:
        #     curr = queue.popleft() 
        #     if curr == None:
        #         s=s+"*"+" "
        #     else:
        #         s = s+str(curr.val)+" "
        #     if curr != None:
        #         queue.append(curr.left)
        #         queue.append(curr.right)
        # return s

        #Using DFS Approach
        if root==None:
            return ""
        self.s=""
        self.helper(root)
        print(self.s)
        return self.s.rstrip()

    def helper(self, root):
        #serialization using Pre-order
        if root == None:
            self.s=f"{self.s}*"+" "
            return
        self.s = f"{self.s}{root.val} "
        self.helper(root.left)
        self.helper(root.right)
        
            
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        #deserialization dfs(Pre-order)
        if len(data) == 0:
            return None
        
        arr = data.split(sep = " ")
        # print(arr)
        self.idx = 0
        root = TreeNode(int(arr[self.idx]))
        self.idx+=1
        self.deserializeHelper(root, arr)
        #deserialization BFS
        # if data == "":
        #     return None
        # print(data)
        # arr = data.split(sep = " ")
        # queue = deque()
        # idx = 0
        # root = TreeNode(arr[idx])
        # idx+=1
        # queue.append(root)
        # while queue:
        #     curr = queue.popleft()
        #     if arr[idx] != "*":
        #         curr.left = TreeNode(arr[idx])
        #         queue.append(curr.left)
        #     idx+=1
        #     print(idx, curr.val)
        #     if arr[idx] != "*":
        #         curr.right = TreeNode(arr[idx])
        #         queue.append(curr.right)
        #     idx+=1
        # return root
        return root

    def deserializeHelper(self, curr, arr):
        #deserialization Pre-order
        if curr == None:
            return
        if arr[self.idx] != "*":
            # print(f"{self.idx} {arr[self.idx]}")
            curr.left = TreeNode(int(arr[self.idx]))
        self.idx+=1
        self.deserializeHelper(curr.left, arr)
        if arr[self.idx] != "*":
            # print(f"{self.idx} {arr[self.idx]}")
            curr.right = TreeNode(int(arr[self.idx]))
        self.idx+=1
        self.deserializeHelper(curr.right, arr)


        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))