from django.urls import path, include
from .views import GuestAccessView


urlpatterns = [
    
    # path('login/', CustomLoginView.as_view(), name='login'),
    # path('signup/', CustomSignupView.as_view(), name='signup'),
    path('guest/', GuestAccessView.as_view(), name='guest_access'),
    path('', include('allauth.urls')),
]
