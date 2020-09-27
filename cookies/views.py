from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import  Http404


from .models import Cookie

def home(request):
    cookies = Cookie.objects.all()
    return render(request, 'home.html', {
        'cookies': cookies,
    })

