import os
from django.conf import settings
from django.shortcuts import render
from django.db import models
from django_daraja.mpesa.core import MpesaClient
from requests.models import Response
from django.urls import reverse
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from .models import LNMOnline




@api_view(["POST"])
def LNMCallbackUrlView(request):
    # print(request.data)
    # # try:
    # #     f = open(settings.MEDIA_ROOT + f"/mpesa/mmpesa_consoles/{datetime.now().strftime('%Y%m%d')}_stks.txt", 'a')
    # # except Exception as e:
    # #     try:
    # #         os.mkdir(os.path.join(settings.MEDIA_ROOT, 'mpesa/'))
    # #     except Exception as e:
    # #         try:
    # #             os.mkdir(os.path.join(settings.MEDIA_ROOT, 'mpesa/mmpesa_consoles/'))
    # #         except:
    # #             pass
    # #     f = open(settings.MEDIA_ROOT + f"/mpesa/mmpesa_consoles/{datetime.now().strftime('%Y%m%d')}_stks.txt", 'a')
    # # f.write(str(request.data) + "\n")

    print(request.data)
    lnm = LNMOnline.objects.all()
    for l in lnm:
        print(l.Amount)
    
    if request.method == "POST":
        merchant_request_id = request.data['Body']['stkCallback']['MerchantRequestID']
        checkout_request_id = request.data['Body']['stkCallback']['CheckoutRequestID']
        result_code = request.data['Body']['stkCallback']['ResultCode']
        result_description = request.data['Body']['stkCallback']['ResultDesc']
        ammount  = request.data['Body']['stkCallback']['CallbackMetadata']['Item'][0]['Value']
        mpesa_receipt_number  = request.data['Body']['stkCallback']['CallbackMetadata']['Item'][1]['Value']
        balance  = ""
        transaction_date  = request.data['Body']['stkCallback']['CallbackMetadata']['Item'][3]['Value']
        phone_number  = request.data['Body']['stkCallback']['CallbackMetadata']['Item'][4]['Value']
        from datetime import datetime 
        str_transaction_date = str(transaction_date)
        transaction_datetime = datetime.strptime(str_transaction_date,"%Y%M%d%H%M%S")
        #Saving to database
        try: 
            lnmonline = LNMOnline.objects.create(
                CheckoutRequestID = checkout_request_id,
                MerchantRequestID = merchant_request_id,
                ResultCode = result_code,
                ResultDesc = result_description,
                MpesaReceiptNumber = mpesa_receipt_number,
                Amount = ammount,
                Balance = balance,
                TransactionDate = transaction_datetime,
                PhoneNumber = phone_number
            )
            lnmonline.save()
            print("Saved to database")
            

        
        except:
            return Response({"success": False,
                                             "errors": [{"Payment Error": "Cannot process payment Request"}],
                                             "status_code": 1, "status_message": "failed",
                                             "message": "Cannot process payment request",
                                             "data": None}, status=status.HTTP_400_BAD_REQUEST)
        return Response({
                            "success": True,
                            "errors": None,
                            "status_code": 0,
                            "status_message": "success",
                            "message": "successfully sent a payment request ",
                            'data': None, })
