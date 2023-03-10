from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def register(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('login')
    else:
        form=UserRegisterForm()
    return render(request,'app_logreg/register.html',{'form':form})

@login_required
def home(request):
    return HttpResponse("<h1>home</h1>")