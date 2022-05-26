from django.urls import path
from transaction.views import LNMCallbackUrlView

from users.views import add_child, login_user, login_user,register,otp,reset_password,parent_dashboard,child_dashboard,splash,landing,logout_view
from wallet.views import top_up, top_up_success, transfer_cash

app_name = 'users'

urlpatterns = [
    path('', splash,name='ptc-splash'),
    path('landing/', landing,name='ptc-landing'),
    path('login/', login_user,name='ptc-login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register,name='ptc-register'),
    path('register/otp/', otp,name='ptc-otp'),
    path('reset_password/', reset_password,name='ptc-reset_password'),
    path('parent/dashboard/', parent_dashboard,name='ptc_parent_dashboard'),
    path('parent/add_child/', add_child,name='ptc_parent_add_child'),
    path('wallet/top_up/', top_up,name='ptc_wallet_top_up'),
    path('wallet/top_up/success/',top_up_success,name="ptc-wallet_top_up_success"),
    path('child/dashboard/', child_dashboard,name='ptc_child_dashboard'),
    path('child/top_up/<int:reciever_id>', transfer_cash,name='ptc_child_top_up'),
    path('lnm/', LNMCallbackUrlView,name="LNMCallbackUrlView"),

]

handler404 = 'users.views.error_404_view'
