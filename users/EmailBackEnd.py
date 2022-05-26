
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password 
from django.contrib.auth.backends import ModelBackend

class EmailBackEnd(ModelBackend):
    # def authenticate(self,request, username=None, password=None, **kwargs): solved this error by removing the self as bellow
    def authenticate(request, phone_number=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.filter( phone_number=phone_number)
        
            if user.exists():
                user = user.first()
                if check_password(password, user.password):
                    return user
        
        except UserModel.DoesNotExist:
            return None
        
        return None
        

