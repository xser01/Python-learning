#leetcode 20
class Solution:
    def isValid(self, s: str) -> bool:
        reverse0={
            ')':'(',
            ']':'[',
            '}':'{'
        }
        stack=[]
        for char in s:
            if char in '({[':
                stack.append(char)
            else:
                if stack and stack[-1]==reverse0[char]:
                    stack.pop()
                else:
                    return False
        return not stack