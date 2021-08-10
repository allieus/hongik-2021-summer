from django import forms

from movist.models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["message"]
