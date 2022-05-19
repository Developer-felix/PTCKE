from django.urls import path

from users.views import login,register,otp,reset_password,parent_dashboard,child_dashboard

app_name = 'users'

urlpatterns = [
    path('', login,name='ptc-login'),
    path('register/', register,name='ptc-register'),
    path('register/otp/', otp,name='ptc-otp'),
    path('reset_password/', reset_password,name='ptc-reset_password'),
    path('parent/dashboard/', parent_dashboard,name='ptc_parent_dashboard'),
    path('child/dashboard/', child_dashboard,name='ptc_child_dashboard'),
]
