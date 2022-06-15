from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save , post_save
from django.utils import timezone
from model_utils.models import TimeStampedModel
from users.models import Account

class MobileDevice(models.Model):
    participant = models.OneToOneField(Account, related_name='device', on_delete= models.CASCADE)
    platform = models.CharField(max_length=20, choices=(('iOS', 'iOS'), ('Android', 'Android'),))
    token = models.TextField()


class MobileNotification(TimeStampedModel):
    recipient = models.ForeignKey(Account, related_name='user_device_notifications', on_delete=models.CASCADE)
    title = models.CharField(max_length=512, null=True, blank=True)
    message = models.TextField()
    status = models.CharField(max_length=10, default='unread')


class InAppMessage(models.Model):
    sender = models.ForeignKey(Account, related_name='sent_messages', on_delete=models.CASCADE)
    recipient = models.ForeignKey(Account, related_name='received_messages', on_delete=models.CASCADE)
    content = models.CharField(max_length=512)

@receiver(post_save, sender=InAppMessage)
def send_new_message_notification(sender, **kwargs):
    message = kwargs['instance']
    send_new_message_push_notification(sender_id=message.sender.id,
                                       recipient_id=message.recipient.id,
                                       content=message.content)