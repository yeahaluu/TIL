for tc in range(1, int(input())+1):
    card = [int(i) for i in input().split()]
    player1 = [0] * 12  # 6자리 수로부터 각 자리 수를 추출하여 개수를 누적할 리스트
    player2 = [0] * 12

    result = 0

    for i in range(12):
        if i%2==0:
            player1[card[i]] +=1

            for t in range(10):
                if player1[t] >= 3:
                    result = 1

                if player1[t] and player1[t + 1] and player1[t + 2]:
                    result = 1

            if result ==1:
                break

        elif i%2:
            player2[card[i]] +=1

            for t in range(10):
                if player2[t] >= 3:
                    result = 2


                if player2[t] and player2[t + 1] and player2[t + 2]:
                    result = 2

            if result ==2:
                break

    print(f'#{tc} {result}')