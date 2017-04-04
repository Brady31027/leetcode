# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        ans = []
        def dfs(root):
            if not root:
                ans.append('#')
                return
            ans.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return ' '.join(ans)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def convert_str_to_iterator(source, seperator):
            start, seperator_size, index = 0, len(seperator), 0
            while True:
                index = source.find(seperator, start)
                if index == -1: # not found
                    yield(source[start:])
                    return
                yield(source[start: index])
                start = index + seperator_size
        
        def dfs():
            val = next(iterators)
            if val == '#': return None
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node
        iterators = iter(convert_str_to_iterator(data, ' '))
        return dfs()

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
