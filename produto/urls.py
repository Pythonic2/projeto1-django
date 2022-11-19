from django.urls import path
from .views import metodo

urlpatterns = [
    path('',metodo),

]