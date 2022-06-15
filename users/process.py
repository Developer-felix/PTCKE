from datetime import datetime

current_time = datetime.now()

print(current_time)

user = "Account".objects.filter(user_id=5)

def process(user_id):
    print("Done")

process(user_id=user)
