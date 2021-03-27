import sys

sys.stdin = open('input_달팽이.txt', 'r')

for tc in range(int(input())):
    n = int(input())

    dr = [0, 1, 0, -1]  # 우하좌상
    dc = [1, 0, -1, 0]

    arr = [[0 for col in range(n)] for row in range(n)]

    # for i in range(1,n+1):
    #     arr[0][i-1] = i

    k = 0
    num = 0
    row = 0
    col = -1

    #
    for i in range(n * 2, 1, -1):  # 전체 움직이는 변의 횟수 [0][-1]에서 시작
        for _ in range(i // 2):  # 한 변에서 움직이는 횟수

            # 계속 증가하는 수를 넣어야하니까
            num += 1

            # dr, dc의 idx가 (k%4)번째 값이 반복
            row += dr[k % 4]
            col += dc[k % 4]
            # row와 col의 값에 num 넣기
            arr[row][col] = num
        # dr, dc의 다음 idx을 들고오기 위해!
        k += 1

    print('#{}'.format(tc + 1))
    for i in range(n):
        print(*arr[i])
