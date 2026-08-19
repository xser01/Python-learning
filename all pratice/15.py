# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        from collections import deque
        queue=deque()
        queue.append(root)
        count=0
        cen=0
        need_while=0
        while queue:
            if cen==0:
                cen=len(queue)
            node=queue.popleft()
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
            need_while+=1
            if need_while==cen:
                cen=0
                need_while=0
                count+=1
        return count

'''
while queue:
    level_size = len(queue)

    for _ in range(level_size):
        node = queue.popleft()

        # 处理 node

        # 加入下一层节点

    depth += 1
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return max(
            self.maxDepth(root.left)
            ,self.maxDepth(root.right)
        )+1