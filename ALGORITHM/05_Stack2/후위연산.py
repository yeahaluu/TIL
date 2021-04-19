expression ='6+5*(2-8)/2'

priority = {'+':1, '-': 1, '*':2, '/':2, '(': 0}

stack = []
result_lst = []
expression = '('+ expression + ')'

for token in expression:
    # 스택 연산 push()
    if token in ('0','1','2','3','4','5','6','7','8','9'):
        result_lst.append(token)
    elif token in ('+','-','*','/'):
        tmp = stack.pop()
        if priority[token] > priority[tmp]:
            stack.append(tmp)
            stack.append(token)
        else:
            result_lst.append(tmp)
            stack.append(token)
    elif token =='(':
        stack.append(token)
    elif token == ')':
        tmp = stack.pop()
        while tmp !='(':
            result_lst.append(tmp)
            tmp = stack.pop()

print(*result_lst)
