from django.shortcuts import render

def main(request):
    return render(request, 'main.html')

def post_list(request):
    return render(request, 'post_list.html')

def contact(request):
    return render(request, 'contact.html')  # Проверим, что шаблон есть
