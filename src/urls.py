from django.urls import path, include
from .views import home, jobs_view, post_jobs_view, bid_view, bidders_view, Welcome_view, bider_info_view, client_info_view

urlpatterns = [
    
    #path('', Welcome_view.as_view(), name='welcome'),
    path('home/', home, name='home'),
    path('jobs/<int:pk>/', jobs_view, name='jobs'),
    path('suppliers/<int:pk>/', bidders_view, name='bidders'),
    path('post-job/<int:pk>/', post_jobs_view, name='post'),  
    path('jobs/<int:pk>/bid/', bid_view, name='bid'), 
    path('jobs/<int:pk>/bider-info', bider_info_view, name='info'),
    path('jobs/<int:pk>/client-info', client_info_view, name='client-info'),
    path('', include('accounts.urls')),  
]
