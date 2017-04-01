class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        ticket_dict = collections.defaultdict(list)
        for src, dst in tickets: ticket_dict[src].append(dst)
            
        def dfs(src):
            left, right = [], []
            for dst in sorted(ticket_dict[src]):
                if dst not in ticket_dict[src]: continue
                ticket_dict[src].remove(dst)
                subtree = dfs(dst)
                if src in subtree:
                    left += subtree
                else:
                    right += subtree
            return [src] + left + right
        return dfs("JFK")
        
        
