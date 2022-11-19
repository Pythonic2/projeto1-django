from django.urls import path
# .  referencia propria pasta
from . import views

#/blog/
urlpatterns = [
    path('', views.index)

]
