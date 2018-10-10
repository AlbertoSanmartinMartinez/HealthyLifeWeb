from django.db.models.signals import post_save
from django.dispatch import receiver
from healthylifeapp import models
from django.core.mail import send_mail

@receiver(post_save, sender=models.Post)
def createPost(sender, **kwargs):
    pass


"""
@receiver(post_save, sender=models.Comment):
def notifyNewComment(sender, instance, created, **kwargs):
    if created:
        user = instance.author_id
        send_mail("Nuevo comentario", email_from, email_to, email_message, fail_silently=True)
"""
