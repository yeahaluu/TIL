import sys

sys.stdin = open('input_백만장자.txt', 'r')

for tc in range(1, int(input()) + 1):
    N = int(input())
    prices = list(map(int, input().split()))


    result = 0
    max_n = prices[N - 1]
    for i in range(N-1, -1, -1):

        if prices[i] < max_n:
            result += max_n - prices[i]

        elif prices[i] > max_n:
            max_n = prices[i]
    print('#{} {}'.format(tc,result))


##### 앞에서 좀 어려우면 뒤에서 부터 생각해보기