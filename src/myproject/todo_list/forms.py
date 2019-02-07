from django import forms
from todo_list.models import Todo
class TodoForm(forms.ModelForm):
    text=forms.CharField(max_length=50,widget=forms.TextInput(attrs={
    'placeholder':'Your todo item'
    }))
    class Meta:
        model=Todo
        fields=[
        'text'
        ]
