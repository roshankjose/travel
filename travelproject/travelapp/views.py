from django.http import HttpResponse
from django.shortcuts import render
from .models import Place, People


# Create your views here.
class Peoples:
    pass


def demo(request):
    obj=Place.objects.all()
    peo=People.objects.all()
    return render(request,'index.html',{'result':obj,'results':peo})
# orm object oriented programming(its is rich with libraies to store and fetch data)
# def desc(request):
#     obj1=desc.objects.all()
#     return render(request,'index.html',{'results':obj1})
def register():
    return None