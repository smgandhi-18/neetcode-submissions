class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        record = {}   #empty dictionary or hash map
        for char in s:
            record[char] = record.get(char, 0) + 1
        
        for char in t:
            if char not in record or record[char] == 0:
                return False
            record[char] -= 1
        
        return True

        # return Counter(s) == Counter(t)

        