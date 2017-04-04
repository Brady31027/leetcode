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
        if not root: return []
        ans, queue, queue2 = [root.val], [root], []
        flag = True # to solve cases such as [5,2,3,null,null,2,4,3,1]
        while len(queue) and flag:
            flag = False
            for node in queue:
                if node != '#' and node.left:
                    queue2.append(node.left)
                    ans.append(node.left.val)
                    flag = True
                else:
                    queue2.append('#')
                    ans.append("#")
                if node != '#' and node.right:
                    queue2.append(node.right)
                    ans.append(node.right.val)
                    flag = True
                else:
                    queue2.append('#')
                    ans.append('#')
            queue, queue2 = queue2, []
            
        for i in range(len(ans) - 1, 0, -1):
            if ans[i] == '#': ans.pop() #remove tailing #
            else: break
        return ans
            
            
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        # formula: the left/right children of root with index i are node with index (i*2+1) & (i*2+2)
        data_size = len(data)
        if len(data) == 0: return None
        node_list = [TreeNode(0) for _ in range(data_size)]
        for i in range(data_size):
            #print "incoming node {}".format(data[i])
            if data[i] != '#':
                node_list[i].val = data[i]
                
                left_child_idx = i * 2 + 1
                right_child_idx = i * 2 + 2
                
                if left_child_idx < data_size and data[left_child_idx] != '#':
                    #print "add left child {}".format(data[left_child_idx])
                    node_list[i].left = node_list[left_child_idx]
                if right_child_idx < data_size and data[right_child_idx] != '#':
                    #print "add right child {}".format(data[right_child_idx])
                    node_list[i].right = node_list[right_child_idx]
        return node_list[0]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
