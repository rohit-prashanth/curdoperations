from django.shortcuts import render
from .forms import curdforms
from .models import Curdoperations
from django.http import HttpResponseRedirect
from django.contrib import messages

# Create your views here.
def curdop(request):
    if request.method == 'POST':
        fm = curdforms(request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/')
    else:
        fm = curdforms()
        data = Curdoperations.objects.all()
        return render(request,'curd.html',{'form':fm , 'data':data})

def delete_data(request,id):
    if request.method == "POST":
        row = Curdoperations.objects.get(pk=id)
        row.delete()
        return HttpResponseRedirect('/')

def update_data(request,id):
    if request.method == 'POST':
        data = Curdoperations.objects.get(pk=id)
        form = curdforms(request.POST, instance=data)
        form.save()
        messages.info(request,'Updated Successfully')
        return HttpResponseRedirect('/')
    else:
        data = Curdoperations.objects.get(pk=id)
        form = curdforms(instance=data)
        return render(request,'update.html',{'form':form})