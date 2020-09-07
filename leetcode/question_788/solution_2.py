"""
Same method, used a boolean diff to indicate if the digits changes. Previous solution's run time was about 200ms, this one is about 110ms
"""

class Solution:
    def rotatedDigits(self, N: int) -> int:
        # these two lists is used to do number rotation
        num_before = ["0", "1", "8", "2", "5", "6", "9"]
        num_after = ["0", "1", "8", "5", "2", "9", "6"]
        diff = False  # used to determine if the number after rotatio changes
        result = 0  # the output
        
        for i in range(1, N + 1):
            for num in str(i):  # if the number is greater than 9 there are going to be more than two digits we need to rotate
                if num in num_before:
                    if num_after[num_before.index(num)] != num:
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
