class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        count = 0
        for byte in data:
            if count == 0:
                # 2 byte
                if byte >> 5 == 0b110:
                    count = 1
                # 3 byte
                elif byte >> 4 == 0b1110:
                    count = 2
                # 4 byte
                elif byte >> 3 == 0b11110:
                    count = 3
                # 1 byte
                elif byte >> 7 != 0b0:
                    return False
                elif byte >> 7 == 0b0:
                    count = 0    
            else:
                if byte >> 6 != 0b10:
                    return False
                count -= 1
        return count == 0
        
