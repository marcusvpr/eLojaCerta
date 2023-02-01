from django.urls import path
from . import views


app_name = 'tabelaInt'

urlpatterns = [
    path('', views.TabelaInts.as_view(), name="lista"),
    path('<int:tabelaIntId>', views.detalhe, name='detalhe'),
]
