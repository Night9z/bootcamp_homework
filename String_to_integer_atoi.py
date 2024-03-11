class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        i = 0
        n = len(s)
        result = 0
        sign = 1  
        
        while i < n and s[i] == ' ':
            i += 1
        if i < n and s[i] == '-':
            sign = -1
            i += 1
        elif i < n and s[i] == '+':
            i += 1
        
        while i < n and s[i].isdigit():
            result = result * 10 + int(s[i])
            i += 1

            if result * sign < INT_MIN:
                return INT_MIN
            if result * sign > INT_MAX:
                return INT_MAX
        
        result *= sign
        
     
        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX
        
        return result

