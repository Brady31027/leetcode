class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        # build up graph
        degree = [0] * numCourses
        children = [[] for x in range(numCourses)]
        for c, p in prerequisites:
            degree[c] += 1
            children[p].append(c)
        unvisited_course = set(range(numCourses))
        if not prerequisites: return list(unvisited_course)
        
        #bfs
        has_node_being_deleted = True
        queue_ans = []
        while has_node_being_deleted and len(unvisited_course):
            has_node_being_deleted = False
            removed_nodes = []
            for course in unvisited_course:
                if degree[course] == 0:
                    for child in children[course]:
                        degree[child] -= 1
                    removed_nodes.append(course)
                    has_node_being_deleted = True
            for node in removed_nodes:
                queue_ans.append(node)
                unvisited_course.remove(node)
        return [] if len(unvisited_course) else queue_ans
            
            
        
