from datetime import datetime
import email
import os
from pyexpat.errors import messages
from django import forms
from django.conf import settings
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from config.africastalkings import child_password_and_phone_number_send_to_phone, send_otp_to_validate_phone
from transaction.models import Transaction
from pytz import utc
from otp.models import Otps
from otp.views import random_number_generator

from users.EmailBackEnd import EmailBackEnd

from users.models import Account
from notifications.signals import notify
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

from wallet.models import Wallet


def error_404_view(request, exception):
    return render(request,'404.html')

def delete_child(request, id):
  member = Account.objects.get(id=id)
  member.delete()
  return redirect('users:ptc_parent_dashboard')




def splash(request):
    return render(request,'splash.html')

def landing(request):
    return render(request,'landing.html')

def login_user(request):
    username = password = ''

    if request.method == "POST":
        password = request.POST['pin']
        phone_number = request.POST['phone']
        # password = make_password('password')
        # print(password)
        user = authenticate(username=phone_number, password=password)
        # if user is not None:
        login(request,user)
            #messages.info(request, f"You are now logged in as {phone_number}.")
            # playsound('C:\\Users\\admin\\Downloads\\note.mp3')
        acc = Account.objects.all()
        for acc in acc:
            print(acc.phone_number)
            if acc.phone_number == phone_number:
                print(acc.is_parent)
                if acc.is_parent == True:
                    return redirect("users:ptc_parent_dashboard")
                if acc.is_child == True:
                    return redirect("users:ptc_child_dashboard")
    return render(request,"login.html")

def logout_view(request):
    logout(request)
    print("Loged Out")
    return redirect('users:ptc-login')

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect



# def login_user(request):
#     data = {}
#     if request.method == "POST":
#         pin = request.POST.get('pin')
#         phone = request.POST.get('phone')
#         print(pin)
#         print(phone)

#         user=EmailBackEnd.authenticate(request,username=phone,password=pin)
#         # if user!=None:
#         login(request,user)
#         print("Authenticated")
#         print("UnAuthenticated")

#         if phone == "254717713943" and pin == "1234":
#             return redirect('parent/dashboard/')
        
#         elif phone == "254717713941" and pin == "1234":
#             return redirect('child/dashboard/')
        
#         else:
#             return redirect('users:ptc-login')

#     return render(request,'login.html',data)



from django.contrib.auth.hashers import make_password, check_password




def register(request):
    data = {}
    if request.method == "POST":
        username = request.POST.get('username')
        phone = request.POST.get('phone')
        country = request.POST.get('country')
        pin = request.POST.get('pin')

        users = Account.objects.all()
        for user in users:
            if user.phone_number == phone:
                return redirect("")

        #Check if the user already exists
        # user = Account.objects.all()
        # for user in user:
        #     if user.phone_number == phone:
        #         return redirect('users:ptc-login')
        #     else:
        #         return redirect('users:ptc-register')
        
        

        # pin = make_password('pin')
        # print(pin)
        
        

        # parent = Account(
        #         phone = phone,
        #         username = username,
        #         country = country,
        #         password=pin
        #     )
        # parent.save()

        #     create a custom user with the phone number as the username and email backend as the password
        parent = Account(
            phone_number = phone,
            user_name = username,
            country = country,
            password=make_password(pin),
            email = phone + "@gmail.com"
        )
        parent.save()
        user = authenticate(request,username=phone,password=pin)
        login(request,parent)
        # except:
        print("Error")

        
        # parent = Account.objects.create_user(
        #         phone_number = phone,
        #         user_name = username,
        #         password=make_password(pin),
        #         email = "parent@gmail.com",
        # )
        # login(request,parent)
        

        print("Authenticated")
        print(make_password(pin))
        parent.is_parent = True
        
        parent.save()

        #authenticate the user to remove the error anonoymous user _meta object
        # user = authenticate(username=phone, password=pin)
        # login(request,user)

        phonenumber = phone
        otp_number = random_number_generator(size=4)
        try:
            #Check number if it exist
            check_number_if_otp_exists = Otps.objects.filter(phone_number=phone)
        except:
            check_number_if_otp_exists = {}
            
        if bool(check_number_if_otp_exists) == False:
            otp = Otps(
                    phone_number = phone,
                    otp = otp_number
            )
            print(otp_number)
            send_otp_to_validate_phone(
                phone=phone,
                otp=otp_number
            )
            otp.save()
            print("OTP Saved Sucessfull")

                # add otp id to the user model to authenticate before login
            try:
                Account.objects.filter(phone_number=phone).update(
                        otp=Otps.objects.filter(otp=otp_number))
            except:
                print("none")

        elif bool(check_number_if_otp_exists) == True:
            new_otp = Otps.objects.filter(phone_number=phone).update(otp=otp_number)
            print(otp)
            print("OTP updated")

        return redirect('otp/?phone='+phone)

    # except:
    #     return redirect('users:ptc-register')
    print("Done")

    

    return render(request,'parent/registration.html',data)

