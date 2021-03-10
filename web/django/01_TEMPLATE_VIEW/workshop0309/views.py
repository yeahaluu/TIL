from django.shortcuts import render


def dinner(request, menu, people_num):
    context = {
        'menu': menu,
        'people_num': people_num,
    }
    return render(request, 'workshop0309/dinner.html', context)
    