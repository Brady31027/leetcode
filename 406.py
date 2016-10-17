class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        """
        sorting accoring to the following rules:
        (1). sorting by priority, higher priority comes first
        (2). sorting by height, shorter height comes first
        """
        sorted_people = sorted(people, key=lambda person: (-person[0], person[1]))
        """
        adjust each of every person according to his proirity
        """
        l_ans = []
        for person in sorted_people:
            l_ans.insert(person[1], person)
        return l_ans
