from django import forms
from to_do_app.models import TaskModel

# form are working
class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = ["taskTitle", "taskDescription"]
        widgets = {
            "taskTitle": forms.TextInput(
                attrs={
                    "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:border-2 focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 mb-2.5"
                }
            ),
            "taskDescription": forms.TextInput(
                attrs={
                    "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:border-2 focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 mb-2.5"
                }
            ),
        }
