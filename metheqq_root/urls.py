from django.contrib.auth import views as auth_views
from unicodedata import name
from django.views.generic import TemplateView
from django.urls import path, include
from .froms import (UserLoginForm, PwdResetForm ,PwdResetConfirmForm)
from .  import views


app_name = 'metheqq_root'

urlpatterns = [
    path('', views.campany),
    path('login/', auth_views.LoginView.as_view(template_name='metheqq_root/registration/login.html', form_class=UserLoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/account/login/'), name='logout'),
    path('cheekpage/', views.Cheekpage ,name='cheekpage'),
    path('cheek/', views.Cheek , name='cheek'),
    path('packects/', views.packects, name='packects'),
    path('register/', views.account_register , name='register'),
    path('activate/<slug:uidb64>/<slug:token>)/', views.account_activate, name='activate'),
    path('pay/', views.pay_pakect , name='pay'),
    path('pay2/', views.pay_pakect2 , name='pay2'),
    path('dashboard/', views.dashboard , name='dashboard'),
    path('profile/edit/', views.edit_details , name='edit_details'),
    path('profile/delete_user/', views.delete_user , name='delete_user'),
    path('profile/delete_confirm/', TemplateView.as_view(template_name="metheqq_root/user/delete_confirm.html"), name='delete_confirmation'),
]

