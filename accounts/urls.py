from django.urls import path, include
from .views import CustomSignupView, CustomLoginView, GuestAccessView

app_name = 'accounts'

urlpatterns = [
    path('', include('allauth.urls')),
    path('signup/', CustomSignupView.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('guest/', GuestAccessView.as_view(), name='guest_access'),
]
