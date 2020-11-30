from django import forms
from .models import Tracking
from django.utils import timezone

# creating a form
class TrackingForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = Tracking
        # specify fields to be used
        fields = [
            "mood",
            "workDate",
        ]
