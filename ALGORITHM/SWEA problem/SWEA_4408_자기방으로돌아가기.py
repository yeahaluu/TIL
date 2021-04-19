import sys

sys.stdin = open('input_자기방.txt', 'r')


def m_max(lst):
    max_n = lst[0]
    for i in range(len(lst)):
        if max_n < lst[i]:
            max_n = lst[i]
    return max_n


for tc in range(1, int(input()) + 1):
    N = int(input())

    visited = [0] * 200

    for idx in range(N):
        now, comeback = map(int, input().split())
        for idx in range(200):
            if comeback > now and (now-1)//2 +1 <= idx <= (comeback-1)//2 +1:
                visited[idx] +=1
            elif now > comeback and (comeback-1)//2 +1 <= idx <= (now-1)//2 +1:
                visited[idx] += 1

    print('#{} {}'.format(tc, m_max(visited)))
