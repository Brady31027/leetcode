class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        tokens = IP.split('.')
        if len(tokens) == 4:
            for token in tokens:
                if not token: return "Neither"
                if token != '0' and len(token.lstrip('0')) != len(token): return "Neither"
                if re.sub(r'[0-9]', '', token): return "Neither"
                if int(token) > 255: return "Neither"
            return "IPv4"
        tokens = IP.split(':')
        if len(tokens) == 8:
            for token in tokens:
                if len(token) > 4 or len(token) < 1: return "Neither"
                if re.sub(r'[0-9a-fA-F]','', token): return "Neither"
            return "IPv6"
        return "Neither"
