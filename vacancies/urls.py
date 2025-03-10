from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main_page'),
    path('post_list/', views.post_list, name='post_list_page'),
    path('post_list/contact.html', views.contact, name='contact_page'),
]
