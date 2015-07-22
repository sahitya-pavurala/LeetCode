class Solution:
    # @param {string[]} tokens
    # @return {integer}
    def evalRPN(self, tokens):
        
        operators = ["+","-","*","/"]
        check = []
        #base case
        if len(tokens) <= 2:
            return int(tokens[0])
        try:
            check.append(int(tokens[0]))
            check.append(int(tokens[1]))
        except:
            return None
        for i in range(2,len(tokens)):
            if tokens[i] in operators:
                opr = tokens[i]
                oprnd1 = check.pop(-2)
                oprnd2 = check.pop(-1)
                if opr == "+":
                    check.append(oprnd1 + oprnd2)
                elif opr == "-":
                    check.append(oprnd1 - oprnd2)
                elif opr == "*":
                    check.append(oprnd1 * oprnd2)
                elif opr == "/":
                    # doing this because division of negative numbers is sloppy in python
                    check.append(int(float(oprnd1)/oprnd2))
            else:
                check.append(int(tokens[i]))
        
        if len(check) > 1:
            return None
            
        return check[-1]
                    
                    
            
            