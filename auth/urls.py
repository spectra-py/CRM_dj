from django.urls import path
from .views import SignUpView , GetCSRFToken


urlpatterns = [
    
    path('register/',SignUpView.as_view(), name='signup'),
    path('csrf-cookie/',GetCSRFToken.as_view())
]