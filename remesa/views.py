from django.shortcuts import render


def home(request):
    context = {}
    return render(request, 'remesa/home.html', context)
