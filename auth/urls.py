from django.urls import path
from .views import SignUpView , GetCSRFToken,LoginView,LogoutView,CheckAuthenticateView


urlpatterns = [
    
    path('sign-up/',SignUpView.as_view(), name='signup'),
    path('csrf-cookie/',GetCSRFToken.as_view()),
    path('Sign-in/',LoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('authenticated/',CheckAuthenticateView.as_view(),name='status')


    
]