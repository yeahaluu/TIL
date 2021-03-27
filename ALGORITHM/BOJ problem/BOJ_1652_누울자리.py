N = int(input())

room = [[s for s in input()] for _ in range(N)]

row_cnt = 0
col_cnt = 0

stack = []
stack.append(-1)
for row in range(N):
    # col만큼 돌면서 x인덱스 stack에 넣기
    # 벽도 넣어준다
    for col in range(N):
        if room[row][col] == 'X':
            stack.append(col)
    stack.append(N)
    # x의 인덱스의 차가 2보다 크면 자리가 있다!
    for i in range(len(stack)-1):
        sel1 = stack.pop()
        sel2 = stack.pop()
        if sel1-sel2 >2:
            row_cnt +=1
        stack.append(sel2)

stack = []
stack.append(-1)
for col in range(N):

    for row in range(N):
        if room[row][col] == 'X':
            stack.append(row)
    stack.append(N)

    for i in range(len(stack)-1):
        sel1 = stack.pop()
        sel2 = stack.pop()
        if sel1-sel2 >2:
            col_cnt +=1
        stack.append(sel2)

print(row_cnt, col_cnt)

