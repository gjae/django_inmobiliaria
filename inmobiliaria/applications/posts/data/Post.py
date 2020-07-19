from django.db import models
from django.contrib.auth.models import User
from model_utils.models import SoftDeletableModel, TimeStampedModel
from applications.categories.models import Category
from applications.data.models import People

class Post(SoftDeletableModel, TimeStampedModel):
    BUSINESS_TYPE_CHOICE = [
        ('V', 'Venta'),
        ('R', 'Alquiler')
    ]

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE)
    title = models.CharField(
        max_length=60)
    is_aprobed = models.BooleanField(
        'Publicación aprobada', default=False)
    business_type = models.CharField(
        'Se encuentra en', 
        choices=BUSINESS_TYPE_CHOICE, 
        default='V',
        max_length=2)
    available = models.BooleanField(
        'Propiedad disponible', default=True)
    owner = models.ForeignKey(
        People, on_delete=models.CASCADE, related_name='owner_of_property')


    def __str__(self):
        return '{0} | {1}'.format(
            self.category,
            self.title
        )