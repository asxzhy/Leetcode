"""
Use one list to store the number that can be rotated and another list stores corresponding rotated digits and with same index. Use a for loop to iterate from 1 to the
input number, and another for loop to convert every digit of that number to the rotated digits. If the number has digits that cannot be rotated, proceed to the next number.
Check if the rotated number is same as the number before rotating. If so, count one. Return the number of numbers that can be rotated and changes after rotation at the end.
"""

class Solution:
    def rotatedDigits(self, N: int) -> int:
        # these two lists is used to do number rotation
        num_before = ["0", "1", "8", "2", "5", "6", "9"]
        num_after = ["0", "1", "8", "5", "2", "9", "6"]
        num_rotated = ""  # used to store the number after rotation
        result = 0  # the output
        
        for i in range(1, N + 1):
            for num in str(i):  # if the number is greater than 9 there are going to be more than two digits we need to rotate
                if num in num_before:  # add the rotated number to the num_rotated
                    num_rotated += num_after[num_before.index(num)]
                else:  # if the digit cannot be rotated, exit and proceed to the next digit
                    num_rotated = i
                    break
            
            if i != int(num_rotated):  # check if the number after rotation is different from the previous number
                result += 1

            num_rotated = ""  # reset to empty
        
        return result
