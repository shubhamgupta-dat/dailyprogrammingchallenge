class TreeNode(object):
    def __init__(self, x=None):
        self.val = x
        self.left = None
        self.right = None


class TreeSolution(object):

    def preorder(self, root):
        A = []
        if root is not None:
            A.append(root.val)
            if root.left is not None:
                A.extend(self.preorder(root.left))
            else:
                A.append(None)
            if root.right is not None:
                A.extend(self.preorder(root.right))
            else:
                A.append(None)
            return A
        else:
            return None


    def serialize(self, root:TreeNode):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        A =  self.preorder(root)
        if A is None:
            return None
        return ','.join(list(map(str, A)))

    def deserialize(self, data:TreeNode):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        if data is None:
            return None
        def helper(lst):
            first = lst.pop(0)
            if first is None:
                return None
            else:
                root = TreeNode(first)
                root.left = helper(lst)
                root.right = helper(lst)
                return root
        A = data.split(',')
        A = [int(a) if a!='None' else None for a in A ]
        return helper(A)


    def preorder_traversal(self, root:TreeNode):
        A = []
        if root is not None:
            A.append(root.val)
            A.extend(self.preorder_traversal(root.left))
            A.extend(self.preorder_traversal(root.right))
        return A

    def count_univals(self, root:TreeNode):
        """
        Returns the count of unival trees. Its important to note that how this question was asked. Universal
        value tree has been here identified as where left node and right are equal, even if they are none.
        :type root: TreeNode
        :return count: int
        """
        # The Daily Coding Probelems version ie all nodes under it have the same value.
        count = 0
        if root is not None:
            if root.left is None or root.right is None or root.left.val==root.right.val:
                count+=1
            count+=self.count_univals(root.left)
            count+=self.count_univals(root.right)
        return count


if __name__ == '__main__':
    solution = TreeSolution()
    traversal_string = '1,0,0,None,None,0,None,None,1,None,1,None,None'
    unival_tree = solution.deserialize(traversal_string)
    print(solution.count_univals(unival_tree))