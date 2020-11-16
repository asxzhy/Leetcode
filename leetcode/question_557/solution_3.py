"""
From discussion in leetcode. reverse the word order first. For example,
"I am a student" to "student a am I", and then reverse the entire string to
"I ma a tneduts"
"""


class Solution:
    def reverse_words(self, s: str) -> str:
        return " ".join(s.split()[::-1])[::-1]
