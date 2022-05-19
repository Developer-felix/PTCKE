
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('ptc_secret/', admin.site.urls),
    path('',include('users.urls')),
]
