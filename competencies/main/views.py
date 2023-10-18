from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from .forms import UserForm
from .models import Users


def index(request):
    users = Users.objects.all()
    if request.method == "POST":
        idcard = request.POST.get('value')
        return redirect('userCard', idcard=idcard)
    return render(request, 'main/index.html', {'title': 'Главная страница сайта',
                                               'users': users
                                               })


def userCard(request, idcard):
    context = {}
    user = Users.objects.get(pk=idcard)
    context['user'] = user
    # Внутри карточки можно еще посмотреть результаты того, как он прошел Оценку компетенций
    return render(request, 'main/userCard.html', context)


def addUser(request):
    context = {}
    form = UserForm(request.POST)
    if request.method == "POST" and "save" in request.POST:
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.fullname = user.surname + " " + user.name + " " + user.middleName
            user.save()
            form.save()
            return redirect('home')
    if "cancel" in request.POST:
        return redirect('home')
    context['form'] = form
    return render(request, 'main/addUser.html', context)


# 2.	Окно «Оценка компетенций»:
# Раздел «Профессионально-технические компетенции»:
# Кнопка «Загрузить матрицу компетенций» - возможность загрузки excel файл
# Кнопка «Назначить оценку» - при нажатии на кнопку открывается окно,
# где можно выбрать либо все подразделение либо весь отдел либо конкретных сотрудников и нажать на кнопку «Подтвердить»
# Раздел «Оценка личностных компетенций» - аналогичен подразделу «Профессионально-технические компетенции»
def assessmentOfCompetencies(request):
    context = {}
    user = Users.objects.all()
    context['title'] = 'Карточка сотрудника'
    context['user'] = user
    # Внутри карточки можно еще посмотреть результаты того, как он прошел Оценку компетенций
    return render(request, 'assessmentOfCompetencies/assessmentOfCompetencies.html', context)


# 3.	Окно «Материалы для оценки»
# Раздел «Материалы для тестирования»
# Здесь есть кнопки «Загрузить тестирование» - где можно выбрать Раздел знаний
# Раздел «Библиотека рекомендаций»
# Здесь кнопка «Загрузить учебные материалы» - можно выбрать Раздел знаний, к которому относится учебный материал
def materialsForEvaluation(request):
    context = {}
    user = Users.objects.all()
    context['title'] = 'Карточка сотрудника'
    context['user'] = user
    # Внутри карточки можно еще посмотреть результаты того, как он прошел Оценку компетенций
    return render(request, 'materialsForEvaluation/materialsForEvaluation.html', context)


# 4.	Окно «Анализ результатов»
# Здесь какие-нибудь круговые диаграммы, где можно посмотреть по процентам результаты прохождения оценки
# (например диаграмма Бригада КРС и на диаграмме 50% соответствуют уровню знаний и 50 % не соответствуют)
def analysisOfResults(request):
    context = {}
    user = Users.objects.all()
    context['title'] = 'Карточка сотрудника'
    context['user'] = user
    # Внутри карточки можно еще посмотреть результаты того, как он прошел Оценку компетенций
    return render(request, 'analysisOfResults/analysisOfResults.html', context)


def department_autocomplete(request):
    if request.GET.get('q'):
        q = request.GET['q']
        data = Users.objects.filter(department__contains=q).values_list('department', flat=True)
        json = list(data)
        return JsonResponse(json, safe=False)
    else:
        HttpResponse("No cookies")


def employee_autocomplete(request):
    if request.GET.get('q'):
        q = request.GET['q']
        data = Users.objects.filter(fullname__contains=q).values_list('fullname', flat=True)
        json = list(data)
        return JsonResponse(json, safe=False)
    else:
        HttpResponse("No cookies")

def structuralDivision_autocomplete(request):
    if request.GET.get('q'):
        q = request.GET['q']
        data = Users.objects.filter(structuralDivision__contains=q).values_list('structuralDivision', flat=True)
        json = list(data)
        return JsonResponse(json, safe=False)
    else:
        HttpResponse("No cookies")
