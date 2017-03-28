class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        """
        def get_height(root):
            visit_book = set([i for i in range(n)])
            visit_book.remove(root)
            depth = 0
            queue1 = [root]
            while visit_book:
                queue2 = []
                for node in queue1:
                    for edge in edges:
                        if node not in edge: continue
                        elif node == edge[0]:
                            queue2.append(edge[1])
                            visit_book.discard(edge[1])
                        elif node == edge[1]:
                            queue2.append(edge[0])
                            visit_book.discard(edge[0])
                queue1, queue2 = queue2, []
                depth += 1
            return depth
        """        
        if n < 3:
            if n < 2: return [0]
            else: return [0, 1]
            
        degree = {}
        for i in range(n): degree.update({i:0})
        for edge in edges:
            degree[edge[0]] += 1
            degree[edge[1]] += 1
        to_be_killed_d, to_be_killed_e = [], []
        while len(degree) > 2:
            for d_key in degree:
                if degree[d_key] == 1:
                    to_be_killed_d.append(d_key)
                    for edge in edges: 
                        if d_key in edge: edges.remove(edge)#to_be_killed_e.append(edge)
            for key in to_be_killed_d: del degree[key]
            for edge in to_be_killed_e: edges.remove(edge)
            to_be_killed_d, to_be_killed_e = [], []
            for d_key in degree: degree[d_key] = 0
            for edge in edges:
                degree[edge[0]] += 1
                degree[edge[1]] += 1
        if len(degree) == 1: return degree.keys()
        else:
            keys = []
            for key in degree: keys.append(key)
            return keys
