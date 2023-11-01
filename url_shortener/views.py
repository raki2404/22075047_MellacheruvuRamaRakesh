from django.shortcuts import render,redirect
from .models import Shortened_Url
import random,string

def home(request):
    if request.method=='POST':
        long_url=request.POST.get('long_url')
        short_url=''.join(random.choice(string.ascii_letters) for i in range(10))
        Shortened_Url.objects.create(long_url=long_url,short_code=short_url)
    
    shortened_urls=Shortened_Url.objects.all()
    return render(request,'home.html',{'shortened_urls':shortened_urls})

def redirectPage(request,short_url):
    Url=Shortened_Url.objects.get(short_code=short_url)
    return redirect(Url.long_url)



