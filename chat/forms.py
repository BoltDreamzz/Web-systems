from django import forms
from .models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content']
        widget = {
            "content": forms.Textarea(attrs={
                "class": "form-control",
                "id": "messageForm",
            })
        }
