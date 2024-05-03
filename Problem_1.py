'''
Time Complexity - O(n)
Space Complexity - O(logn)

Works on leetcode

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        #self.sumV = 0
        sumV = 0
        st = deque()
        #Iterative pre-order
        # st.append(root)#push root initially
        # while st:
        #     curr = st.pop() #pop from the stack
        #     print(curr.val)
        #     if curr.val >= low and curr.val <= high: #check value is within range
        #         sumV+=curr.val #add to sum
        #     if curr.right!=None and curr.val < high: #add the right node to stack first if curr val is less than high
        #         st.append(curr.right)
        #     if curr.left!=None and curr.val > low: #add the left node to stack next if curr val is greater than low
        #         st.append(curr.left)


        #iterative inorder traversal
        # while root or st:
        #     while root != None:
        #         st.append(root)
        #         if root.val > low:
        #             root = root.left
        #         else:
        #             root = None
        #     root = st.pop()
        #     if root.val >= low and root.val <= high:
        #         sumV+=root.val
        #     if root.val < high:
        #         root = root.right
        #     else:
        #         root = None

        # iterative postorder traversal
        st.append(root)
        prev = None
        while st:
            curr = st[-1]
            if prev == None or prev.left == curr or prev.right == curr:
                if curr.left != None:
                    st.append(curr.left)
                elif curr.right != None:
                    st.append(curr.right)
                else:
                    if curr.val >= low and curr.val <=high:
                        sumV+=curr.val
                    st.pop()
            elif curr.left == prev:
                if curr.right != None:
                    st.append(curr.right)
                else:
                    if curr.val >= low and curr.val <=high:
                        sumV+=curr.val
                    st.pop()
            elif curr.right == prev:
                if curr.val >= low and curr.val <=high:
                    sumV+=curr.val
                st.pop()
            prev = curr
        return sumV
        return self.dfs(root, low, high)
        
    
    def dfs(self, root, low, high):
        if root == None:
            return 0
        result = 0
        if root.val > low:
            result+=self.dfs(root.left, low, high)
        if root.val < high:
            result+=self.dfs(root.right, low, high)
        if root.val >= low and root.val <= high:
            result += root.val
        return result
        