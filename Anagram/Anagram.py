class Solution(object):
    def isAnagram(self, str1, str2):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """           
        list_str1 = list(str1)
        list_str1.sort()
        list_str2 = list(str2)
        list_str2.sort()

        return (list_str1 == list_str2)