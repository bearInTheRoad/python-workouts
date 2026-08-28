from typing import List, Optional
from collections import defaultdict, deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(values):
    if not values:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        return self.levelOrder_BFS(root)

    def levelOrderDep(self, tree, root, current_level=0):
        current_level += 1
        if not root:
            return
        if root.left:
            tree[current_level].append(root.left.val)
        if root.right:
            tree[current_level].append(root.right.val)

        if root.left:
            self.levelOrderDep(tree, root.left, current_level)
        if root.right:
            self.levelOrderDep(tree, root.right, current_level)

    def levelOrder_DFS(self, root: Optional[TreeNode]) -> List[List[int]]:
        tree = defaultdict(list)

        if root:
            tree[0] = [root.val]
            current_level = 0
            self.levelOrderDep(tree, root, current_level)

        return list(tree.values())

    def levelOrder_BFS(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        queue = deque([root])
        result = []

        while queue:
            level_size = len(queue)
            level_vals = []

            for _ in range(level_size):
                node = queue.popleft()

                level_vals.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level_vals)

        return result


test_case = [1, 2, 3, 4, None, None, 5]
root = build_tree(test_case)

solution = Solution()
print(solution.levelOrder(root))
