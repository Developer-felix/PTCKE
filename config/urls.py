
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from transaction.views import LNMCallbackUrlView

from ussd.views import ussd_callback

urlpatterns = [
    path('mpesa_callback/',LNMCallbackUrlView,name='LNM_callback'),
    path('admin/', admin.site.urls),
    path("ussd_callback/",ussd_callback,name="get-ussd_callback"),
    path('',include('users.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)