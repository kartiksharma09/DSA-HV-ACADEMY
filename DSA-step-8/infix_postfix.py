stack = []
precedence = {"^":3,"/":2,"*":2,"+":1,"-":1,"(":0}


def infixToPostfix(string):
    expression=""
    for i in string:
        if i in ["^","/","*","+","-"]:
            if not stack:
                stack.append(i)
            else:
                while len(stack)>0 and precedence[stack[-1]] >= precedence[i]:
                    expression+=stack.pop()
                else:
                    stack.append(i)
        elif i=="(":
            stack.append(i)
        elif i==")":
            while stack[-1]!="(":
                expression+=stack.pop()
            stack.pop()
        else:
            expression+=i

    while stack:
        expression+=stack.pop()
    return expression

string = input()
print(infixToPostfix(string))