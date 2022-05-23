from django.shortcuts import render

# Create your views here.
def top_up(request):
    if request.method == "POST":
        ammount = request.POST.get("ammount")
        phone = request.POST.get("phone")
        print(ammount)
    return render(request,'parent/top_up.html')