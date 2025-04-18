from django.urls import path
from . import views

urlpatterns = [
    path("",views.accept_data, name='accept_data'),
    path('result', views.result, name='result'),
    path('jumble',views.jumble_word,name='jumble_word')
]

