"""
Used a different method, the previous methods are searching if the input number's digit is a rotatable number. This method is searching if the rotatable and 
non-rotatable digits are in the input number. About 30ms faster than the previous solution
"""

class Solution:
    def rotatedDigits(self, N: int) -> int:
        result = 0  # output
        
        for i in range(1, N + 1):
            num = str(i)
            
            if "3" in num or "4" in num or "7" in num:
                # if these non-rotatable digits are in the number, continue to the next cycle
                continue
            if "5" in num or "2" in num or "9" in num or "6" in num:
                # if these any of these digits is in the number, that means the number changes no matter how many
                # rotatable digits that doesn't change are in the number
                result += 1
        
        return result
