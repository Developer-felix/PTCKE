from django.shortcuts import redirect, render
# from config.PTC_MPESA.lipa_na_mpesa_online import lipa_na_mpesa

from wallet.models import Wallet

# Create your views here.
def top_up(request):
    if request.method == "POST":
        ammount = request.POST.get("ammount")
        phone = request.POST.get("phone")

        # lipa_na_mpesa(phone_number=254713303092,ammount="1")

        print(ammount)
        def get_wallet_balance():
            wallet = Wallet.objects.filter(user_id=request.user.id)
            for wallet in wallet:
                wallet_balance =  wallet.account_balance
                return wallet_balance
        wallet_balance=get_wallet_balance()
        print(wallet_balance)
        updated_balance = int(wallet_balance) + int(ammount)

        Wallet.objects.filter(user_id=request.user.id).update(account_balance=updated_balance)

        #Succes Modals
        return redirect("success/?ammount="+ammount)
        
    return render(request,'parent/top_up.html')


def top_up_success(request):
    ammount = request.GET.get("ammount")
    print(ammount)
    def get_wallet_balance():
            wallet = Wallet.objects.filter(user_id=request.user.id)
            for wallet in wallet:
                wallet_balance =  wallet.account_balance
                return wallet_balance
    wallet_balance=get_wallet_balance()
    data = {
        "ammount" : ammount,
        "wallet_balance":wallet_balance
    }
    return render(request,'parent/top_up_success.html',data)