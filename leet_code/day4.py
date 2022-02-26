
# valid Parenthesis
class Solution:
    def isValid(self, s):
        dictionary_brackets = {
            '}':'{',
            ')':'(',
            ']':'['
             }
        open_bracket = ('{','(','[')
        stack_bracket = []
        # s = "()"
        # s = "()[]{}"
        for each_char in s:
            if stack_bracket == [] or each_char in open_bracket:
                stack_bracket.append(each_char)
            elif(dictionary_brackets[each_char]==stack_bracket[-1]):
                stack_bracket.pop()
            else:
                return False
        return False if stack_bracket else True


def lengthOfLongestSubstring(s):
        if len(set(s)) == len(s):                       
            return len(s)
        substring = ''
        maxLen = 1
        for i in s:
            if i not in substring:                      
                substring = substring + i
                maxLen = max(maxLen, len(substring))    
            else:                                       
                substring = substring.split(i)[1] + i   
        return maxLen


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset = set()
        l=0
        res=0
        for r in range(len(s)):
            while s[r] in hashset:
                hashset.remove(s[l])
                l+=1
            hashset.add(s[r])
            res = max(res,r-l+1)
        return res

if __name__ == "__main__":
    sol = Solution()
    # res = sol.isValid('()')
    print(res)



