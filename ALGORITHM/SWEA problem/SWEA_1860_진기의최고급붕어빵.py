import sys

sys.stdin = open('input_붕어빵.txt', 'r')

for tc in range(1, int(input())+1):
    # N : 손님 수
    # M : 붕어빵 만드는데 걸리는 시간
    # K : M초 동안 만드는 붕어빵 개수
    N, M, K = map(int, input().split())
    customer = list(map(int,input().split()))

    time =  [0] * 11112  # 0 초 이상 11111 초 이하

    # customer이 방문 예약 시간 (time) 입력
    for t in customer:
        time[t] +=1

    #붕어빵 stack
    bungeppang = []
    result = 'Possible'
    for i in range(11112):  # 시간이 흐른다

        # M초 마다 붕어빵 저장소에 붕어빵 K개 추가
        if i!=0 and i%M ==0:
            for _ in range(K):
                bungeppang.append('bounge')

        # 만약 시간에 방문 예약이 있으면 붕어빵을 줘라.
        if time[i]:
            for _ in range(time[i]):
                # 붕어빵 줘야하는데 없으면 impossible!!
                if len(bungeppang) == 0:
                    result = 'Impossible'
                    break
                bungeppang.pop()

    print('#{} {}'.format(tc, result))



