"""
In this solution, I created another function to convert the email to it's actual email address. Then, I used a set to store all the email addresses. The if statement in function 
numUniqueEmails can be omitted because set does not allow duplicated elements. At the end, I returned the length of the set to get the actual email address we are sending to.
"""

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        result = set()  # use a set to get rid of duplicates
        for email in emails:
            address = self.getActualEmail(email)  # get the email address
            if address not in result:
                result.add(address)  # if it's a new address, add it to the set
        
        return len(result)  # return the length of the set

    
    def getActualEmail(self, email):
        # used to get the actual email address
        email = email.split("@")  # split the address to local name and domain name
        result = ""
        
        for l in email[0]:
            if l == ".":  # ignore the periods in local name
                continue
            if l == "+":  # ignore everything after the plus sign
                break
            result += l
        
        return result + "@" + email[1]  # return the actual email adress
