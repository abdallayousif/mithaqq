from queue import Empty
from turtle import update
from unicodedata import decimal
from django.shortcuts import render, get_object_or_404,redirect
from django.http.response import JsonResponse
from django.contrib.auth import login, logout
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.conf import settings
from django.http import HttpResponse
from .froms import RegistrtaionForm, UserEditForm
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

from acount.token import account_activation_token
from acount.models import UserBase
from .models import Campany,MangerWord,Marketers,MarketersComisions,Ecard
from acount import froms


# Create your views here.
def campany(request):
        companys = Campany.objects.all()
        mange = MangerWord.objects.all()
        contaxt = {
            'campany': companys,
            'mange': mange
        }
        return render(request, 'metheqq_root/index.html', contaxt)


def SenEmail(request):
    pass


@login_required
def Cheekpage(request):
    return render(request, 'metheqq_root/refrence/ref.html')



@login_required
def Cheek(request):
    if request.method == 'POST':
        ref_key = request.POST.get('ref')
        packects = request.POST.get('packects')
        packectssrt = request.POST.get('packectssrt')
        print(type(packects))
        print(ref_key)
        print(packectssrt)
        
        if Marketers.objects.filter(refrens=ref_key).exists:
            mark = get_object_or_404(Marketers,refrens=ref_key)
            print(mark)
            mard_id = mark.id
            print(mard_id)
            markcom = get_object_or_404(MarketersComisions,marketers=mard_id)
            print(markcom)
            markcom.comisions += ((float(packects) * 2 ) / 100)
            markcom.save()
            xxxx = mark.user 
            print(xxxx)
            data = { 
                    'is_taken': xxxx.first_name
                }
        else:
            print('sooory')
     
    return JsonResponse(data)



def packects(request):
    return render(request, 'metheqq_root/packects/page.html')



def account_register(request):
    if request.method == 'POST':
        registerfrom = RegistrtaionForm(request.POST)
        print(registerfrom)
        if registerfrom.is_valid():
            user = registerfrom.save(commit=False)
            user.first_name = registerfrom.cleaned_data['first_name']
            user.email = registerfrom.cleaned_data['email']
            user.set_password(registerfrom.cleaned_data['password'])
            user.is_active = False
            user.save()
            uaser = Marketers.objects.create(user=user,  is_tts=False, is_ts= False)
            MarketersComisions.objects.create(marketers=uaser, comisions=0)
            current_site = get_current_site(request)
            subject = 'Activate youer Account'
            message = render_to_string('metheqq_root/registration/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject=subject, message=message)
            return HttpResponse('تم التسجيل ب نجاح')
    else:
        registerfrom = RegistrtaionForm()

    return render(request, 'metheqq_root/registration/register.html', {'form': registerfrom})

def account_activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = UserBase.objects.get(pk=uid)
    except:
        pass
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user) 
        return redirect('metheqq_root:cheekpage')
    else:
        return render(request, 'account/registration/activation_invalid.html')

@login_required
def pay_pakect(request):
    return render (request, 'metheqq_root/pay/pay.html')

@login_required
def pay_pakect2(request):    
    if request.method == 'POST':
        code = request.POST.get('code')
        print(code)
        
        if Ecard.objects.filter(ecard=code).exists():
            code2 = get_object_or_404(Ecard, ecard=code, is_use=False)
            print(code2)
            code2.is_use = True
            code2.save()
           
            
    return JsonResponse({'code': 'sussus'})
    
@login_required
def dashboard(request):
    return render(request, 'metheqq_root/user/dashboard.html')


@login_required
def edit_details(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        if user_form.is_valid():
            user_form.save()
    else:
        user_form = UserEditForm(instance=request.user)

    return render(request, 'metheqq_root/user/edit_details.html', {'user_form': user_form})


@login_required
def delete_user(request):
    user = UserBase.objects.get(user_name=request.user)
    user.is_active = False
    user.save()
    logout(request)
    return redirect('metheqq_root:delete_confirmation')