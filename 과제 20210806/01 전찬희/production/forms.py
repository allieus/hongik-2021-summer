from django import forms
from django.db import models
from django.db.models import fields
from production.models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["title", "message"]
