# import package
import africastalking

# Initialize SDK
username = "gasspoint"    # use 'sandbox' for development in the test environment
api_key = "a11bc7cad147f2b7483347623541a9f2d344ea6d32fc29cc37db05dd15a04d64"      # use your sandbox app API key for development in the test environment
africastalking.initialize(username, api_key)

# Initialize a service e.g. SMS
sms = africastalking.SMS


# Use the service synchronously
response = sms.send("Hello Message!", ["+254717713943"])
print(response)


