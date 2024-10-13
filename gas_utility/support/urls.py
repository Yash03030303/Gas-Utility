from django.urls import path
from . import views

app_name = 'support'

urlpatterns = [
    path('manage/', views.manage_requests, name='manage_requests'),
    path('update/<int:pk>/', views.update_request_status, name='update_request_status'),
]
