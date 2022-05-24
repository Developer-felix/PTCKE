# import package
import africastalking

# Initialize SDK
username = "sandbox"    # use 'sandbox' for development in the test environment
api_key = "6e5801a97796f3718a57ab5dec8089a1f30b8da78d10fb694912f7cbfecfcb14"      # use your sandbox app API key for development in the test environment
africastalking.initialize(username, api_key)

# Initialize a service e.g. SMS
sms = africastalking.SMS


# Use the service synchronously
response = sms.send("Hello Message!", ["+254717713943"])
print(response)


