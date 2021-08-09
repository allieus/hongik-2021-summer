from django import forms

from movies.models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["messages"]
