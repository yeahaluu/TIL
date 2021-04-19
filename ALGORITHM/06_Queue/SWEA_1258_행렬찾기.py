

for tc in range(1, int(input())+1):
    N = int(input())
    chemicals = [[int(i) for i in input().split()] for _ in range(N)]

    c_stack = []

    for row in range(N+1):
        c_stack.append(-1)
        for col in range(N):
            if (chemicals[row][col] != 0: and chemicals[row][col+!] ==0) or (chemicals[row][col] == 0: and chemicals[row][col+1] !=0):
                c_stack.append(col)
        c_stack.append(N)

        for