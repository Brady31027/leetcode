class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node: return None
        queue, clone = [node], {node: UndirectedGraphNode(node.label)}
        while len(queue):
            current = queue.pop()
            for neighbor in current.neighbors:
                if neighbor not in clone:
                    queue.append(neighbor)
                    clone[neighbor] = UndirectedGraphNode(neighbor.label)
                clone[current].neighbors.append(clone[neighbor])
        return clone[node]
