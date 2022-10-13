from django.shortcuts import render, HttpResponse

# Create your views here.
from random import choice
from string import digits, ascii_lowercase, ascii_uppercase

menu = [
    {'title': 'Главная страница', 'url_name': 'home'},
    {'title': 'О сайте', 'url_name': 'about'},
]


def home(request):
    length_password = list(range(4, 17))
    return render(request, 'generator/home.html', {'length_password': length_password, 'menu': menu})


def password(request):
    symbols = ''
    dict_symbols = {'numbers': digits,
                    'special': '!@#$%^&*()?/',
                    'uppercase': ascii_uppercase,
                    'lowercase': ascii_lowercase
                    }
    # symbols = [dict_symbols[req] for req in list(dict_symbols) if request.GET.get(req)]

    for req in list(dict_symbols):
        if request.GET.get(req):
            symbols += dict_symbols[req]

    if not symbols:
        symbols += ascii_lowercase

    length = int(request.GET.get('length'))
    thepassword = ''.join([choice(symbols) for _ in range(length)])
    return render(request, 'generator/password.html', {'password': thepassword, 'menu': menu})


def about(request):
    return render(request, 'generator/about.html', {'menu': menu})
