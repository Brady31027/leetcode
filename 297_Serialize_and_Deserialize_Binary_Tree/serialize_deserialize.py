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
        serialized_string = ' '.join(ans)
        return serialized_string    
            
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def split(input_str, seperator):
            seperator_size = len(seperator)
            start = 0
            while True:
                length = input_str.find(seperator, start)
                if length == -1:
                    yield input_str[start:]
                    return
                yield input_str[start:length]
                start = length + seperator_size
        def dfs():
            val = next(iterators)
            if val == '#': return None
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node
        iterators = iter(split(data, ' '))
        return dfs()
        
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
