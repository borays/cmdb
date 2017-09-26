from django.shortcuts import render

# Create your views here.

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('yto_cmdb:index'))

def register(request):
    if request.method!='POST':
        form=UserCreationForm()
    else:
        form=UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user=form.save()
            authenticated_user=authenticate(username=new_user.username,password=request.POST['password1'])
            login(request,authenticated_user)
            return HttpResponseRedirect(reverse('yto_cmdb:index'))

    content={'form':form}
    return render(request,'users/register.html',content)

def change_pass(request):
    if request.method!='POST':
        form=PasswordChangeForm(request.user.username)
    else:
        form=PasswordChangeForm(data=request.POST)

        if form.is_valid():
            new_user=form.save()
            logout(request)
            return HttpResponseRedirect(reverse('yto_cmdb:index'))
    content={'form':form}
    return render(request, 'users/change_pass.html', content)