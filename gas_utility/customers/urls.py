from django.urls import path
from . import views

app_name = 'customers'

urlpatterns = [
    path('submit/', views.submit_request, name='submit_request'),
    path('requests/', views.request_list, name='request_list'),
    path('requests/<int:pk>/', views.request_detail, name='request_detail'),
    path('account/', views.account_info, name='account_info'),
]
