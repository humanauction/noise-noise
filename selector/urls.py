from django.urls import path
from . import views

app_name = 'selector'

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('selector/', views.SelectorView.as_view(), name='selector'),
]
