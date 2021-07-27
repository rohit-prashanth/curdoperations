from django.shortcuts import render
from .forms import curdforms
from .models import Curdoperations
from django.http import HttpResponseRedirect

# Create your views here.
def curdop(request):
    if request.method == 'POST':
        fm = curdforms(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm = curdforms()
    data = Curdoperations.objects.all()
    return render(request,'curd.html',{'form':fm , 'data':data})

def delete_data(request,id):
    if request.method == "POST":
        row = Curdoperations.object.get(pk=id)
        row.delete()
        return HttpResponseRedirect('/')