import datetime
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from pytz import utc
from otp.models import Otps
from otp.views import random_number_generator

from users.models import Account

users = [
    {
        "phone" : "25417713943",
        "pin" : "1234"
        "role" "1"
    },
    {
        "phone" : "25417713943",
        "pin" : "1234"
        "role" "1"
    },
    {
        "phone" : "25417713943",
        "pin" : "1234"
        "role" "1"
    },
    {
        "phone" : "25417713943",
        "pin" : "1234"
        "role" "1"
    },
    {
        "phone" : "25417713943",
        "pin" : "1234"
        "role" "1"
    },
    {
        "phone" : "25417713943",
        "pin" : "1234"
        "role" "1"
    },
]

def splash(request):
    return render(request,'splash.html')

def landing(request):
    return render(request,'landing.html')

def login(request):
    data = {}
    if request.method == "POST":
        pin = request.POST.get('pin')
        phone = request.POST.get('phone')
        print(pin)
        print(phone)

        if phone == "254717713943" and pin == "1234":
            return redirect('parent/dashboard/')
        
        elif phone == "254717713941" and pin == "1234":
            return redirect('child/dashboard/')
        
        else:
            return redirect('users:ptc-login')

    return render(request,'login.html',data)

def register(request):
    data = {}
    if request.method == "POST":
        username = request.POST.get('username')
        phone = request.POST.get('phone')
        country = request.POST.get('country')
        pin = request.POST.get('pin')
        is_parent = True

        try:
            parent = Account(
                phone = phone,
                pin = pin,
                username = username,
                country = country
            )
            parent.save()

            phonenumber = phone
            otp_number = random_number_generator(size=4)
            try:
                #Check number if it exist
                check_number_if_otp_exists = Otps.objects.get(phone_number=phone)
            except:
                check_number_if_otp_exists = {}
            
            if bool(check_number_if_otp_exists) == False:
                otp = Otps(
                    phone_number = phone,
                    otp = otp_number
                )
                print(otp_number)
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

        except:
            return redirect('users:ptc-register')
        print("Done")

        print(username)

        print(phone)

    return render(request,'parent/registration.html',data)

def reset_password(request):
    return render(request,'reset_password.html')

def otp(request):
    if request.method == "POST":
        phone = request.GET.get('phone')
        otp = request.POST.get('otp')
        print(phone)
        print(otp)

        #Validate otp to authenticate the user
        validate_otp = Otps.objects.filter(phone_number=phone)
        for otps in validate_otp:
            if  str(otp) == str(otps.otp):
                if datetime.datetime.now().replace(tzinfo=utc) <= (otps.expire_at.replace(tzinfo=utc)):
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
    return render(request,'parent/dashboard.html')

