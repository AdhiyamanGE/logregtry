from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegisterForm
# Create your views here.
def home(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=UserRegisterForm()
    return render(request,'app_logreg/nono.html',{'form':form})