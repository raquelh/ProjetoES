from django.urls import path
from . import views

urlpatterns = [
    path('', views.cadastroF_list, name='cadastroF_list'),
]
