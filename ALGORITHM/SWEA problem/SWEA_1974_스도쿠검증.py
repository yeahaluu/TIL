import sys

sys.stdin = open('input_스도쿠검증.txt', 'r')

for tc in range(1, int(input())+1):
    sdoku = [[int(i) for i in input().split()]for _ in range(9)]

    # result 초기값 설정
    result = 1

    # 방문도장 찍는 방법으로 모든 숫자가 다 있지 않고 하나라도 False가 있으면 result = 0
    # 행 검사
    for row in range(9):
        visited = [False] * 9
        for col in range(9):
            visited[sdoku[row][col]-1] = True
        for i in visited:
            if i == False:
                result = 0

    # 열 검사
    for col in range(9):
        visited = [False] * 9
        for row in range(9):
            visited[sdoku[row][col] - 1] = True
        for i in visited:
            if i == False:
                result = 0

    # 3*3 검사
    for i in range(0, 7 ,3):
        visited = [False] * 9
        for row in range(i,i+3):
            for col in range(i,i+3):
                visited[sdoku[row][col] - 1] = True
        for i in visited:
            if i == False:
                result = 0

    print('#{} {}'.format(tc,result))

