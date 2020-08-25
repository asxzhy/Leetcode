"""
I created a new function to get the frequency of the smallest character in list. Then, I counted how many numbers in words are greater than the numbers in queries
"""

class Solution:
    def numSmallerByFrequency(self, queries, words):
        queries = self.convertToNum(queries)  # get the length of the smallest character
        words = self.convertToNum(words)
        result = []

        for num in queries:
            # for every length in queries, check it with the length in words. count how many is greater than the queires' length
            length = 0
            for i in range(0, len(words)):
                if num < words[i]:
                    length += 1

            result.append(length)

        return result
        
        
        
    def convertToNum(self, words):
        for i in range(0, len(words)):
            words[i] = sorted(words[i])  # sort the words alphabetically

            if len(words[i]) == 1:
                words[i] = 1  # if it is a single character, the length will be one
            else:
                # otherwise check when the letter changes, get the number of letters when the first change in letter occurs
                for j in range(0, len(words[i]) - 1):
                    if words[i][j] != words[i][j + 1]:
                        words[i] = j + 1
                        break

                    # if there is no letter change, that means all the letters are the same.
                    if j == len(words[i]) - 2:
                        words[i] = len(words[i])

        return words
