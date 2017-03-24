class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        
        degrees : for child node, degree stands for the number of parents
        children : for parent node, children is the list containing child nodes
        """
        degrees = [0] * numCourses
        children = [[] for _ in range(numCourses)]
        courses = set(range(numCourses))
        # build up the graph
        for pre in prerequisites:
            degrees[ pre[0] ] += 1
            children[ pre[1] ].append(pre[0])
        # bfs
        has_node_being_deleted = True
        while has_node_being_deleted and len(courses):
            remove_courses = []
            has_node_being_deleted = False
            for x in courses:
                if degrees[x] == 0: # indep. node
                    has_node_being_deleted = True
                    remove_courses.append(x)
                    for child in children[x]: degrees[child] -= 1
            for x in remove_courses: courses.remove(x)
        return len(courses) == 0
