
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
    def lengthOfLongestSubstring(self, s):
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

class Solution:
    def characterReplacement(self, s, k):
        count = {}
        l=0
        res=0
        maxf=0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r],0)
            maxf = max(maxf,count[s[r]])
            while (r-l+1) - maxf > k:
                count[s[l]] -=1
                l+=1
            res = max(res,r-l+1)
        return res

class Solution:
    def minWindow(self, s, t):
        if t == "": return ""
        countT,window = {},{}
        for c in t:
            countT[c] = 1 + countT.get(c,0)
        have ,need = 0,len(countT)
        res ,resLen = [-1,-1],float('infinity')
        l=0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c,0)
            if c in countT and window[c] == countT[c]:
                have+=1
            
            while have == need:
                #curr length of string or frame (r-l+1)
                if (r-l+1) < resLen:
                    res = [l,r]
                    resLen = (r-l+1)
                #pop from the left of our window/frame
                window[s[l]] -=1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -=1
                l += 1
        l,r = res
        return s[l:r+1] if resLen != float('infinity') else ""


class Solution:
    def reverseList(self, head):
        prev, curr = None,head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev



class Solution:
    def hasCycle(self, head):
        slow,fast = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False        

if __name__ == "__main__":
    sol = Solution()
    # res = sol.isValid('()')
    print(res)



