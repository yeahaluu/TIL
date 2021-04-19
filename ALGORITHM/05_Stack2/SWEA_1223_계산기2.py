for tc in range(1, 11):
    N = int(input())
    expression = input()

    # 후위연산식으로 만들기
    priority = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}

    stack = []
    result_lst = []
    expression = '(' + expression + ')'

    for token in expression:
        # 스택 연산 push()
        if token in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
            result_lst.append(token)
        elif token in ('+', '-', '*', '/'):
            tmp = stack.pop()
            if priority[token] > priority[tmp]:
                stack.append(tmp)
                stack.append(token)
            else:
                result_lst.append(tmp)
                stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            tmp = stack.pop()
            while tmp != '(':
                result_lst.append(tmp)
                tmp = stack.pop()
    expression2 = ''
    for s in result_lst:
        expression2 += s

    # 후위연산식 계산
    stack = []

    for token in expression2:
        if token in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
            stack.append(token)
        elif token in ('+', '-', '/', '*'):
            tmp1 = int(stack.pop())
            tmp2 = int(stack.pop())
            if token == '+':
                tmp3 = tmp2 + tmp1
            elif token == '-':
                tmp3 = tmp2 - tmp1
            elif token == '*':
                tmp3 = tmp2 * tmp1
            elif token == '/':
                tmp3 = tmp2 / tmp1
            stack.append(tmp3)

    result = stack.pop()

    print('#{} {}'.format(tc, result))