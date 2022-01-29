from django import forms
from django.db.models import fields
from . models import UserBase
from django.contrib.auth.forms import (AuthenticationForm, PasswordResetForm, SetPasswordForm)


class UserLoginForm(AuthenticationForm):

    username =forms.CharField(label='اسم المستخدم او الايميل' , widget=forms.TextInput(attrs={'class':'form-control mb-3', 'placeholder': 'اسم المستخدم', 'id': 'login-username'}))

    password =forms.CharField(label='كلمه السر' , widget=forms.PasswordInput(attrs={'class':'form-control ', 'placeholder': 'كلمة السر', 'id':'login-pwd'}))


        

       


        

class RegistrtaionForm(forms.ModelForm):
    first_name = forms.CharField(label=' اسمك  الكامل', max_length=50 , min_length=4 ,help_text='Required')
    user_name = forms.CharField(label='ادخل اسم المستخدم', max_length=50 , min_length=4 ,help_text='Required')
    email =  forms.EmailField(label='ادخل الايميل', max_length=100, help_text='Required', error_messages={'required': 'sorry you need an email'})
    password =  forms.CharField(label='كلمه السر', widget=forms.PasswordInput)
    password2 =  forms.CharField(label='اعد كلمة السر', widget=forms.PasswordInput)
    

    class Meta:
        model = UserBase
        fields = ('user_name', 'email',)

    def clean_username(self):
        user_name = self.cleaned_data['user_name'].lower()
        r = UserBase.objects.filter(user_name=user_name)
        if r.count():
            raise forms.ValidationError('اسم المستخدم موجود ')
        return user_name

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('كلمة السر غير مطابقه')
        return cd['password2']
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if UserBase.objects.filter(email=email).exists():
            raise forms.ValidationError('من فضلك استخدم ايميل اخر')
        return email

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'اسم اسمك بالكامل'}
        )
        self.fields['user_name'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'اسم المستخدم'}
        )
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'ايميل ', 'name':'email'}
        )
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'كلمة السر '}
        )
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': ' اعد كلمة السر '}
        )

class UserEditForm(forms.ModelForm):
    
    email = forms.EmailField(
        label='ايميلك  (لا يمكن تغيره)', max_length=200, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'الايميل', 'id': 'form-email', 'readonly': 'readonly'}))

    user_name = forms.CharField(
        label='اسم المستخدم', min_length=4, max_length=50, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'اسم المستخدم', 'id': 'form-firstname', 'readonly': 'readonly'}))

    first_name = forms.CharField(
        label='اسمك الاول', min_length=4, max_length=50, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'اسمك الاول', 'id': 'form-lastname'}))

    phone_number = forms.CharField(label='رقم الهاتف', min_length=4, max_length=50, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'رقم الهاتف', 'id': 'form-phone'}))
    class Meta:
        model = UserBase
        fields = ('email', 'user_name', 'first_name',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_name'].required = True
        self.fields['email'].required = True

    
class PwdResetForm(PasswordResetForm):
    email = forms.CharField(label='ادخل الايميل' , max_length=254 , widget=forms.TextInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'الايميل', 'id':'form-email'}
    ))
    def clean_email(self):
        email = self.cleaned_data['email']
        u = UserBase.objects.filter(email=email)
        if not u:
            raise forms.MultiValueField('عفوا , هذا الايميل غير موجود')
        return email
    
    
class PwdResetConfirmForm(SetPasswordForm):
     new_password1 = forms.CharField(
        label='كلمة السر الجديده', widget=forms.PasswordInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'كلمة السر الجديده', 'id': 'form-newpass'}))
     new_password2 = forms.CharField(
        label='كرر كلمه السر ', widget=forms.PasswordInput(
            attrs={'class': 'form-control mb-3', 'placeholder': ' كلمة السر الجديده', 'id': 'form-new-pass2'}))