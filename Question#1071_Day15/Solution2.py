"""
This solution is from leetcode's discussion section. This solution uses a recursive function. It makes sure that the first string is always longer than the second string. 
Then, eliminate letters in string one which are exact same as string two. When one of the string becomes empty, the letters left in the other string will be the answer.
"""

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) < len(str2):  # makes sure the str2 is always shorter than str1
            return self.gcdOfStrings(str2, str1)
        
        if str2 != str1[:len(str2)]:  # if str2 is not a substring of str1 starting at the first index, there won't be a common substring for them
            return ""
        
        if len(str2) == 0:  # if string 2 is alreay empty after some amount of elimination, return the str1
            return str1
        
        return self.gcdOfStrings(str1[len(str2):], str2)  # eliminate the part that is same as str2
