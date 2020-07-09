from django.shortcuts import render
from home.models import Parallex,Slider

# Create your views here.

def home(request):
    slide=Slider.objects.all()
    para=Parallex.objects.all()
    context={
        'slide':slide,
        'para':para
            }
    return render(request,'pages/home.html',context)