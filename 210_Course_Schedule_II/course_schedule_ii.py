class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        # build up graph
        unvisited_course, graph = set(), collections.defaultdict(set)
        for i in range(numCourses): graph[i] = set()
        for c, p in prerequisites: graph[c].add(p)
        
        # find leaf
        queue1, queue2, queue_ans = [], [], []
        for course in range(numCourses):
            if len(graph[course]) == 0: # indep. node
                queue1.append(course)
                queue_ans.append(course)
            unvisited_course.add(course)
        if not prerequisites: return list(unvisited_course)
        #bfs
        has_node_being_deleted = True
        while has_node_being_deleted and len(unvisited_course):
            has_node_being_deleted = False
            for course in queue1:
                if course in unvisited_course: 
                    unvisited_course.remove(course)
                    has_node_being_deleted = True
                # update graph
                for key in graph:
                    graph[key].discard(course) # remove parent for every node
                    if key in unvisited_course and key not in queue1 and key not in queue2 and len(graph[key]) == 0:
                        queue2.append(key)
            queue_ans += queue2
            queue1, queue2 = queue2, []
        return [] if len(unvisited_course) else queue_ans
            
            
        
