
# valid Parenthesis
class Solution:
    def isValid(self, s: str) -> bool:
        dictionary_brackets = {'}':'{',')':'(', ']':'['}
        open_bracket = ('{','(','[')
        stack_bracket = []
        for each_char in s:
            if stack_bracket == [] or each_char in open_bracket:
                stack_bracket.append(each_char)
            elif(dictionary_brackets[each_char]==stack_bracket[-1]):
                stack_bracket.pop()
            else:
                return False
        return False if stack_bracket else True