from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

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
            return redirect('')

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
            return redirect('otp/')

        except:
            return redirect('register/')
        print("Done")

        print(username)

        print(phone)

    return render(request,'parent/registration.html',data)

def reset_password(request):
    return render(request,'reset_password.html')

def otp(request):
    return render(request,'parent/otp.html')

def child_dashboard(request):
    return render(request,'child/dashboard.html')

def parent_dashboard(request):
    return render(request,'parent/dashboard.html')

