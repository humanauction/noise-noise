from django.urls import path
from .views import home

app_name = 'selector'

urlpatterns = [
    path('', home)
]
