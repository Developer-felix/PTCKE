# from http.client import HttpResponse
from email import message
from http.client import HTTPResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import datetime

from users.models import Account


@csrf_exempt
def ussd_callback(request):
    if request.method == "POST":

        global response
        session_id = request.POST["sessionId"]
        service_code = request.POST["serviceCode"]
        phone_number = request.POST["phoneNumber"]
        text = request.POST["text"] 

        sms_phone_number = []
        sms_phone_number.append(phone_number)

        # #checking the service provider
        # import phonenumbers
        # from phonenumbers import geocoder
        # pepnumber = phonenumbers.parse(phone_number)
        # location = geocoder.description_for_number(pepnumber,"en")
        # print("Country :",location)
        # from phonenumbers import carrier
        # service_pro = phonenumbers.parse(phone_number)
        # severvice = carrier.name_for_number(service_pro,"en")
        # print("Service Provider : ",severvice)

        #Split Child and Parent
        users = Account.objects.all()
        for user in users:
            if user.phone_number == phone_number:
                if user.is_parent == True:
                    """
                    Parent logic Goes here
                    """
                    if text == "":
                        def parent_menu():
                            #PARENT MAIN MENU
                            response = "CON What would you like to do? \n"
                            response += "1. check Acount details\n"
                            response += "2. Check phone number"
                            response += "3. Check balance"
                            response += "4. Send money "
                            response += "5. Add Child"
                            return HttpResponse(response)
                        parent_menu()
                    return None
                if user.is_child == True:
                    """
                    Parent logic Goes here
                    """
                    if text == "":
                        def parent_menu():
                            #PARENT MAIN MENU
                            response = "CON What would you like to do? \n"
                            response += "1. check Acount details\n"
                            response += "2. Check phone number"
                            response += "3. Check balance"
                            response += "4. Withdraw Cash "
                            response += "5. Request Cash"
                            return HttpResponse(response)
                        parent_menu()
                    return None
    
    else:
        return HttpResponse("Using a wrong request.... Try using POST")

            

        




























    #     #ussd logic
    #     if text == "":
    #         # #Checking the service provider.
    #         # if severvice != "Safaricom":
    #         #     response = "END Inverlid service provider {}. Try with Safaricom Contact."
    #         #     return Response(response)

            
        
        
    #     elif text == "1":
    #         #SUB MENU 1
    #         response = "CON What would you like to check on your account? \n"
    #         response += "1. Account number"
    #         response += "2. Account balance"
    #         return HttpResponse(response)
        
    #     elif text == "1*1":
    #         #SUB MENU 1
    #         response = "END Your account number is: {}".format(phone_number)
    #         return HttpResponse(response)

    #     elif text == "2":
    #         response = "END Your phone number is {}".format(phone_number)
    #         return HttpResponse(response)
        
        
    #     elif text == "3":
    #         BALANCE = Wallet.objects.filter(account_phone_number=phone_number)
    #         for B in BALANCE:
    #             response = "END Your account balance is Sh.{}".format(B.account_balance)
    #             return HttpResponse(response)
        
    #             # ussd_sms_response(phone=phone_number,response=response)

    #     elif text == "4":
    #         response = "CON Enter the account number you want to send money to ? \n"
    #         return HttpResponse(response)
        

    #     elif text == "5":
    #         response = "CON Enter the name of child? \n"
    #         return HttpResponse(response)

    #     elif text == "1*2":
    #         response = "CON Account balance : 1000"
    #         return HTTPResponse(response)
        
    #     else:
    #         response = "END Invalid input. Try again"
    #         return HttpResponse(response)

    # else:
    #     return HttpResponse("Using a wrong request.... Try using POST")
    
        

        




    
