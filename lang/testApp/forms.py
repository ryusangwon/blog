from django import forms
from .models import User
from .validators import validate_test
from django.core.exceptions import ValidationError

class UserForm(forms.ModelForm):
    
    class Meta:
        model = User
        #fields = '__all__'
        fields = ['name', 'nation', 'age']
        widgets = {'name':forms.TextInput(attrs={'placeholder':'이름 입력'}),
                   'nation':forms.TextInput(attrs={'placeholder':'국적 입력'}),
                   'age':forms.TextInput(attrs={'placeholder':'나이 입력'})}
        
    def clean_name(self):
        name = self.cleaned_data['name']
        if '*' in name:
            raise ValidationError('*는 포함될 수 없음')
        return name