import sys
sys.stdin = open('input_Forth.txt','r')

for tc in range(1,int(input())+1):
    expression = input().split()

    stack = []
    for x in expression:
        # 숫자면 int로 바꿔서 집어넣어!
        if x.isdigit():
            stack.append(int(x))

        # 연산자면?
        elif x in ('/','+', '-', '*'):
            # stack에 2개 이상 안 들어있으면 error
            if len(stack) <=1:
                result = 'error'
                break

            # stack에서 숫자 두개를 뺀다.
            y = stack.pop()
            z = stack.pop()


            if x == '/':  # print(4//2) -> 2  print(4/2) -> 2.0
                tmp = z // y
            elif x == '+':
                tmp = z + y
            elif x == '-':
                tmp = z - y
            else:
                tmp = z * y

            stack.append(tmp)

        elif x == '.':
            result = stack.pop()

    if not len(stack)==0:
        result = 'error'

    print('#{} {}'.format(tc, result))

