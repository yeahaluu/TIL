from django.shortcuts import render
from django.http.response import HttpResponse
import requests
import random

# 사용자가 입력할 form & input 용 **HTML을 제공**
def ping(request):
    return render(request, 'practice0309/ping.html')

def pong(request):
    # 안 씀? x 안 넘어옴 o
    kr_name = request.GET.get('kor-name')  # GET 방식으로 들어온 요청방식을 뽑겠습니다.(get)
    en_name = request.GET.get('eng-name')
    fullname =  kr_name + en_name,
    context={
        'fullname': fullname
    }
    return render(request, 'practice0309/pong.html', context)


def var_route(request, value):
    print(type(value))
    return HttpResponse(value)

def lotto(request, no):
    # 1. 현실 로또 번호 가져온다.
    url = f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={no}'
    lotto = requests.get(url).json()

    lotto_num = []
    for k, v in lotto.items():
        if k in ('drwtNo1', 'drwtNo2','drwtNo3','drwtNo4','drwtNo5','drwtNo6'):
            lotto_num.append(v)
        elif k == 'bnusNo':
            bonus_num = v
    
    result = {'1등':0, '2등': 0, '3등':0, '4등':0, '5등':0, '꽝':0}

    # 2. 1000번
    for i in range(1000):
        my_nums = random.sample(range(1,46),6)

        # 3. 현실 번호와 내가 추첨한 번호를 비교한다.
        cnt = 0
        bonus = 0
        for my_num in my_nums:
            if my_num in lotto_num:
                cnt +=1
            elif my_num == bonus_num:
                bonus +=1

        # 4. 결과를 어딘가에 저장한다.
        if cnt == 6:
            result['1등']+=1
        elif cnt ==5 and bonus ==1:
            result['2등']+=1
        elif cnt ==5:
            result['3등'] +=1
        elif cnt ==4:
            result['4등'] +=1
        elif cnt == 3:
            result['5등'] +=1
        else:
            result['꽝'] +=1
    print(result)
    # 5. 잘 context에 비벼서 내보낸다.
    context= {
        'lotto_num': lotto_num,
        'bonus_num': bonus_num,
        'result' : result,
        'round': lotto['drwNo']
    }
    
    return render(request, 'practice0309/lotto.html', context)