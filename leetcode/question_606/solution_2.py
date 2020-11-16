"""
From leetcode discussion. Same method but used a variable to store the output
"""


class Solution:
    def tree2str(self, t) -> str:
        if t is None:
            return ""

        result = str(t.val)

        if t.left:
            result += "(" + self.tree2str(t.left) + ")"
            if t.right:
                result += "(" + self.tree2str(t.right) + ")"
        elif t.right:
            result += "()" + "(" + self.tree2str(t.right) + ")"

        return result
