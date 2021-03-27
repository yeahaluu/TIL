for tc in range(1, int(input()) + 1):
    n = int(input())
    tri = [ [] for i in range(1, n+1)]

    # 첫번째 값은 채워주기
    tri[0] += [1]


    # 0, 1, 2 행에 각 1, 2, 3 개의 원소
    for i in range(1, n):
        for j in range(0, i + 1):

            # num 에 자신의 왼쪽과 오른쪽 위 숫자를 더한다
            num = 0
            # 왼쪽 위 숫자가 존재하지 않으면 계산 X
            if j >= 1:
                num = tri[i - 1][j - 1]
            # 오른쪽 위 숫자가 존재하지 않으면 계산 X
            if j < len(tri[i - 1]):
                num += tri[i - 1][j]
            # 행에 값 추가
            tri[i].append(num)

    # 출력
    print('#{}'.format(tc))
    for i in range(n):
        for j in range(i+1):
            print(tri[i][j],end= ' ')
        print()

