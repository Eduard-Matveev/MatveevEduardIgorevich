from django.shortcuts import render

def index(request):
    data = {
        'title': 'Главная страница',
        'values': ['Выполнил студент группы БИб-22Э1', 'Матвеев Эдуард Игоревич'] 
    }
    return render(request,'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')  
