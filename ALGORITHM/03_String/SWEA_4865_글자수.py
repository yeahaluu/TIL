import sys

sys.stdin = open('input_글자수.txt', 'r')

for tc in range(int(input())):
    # str1 중복 제거해서 각각으로 list에 넣어 input
    str1= list(set([s for s in input()]))
    str2= [s for s in input()]
    # print(str1, str2)

    str1_count = [0] * len(str1)
    for i in range(len(str2)):
        for j in range(len(str1)):
            if str2[i] == str1[j]:
                str1_count[j] += 1

    max_n = 0
    for n in str1_count:
        if max_n < n:
            max_n = n
    print('#{} {}'.format(tc+1, max_n))