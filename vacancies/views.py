from django.shortcuts import render
from .models import Vacancy
# Create your views here.


def vacancy_list(request):
    vacancies = Vacancy.objects.all()
    return render(request, 'vacancies/list.html', {'vacancies': vacancies})