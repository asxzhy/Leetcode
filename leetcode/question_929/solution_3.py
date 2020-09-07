"""
This solution is same as the previous one, but merged the split and replace to one line.
"""

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        result = set()  # use a set to get rid of duplicates
        for email in emails:
            # get the email address
            address = email.split("@")
            address[0] = address[0].split("+")[0].replace(".", "")
            
            result.add(address[0] + "@" + address[1])  # add the address to the set
            
        return len(result)  # return the length of the set
