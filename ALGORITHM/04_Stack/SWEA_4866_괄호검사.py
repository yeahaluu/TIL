import sys

sys.stdin = open('input_괄호검사.txt', 'r')

for tc in range(1, int(input()) + 1):
    sentence = input()

    #stack 만들기
    stack = []
    # top = -1

    # sentence의 하나씩 넣어!
    for i in range(len(sentence)):

        # 여는 괄호일 때 stack안에 넣어!
        if sentence[i] == '{' or sentence[i] == '(':
            stack.append(sentence[i])
            # top += 1

        # 닫는 괄호일 때 stack에 pop으로 뺀 여는 괄호가 세뚜세뚜인지 봐야해
        elif sentence[i] == '}' or sentence[i] == ')':
            # 여는괄호고 뭐고 아무것도 없네
            if len(stack) == 0:
                stack = ['Fail']
                break
            # 세뚜세뚜가 아니네
            elif (sentence[i] == '}' and stack[-1] == '(') or (sentence[i] == ')' and stack[-1] == '{'):
                stack = ['Fail']
                break
            # 가능!
            else:
                stack.pop()
                # top -= 1

    if len(stack) == 0:
        print('#{} 1'.format(tc))
    else:
        print('#{} 0'.format(tc))
