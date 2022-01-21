from django import forms
from .models import User
from .validators import validate_test
from django.core.exceptions import ValidationError

class UserForm(forms.ModelForm):
    
    class Meta:
        model = User
        #fields = '__all__'
        fields = ['name', 'nation', 'age']
        widgets = {'name':forms.TextInput(attrs={'class':'name', 'placeholder':'이름을 입력하세요'}),
                   'nation':forms.Textarea(attrs={'국적을 입력하세요'}),
                   'age':forms.TextInput(attrs={'placeholder':'나이를 입력하세요'})}