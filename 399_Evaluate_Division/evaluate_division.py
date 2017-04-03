class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        graph = collections.defaultdict( lambda: collections.defaultdict(int))
        for (dividend, divisor), quotient in zip(equations, values):
            graph[dividend][divisor] = quotient
            graph[divisor][dividend] = 1.0 / quotient
        for node1 in graph:
            graph[node1][node1] = 1.0
            for node2 in graph:
                for node3 in graph:
                    if graph[node1][node2] and graph[node2][node3]:
                        graph[node1][node3] = graph[node1][node2] * graph[node2][node3]
        ans = []
        for dividend, divisor in queries:
            ans.append(graph[dividend][divisor] if graph[dividend][divisor] else -1.0)
        return ans
        
