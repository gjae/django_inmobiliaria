from django.db import models
from django.contrib.auth.models import User
from model_utils.models import SoftDeletableModel, TimeStampedModel
from applications.posts.data.Post import Post

class PostUserSubscription(SoftDeletableModel, TimeStampedModel):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='post_subscriptions')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='user_subscriptions')
    is_active = models.BooleanField('Recibir notificaciones', default=True)


    def __str__(self):
        return 'Recibe notificaciones' if self.is_active else 'No recibe notifiacciones'