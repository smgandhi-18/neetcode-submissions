class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagram_map = defaultdict(list)
        for word in strs:
            signature = "".join(sorted(word))
            anagram_map[signature].append(word)

        return list(anagram_map.values())

        #sorting each string and then N iterations so sorted() using timsort: Time. complx = O(N*KlogK)