def reset_password(request):
    return render(request,'reset_password.html')

def otp(request):
    if request.method == "POST":
        phone = request.GET.get('phone')
        otp = request.POST.get('otp')

        #Validate otp to authenticate the user
        validate_otp = Otps.objects.all()
        print("test1")
        for otps in validate_otp:
            print(otps.otp)
            print(otps.phone_number)
            if  str(otp) == str(otps.otp) and str(phone)==str(otps.phone_number):
                print("test3")
                if datetime.now().replace(tzinfo=utc) <= (otps.expire_at.replace(tzinfo=utc)):
                    print("test4")
                # update validation and mark the otp was successfully validated
                    Otps.objects.filter(otp=otp).update(is_otp_authenticated=True)

                    print("Authenticated")
                    return redirect('users:ptc_parent_dashboard')
                else:
                    print("Fail")
            else:
                print("fail2")
    return render(request,'parent/otp.html')

def child_dashboard(request):
    return render(request,'child/dashboard.html')

def parent_dashboard(request):
    global wallet_balance
    user_id = request.user.id 
    user_phone = request.user.phone_number
    transactions = Transaction.objects.filter(sender=user_id).order_by('-id')

    children = Account.objects.filter(parent_id=user_id)
    
    def balance_func():
        wallet = Wallet.objects.filter(user_id=user_id)
        for wallet in wallet:
            wallet_balance = wallet.account_balance
            # x = wallet_balance.split(',',-3)
            # print(x)
            return wallet_balance
    
    print(user_id)
    if request.user.is_authenticated:
        print("Loged In User as "+request.user.user_name)
    
    data = {
        "balance" : balance_func(),
        "children" : children,
        "transactions" : transactions,
    }
    return render(request,'parent/dashboard.html',data)


def add_child(request):
    if request.method == "POST":
        username = request.POST.get('username')
        phone = request.POST.get('phone')
        country = request.POST.get('country')
        pin = random_number_generator(size=4)
        print("Try")
        

        child = Account(
                phone_number = phone,
                user_name = username,
                password=pin,
        )
        child.parent = Account.objects.get(id=request.user.id)
        child.is_child = True
        child.country = country
        child.user_type = 2
        child.save()
        response = child_password_and_phone_number_send_to_phone(
            phone=phone,
            password=pin,
            name=username
        )
        print(response)
        try:
            f = open(settings.MEDIA_ROOT + f"/africastalking/sms_consoles/{datetime.datetime.now().strftime('%Y-%m-%d')}.txt", "a+")
            f.write(f"{datetime.datetime.now()} - {response}\n")
            f.close()
        except Exception as e:
            try:
                os.mkdir(os.path.join(settings.MEDIA_ROOT, 'africastalking/'))
            except Exception as e:
                try:
                   os.mkdir(os.path.join(settings.MEDIA_ROOT, 'africastalking/sms_consoles/'))
                except:
                    pass
            f = open(settings.MEDIA_ROOT + f"/africastalking/sms_consoles/{datetime.now().strftime('%Y%m%d')}_stks.txt", 'a')
        f.write(str(response) + "\n")
    
        print("Saved Child")

    return render(request,'parent/add_child.html')



