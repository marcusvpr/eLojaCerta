from django.urls import path
from . import views


app_name = 'contatos'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:contatoId>', views.detalhe, name='detalhe'),
    path('busca/', views.busca, name="busca"),
]
