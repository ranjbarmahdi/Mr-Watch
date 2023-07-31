from django import forms
from .models import *


# =======================================<< Ticket Form >>=======================================
class TicketForm(forms.Form):
    SUBJECT_CHOICES = (
        ('پیشنهاد', 'پیشنهاد'),
        ('انتقاد', 'انتقاد'),
        ('گزارش', 'گزارش'),
    )
    name = forms.CharField(max_length=250, required=True)
    email = forms.EmailField()
    subject = forms.ChoiceField(choices=SUBJECT_CHOICES)
    message = forms.CharField(widget=forms.Textarea, required=True)


# =======================================<< Comment Form >>=======================================
class CommentForm(forms.ModelForm):
    # name = forms.CharField(max_length=250)
    # email = forms.EmailField()
    # body = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']
