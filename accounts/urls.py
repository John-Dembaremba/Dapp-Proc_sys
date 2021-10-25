from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import signup_view, update_profile

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('settings/account/', update_profile, name='my_account'),
        
]
