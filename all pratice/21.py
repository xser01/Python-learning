#700,leetcode,easy


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        from collections import deque
        if root is None:
            return
        queue=deque()
        queue.append(root)
        while queue:
            node=queue.popleft()
            if node.val==val:
                return node
            elif val<node.val and node.left is not None:
                queue.append(node.left)
            elif val>node.val and node.right is not None:
                queue.append(node.right)
        return
#标准BFS
        


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return
        if val==root.val:
            return root
        elif val<root.val:
            return self.searchBST(root.left,val)
        elif val>root.val:
            return self.searchBST(root.right,val)
#DFS遍历解法




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return None
        while root:
            if root.val==val:
                return root
            elif val<root.val:
                root=root.left
            elif val>root.val:
                root=root.right
        return None
#更简洁的解法，不需要deque储存