"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from todo_list.views import index,addTodo,completeTodo,deleteCompleted,deleteAll
urlpatterns = [
    path('',index,name='index'),
    path('add',addTodo,name='add'),
    path('complete/<todo_id>',completeTodo,name='completed'),
    path('deletecomplete',deleteCompleted,name='deletecomplete'),
    path('deleteall',deleteAll,name='deleteall')
]
