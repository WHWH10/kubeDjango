from django import forms
from django.contrib.auth.hashers import check_password
from .models import AdUser

class LoginForm(forms.Form):
    user_id = forms.CharField(
        error_messages={
            'required' : '아이디를 입력해주세요'
        }, label = '아이디'
    )
    user_password = forms.CharField(
        error_messages={
            'required' : '비밀번호를 입력해주세요'
        }, widget = forms.PasswordInput, label = '비밀번호'
    )

    def clean(self):
        cleaned_data = super().clean()
        user_id = cleaned_data.get('user_id')
        user_password = cleaned_data.get('user_password')

        if user_id and user_password:
            try:
                aduser = AdUser.objects.get(user_id = user_id)
            except AdUser.DoesNotExist:
                self.add_error('user_id', '아이디가 없습니다.')
                return
            
            # if not check_password(user_password, aduser.user_password):
            #     self.add_error('user_password', '비밀번호를 틀렸습니다.')