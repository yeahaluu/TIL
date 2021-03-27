import sys

sys.stdin = open('input_문자열비교.txt', 'r')

for tc in range(int(input())):
    str1 = input()
    str2 = input()

    # str1길이만큼 인덱스 들고와서 str2에 넣고 비교, 같은거 있으면 result = 1 할당.
    result = 0
    for idx in range(len(str2) - len(str1) + 1):
        if str2[idx:len(str1) + idx] == str1:
            result = 1

    # result = 1 이면 1, 0이면 0
    print('#{} 1'.format(tc + 1) if result else '#{} 0'.format(tc + 1))
