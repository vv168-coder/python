
from django import forms



class AddCommentForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea)
    score = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
