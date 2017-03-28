class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n < 3:
            if n < 2: return [0]
            else: return [0, 1]
        tree = collections.defaultdict(set) # node: set(neighbors)
        for u, v in edges:
            tree[u].add(v)
            tree[v].add(u)
        
        #find leaf
        queue1, queue2, unvisited_node = [], [], set()
        for node in range(n):
            if len(tree[node]) == 1: #this is leaf
                queue1.append(node)
            unvisited_node.add(node)
        
        while len(unvisited_node) > 2:
            for node in queue1:
                unvisited_node.remove(node)
                for neighbor in tree[node]:
                    if neighbor in unvisited_node:
                        tree[neighbor].remove(node)
                        if len(tree[neighbor]) == 1:
                            queue2.append(neighbor)
            queue1, queue2 = queue2, []
        return list(unvisited_node)
