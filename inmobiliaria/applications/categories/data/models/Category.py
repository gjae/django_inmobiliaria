from django.db import models
from model_utils.models import SoftDeletableModel, TimeStampedModel

class Category(SoftDeletableModel, TimeStampedModel):
    
    name = models.CharField(
        max_length=40)
    description = models.TextField(
        null=True, blank=True)
    hight_level_cat = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.name
