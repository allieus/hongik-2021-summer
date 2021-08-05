from django.core.validators import MinLengthValidator
from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100, db_index=True,
                            validators=[MinLengthValidator(3)])
    desc = models.TextField()
    photo = models.ImageField(blank=True)
    price = models.PositiveIntegerField()
    is_public = models.BooleanField(default=False, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
