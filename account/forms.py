from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class SignupForm(UserCreationForm):
    class Meta:
        model=CustomUser
        fields=['username','password1','password2','email','address']
        labels = {
            'username' : '아이디',
            'password1' : '패스워드',
            'password2' : '패스워드2',
            'email' : '이메일',
            'address':'주소',
        }
