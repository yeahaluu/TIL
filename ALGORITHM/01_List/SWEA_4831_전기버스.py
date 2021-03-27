import sys
sys.stdin = open('전기버스_input.txt','r')

# 각 충전기들의 거리 구하기 함수 (+ 출발에서 충전기까지)
def distance(Ms):
    distances = []
    distances.append(Ms[0]-0)
    for i in range(len(Ms)-1):
        distances.append(Ms[i+1]-Ms[i])
    return distances

# input (K: 최대 이동 수, N: 종점, M: 충전기 설치 개수, Ms: 충전기 설치 정류장 리스트)
for tc in range(int(input())):
    K, N, M = map(int, input().split())
    Ms = list(map(int, input().split()))

    # 충전기 설치 정류장 리스트에 종점 추가
    Ms.append(N)

    charge_count = 0  # 충전 횟수
    k_count = K  # 이동 수 카운트
    distances = distance(Ms)
    # print(len(distances), distances)

    # 충전기 설치 수만큼 반복
    for time in range(M+1):
        # 처음 출발할 때 못 가면 0 출력
        if (distances[time] > K):
            charge_count = 0  ####
            break
            # 한번 다음 정류장 갈 때마다, 남은 이동 수 - 다음 정류장 까지 거리
            # 최대 이동 남은 수가 충전기 거리보다 작으면 충전! 이때, 충전 수 카운트 +1, 최대이동 남은 수 원상복구
        if k_count < distances[time]:
            charge_count += 1
            k_count = K
            k_count -= distances[time]
        else:
            k_count -= distances[time]


    print('#{} {}'.format(tc+1,charge_count))
