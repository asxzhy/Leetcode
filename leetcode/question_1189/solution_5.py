"""
This solution is basically same as solution 4, but it used count to get the frequency for each character.
"""

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        return min(text.count("b"), text.count("a"), text.count("l")//2, text.count("o")//2, text.count("n"))
