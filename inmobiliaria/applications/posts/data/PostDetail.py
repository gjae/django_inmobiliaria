from django.db import models
from model_utils.models import SoftDeletableModel, TimeStampedModel
from applications.posts.data.Post import Post
from applications.data.models import City

class PostDetail(SoftDeletableModel, TimeStampedModel):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='post_detail')
    address = models.TextField(
        'Dirección de la propiedad', blank=True, null=True)
    amount = models.DecimalField(
        'Costo de la propiedad', max_digits=6, decimal_places=2)
    lon = models.FloatField(
        'Longitud geografica', null=True)
    lat = models.FloatField(
        'Latitud geografica', null=True) 
    city = models.ForeignKey(
        City, on_delete=models.CASCADE, related_name='posts')

    
    def __str__(self):
        return 'Detalle'