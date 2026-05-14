from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'is_completed']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the task name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter a description'}),
            'is_completed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'title': 'Name',
            'description': 'Description',
            'is_completed': 'Completed?',
        }
