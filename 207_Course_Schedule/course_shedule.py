class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if numCourses < 2 or len(prerequisites) < 2: return True
        
        while True:
            remove_cnt = 0
            nodes = [True] * numCourses
            for pre in prerequisites: nodes[pre[0]] = False
            for pre in prerequisites:
                if nodes[pre[1]] == True:
                    prerequisites.remove(pre)
                    remove_cnt += 1
            if len(prerequisites) == 0: return True
            elif remove_cnt == 0: return False
