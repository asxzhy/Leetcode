"""
Learnt that set is faster than list in searching whether or not something is in a set. A little faster than the previous solutions
"""

class Solution:
    def rotatedDigits(self, N: int) -> int:
        # these two lists is used to check if a digit can be rotated and determines if the digit does not change
        rotatable = set(["0", "1", "8", "2", "5", "6", "9"])
        not_changing = set(["0", "1", "8"])
        diff = False  # used to determine if the number after rotatio changes
        result = 0  # the output
        
        for i in range(1, N + 1):
            for num in str(i):  # if the number is greater than 9 there are going to be more than two digits we need to rotate
                if num in rotatable:
                    if not num in not_changing:
                        # check if the digit can be rotated, if so check if the number changes after rotation
                        diff = True
                else:
                    # if the digit cannot be rotated, exit and proceed to the next digit
                    diff = False
                    break
            
            if diff:  # check if the number after rotation is different from the previous number
                result += 1
            diff = False # reset difference to false
        
        return result
