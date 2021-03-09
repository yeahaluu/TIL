from django.shortcuts import render

# Create your views here.
import random


def lotto(request):
    lotto = random.sample(range(1,46), 6)
    context = {
        'lotto': sorted(lotto),  # [1, 2, 3, ...]
        'greeting' : 'Hello World!',
    }
    return render(request, 'workshop0308/lotto.html', context)  # context는 딕셔너리