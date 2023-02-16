from django.forms import ModelForm
from django import forms
from .models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
        labels = {
            "fname": "First Name",
            "lname": "Last Name",
        }

    message = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields["role"].required = False
        self.fields["company"].required = False
