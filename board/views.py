from django.shortcuts import render

# Create your views here.


def kakao(request, template='login.html'):
    print(request)
    return render(request, template, {})
