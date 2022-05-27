# import package
import datetime
import os
import africastalking


# Initialize SDK
username = "gasspoint"    # use 'sandbox' for development in the test environment
api_key = "a11bc7cad147f2b7483347623541a9f2d344ea6d32fc29cc37db05dd15a04d64"      # use your sandbox app API key for development in the test environment
africastalking.initialize(username, api_key)
sms = africastalking.SMS


def ussd_sms_response(phone,response):
    return sms.send(response,[phone])

def send_otp_to_validate_phone(phone,message):
    return sms.send(message,[phone])

def send_transaction_message_response_to_sender_phone(
                  transaction_id,
                  phone_number,
                  sender_name,
                  reciever_name,
                  amount,
                  date,
                  time,
                  balance):
    return sms.send(transaction_id +" Hello "+sender_name+", Confirmed Ksh"+str(amount)+".00 sent to "+reciever_name+"'s Account on "+date+" at "+time+". New PTC Account balance is Ksh"+str(balance)+".00. Transaction cost of Ksh0.00. Thanks for using Parent To Child Transaction management system. #DEVELOPER FELIX @safaricom Automation", [phone_number])

def send_transaction_message_response_to_reciever_phone(
            transaction_id,
            phone_number,
            sender_name,
            reciever_name,
            amount,
            date,
            time,
            balance):
    return sms.send(" Hello "+reciever_name+", Confirmed you have recieved Ksh"+str(amount)+".00 from "+sender_name+"'s Account on "" at "+str(balance)+".New PTC Account balance is Ksh"".00. #DEVELOPER FELIX @safaricom Automation ", [phone_number])

def send_withdrawal_message_response_to_withrawer_phone(
            transaction_id,
            phone_number,
            withdrawer_name,
            amount,
            account_balance,
            date,
            time,
            balance):
    return sms.send()

def child_password_and_phone_number_send_to_phone(
                                   phone,
                                   name,
                                   password
                                  ):
    return sms.send("Hello "+name+ ", Your password is "+str(password)+". Welcome to PTC app, to install click https://github.com/Developer-Felix/ForthYeahFinalProject/blob/main/APK/ptc_manager.apk view then install. Thank You",[phone])

            
def send_otp_to_validate_phone(phone,otp):
    return sms.send("Your OTP is "+str(otp)+".",[phone])


# try:
#     f = open(settings.MEDIA_ROOT + f"/africastalking/sms_consoles/{datetime.now().strftime('%Y%m%d')}_stks.txt", 'a')
# except Exception as e:
#     try:
#         os.mkdir(os.path.join(settings.MEDIA_ROOT, 'africastalking/'))
#     except Exception as e:
#         os.mkdir(os.path.join(settings.MEDIA_ROOT, 'africastalking/sms_consoles/'))
#     f = open(settings.MEDIA_ROOT + f"/africastalking/sms_consoles/{datetime.now().strftime('%Y%m%d')}_stks.txt", 'a')
# f.write(str(response) + "\n")