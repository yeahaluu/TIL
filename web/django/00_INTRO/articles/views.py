from django.shortcuts import render
from django.http.response import HttpResponse
import random

def index(request):
    numbers = range(1,46)
    lotto = random.sample(numbers, 6)
    return HttpResponse(f'Today\'s pick: {sorted(lotto)}')


def mail(request):
    return HttpResponse('제 메일은 \'yeahaluu@gmail.com\' 입니다.')