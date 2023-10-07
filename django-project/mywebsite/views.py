from django.shortcuts import render

def home(request):
    context = {
        'title': 'Selamat Datang',
        'subtitle': 'Waktunya kita belajar Django',
    }
    return render(request, 'home.html', context)