from django.shortcuts import render,redirect
from todo_list.models import Todo
from todo_list.forms import TodoForm
#in order to make sure that addTodo view is dealt only in case of post method we do this
from django.views.decorators.http import require_POST
# Create your views here.
def index(request):
    form=TodoForm()
    obj=Todo.objects.order_by('id')
    context={
    'object':obj,
    'form':form
    }
    return render(request,"todo_list/index.html",context)
@require_POST
def addTodo(request):
    form=TodoForm(request.POST)
    if(form.is_valid()):
        #form.save()
        new_todo = Todo(text=request.POST['text'])
        new_todo.save()
    return redirect('index')#no need to put .html
def completeTodo(request,todo_id):
    todo=Todo.objects.get(pk=todo_id)#or id=item_id
    todo.complete=True
    todo.save()
    return redirect('index')
def deleteCompleted(request):
    Todo.objects.filter(complete__exact=True).delete()
    return redirect('index')
def deleteAll(request):
    Todo.objects.all().delete()
    return redirect('index')
