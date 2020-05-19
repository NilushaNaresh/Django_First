from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from .models import ToDoItem
from django.forms import modelform_factory

#def welcome(request):
#    return HttpResponse("Hello!!!Welcome to my first project")


def welcome(request):
    all_todoitems=ToDoItem.objects.all()
    return render(request,'To_Do/base.html',{ 'items' : all_todoitems})


#def add_item(request):
#    a=request.POST['content']
#    new_item1=ToDoItem(content=a)
#   new_item1.save()
#    return render(request,'To_Do/base.html')
new_item=modelform_factory(ToDoItem,exclude=[])


def add_item(request):
    if request.method=="POST":
        form=new_item(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('welcome')
    else:
        form=new_item()
    return render(request,'To_Do/base.html',{'form':form})


def delete_item(request,todo_id):
    item_to_delete=ToDoItem.objects.get(id=todo_id)
    item_to_delete.delete()
    return render(request,'To_Do/base.html')