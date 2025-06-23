from django import forms
from .models import Task, Tag

class TaskForm(forms.ModelForm):
    deadline = forms.DateTimeField(
        required=False,
        widget=forms.DateTimeInput(
            attrs={"class": "form-control", "type": "datetime-local"}
        )
    )
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Task
        fields = "__all__"