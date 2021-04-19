
for tc in range(1, int(input())+1):
    # N : 화덕의 크기
    # M : 피자의 개수
    N, M = map(int, input().split())

    # 피자에 뿌려진 치즈의 양
    Ci = [0] + list(map(int,input().split()))


    #피자 번호
    pizza = 0

    oven = [0] * N

    for i in range(N):
        pizza += 1
        oven[i] = (pizza, Ci[pizza])

    # 오븐에 무언가 있을 때는 계속 돈다
    while oven:
        pizza_n, cheese = oven[0]

        # 입구쪽 화덕 제일 뒤로 옮기기
        for j in range(N-1):
            oven[j] = oven[j+1]

        # 치즈 절반 녹음
        cheese //= 2

        # 치즈가 0이 아니면
        if cheese:
            oven[N-1] = (pizza_n, cheese)  # 다시 화덕에 집어넣기
        # 치즈가 0이면
        else:
            if pizza < M:  # 남은 피자 있으면
                pizza +=1
                oven[N-1] = (pizza, Ci[pizza])  # oven에 남은 피자 넣기
            else:  # 남은 피자 없으면
                N -=1
                result, _ = oven.pop()
    print('#{} {}'.format(tc,result))




