from aiohttp import Payload
from django.conf import settings
from pyfcm import FCMNotification

from notification.models import MobileNotification
from users.models import Account
# importing APNs
from apns import APNs, Payload

def send_new_message_push_notification(**kwargs):
    sender = Account.objects.get(id=kwargs.get("sender_id"))
    recipient = Account.objects.get(id=kwargs.get("recipient_id"))
    content = kwargs.get("content")
    notification = MobileNotification()
    notification.recipient = recipient
    notification.title = "New notification"
    sender_full_name = "{} {}".format(sender.first_name, 
                                      sender.last_name)
    message = '{} has sent you a message: "{}"'.format(sender_full_name, 
                                                       content)
    notification.message = message

    if recipient.has_android_device():
        data_payload = {
            "badge": recipient.unread_notifications_count(),
            "alert": notification.title,
            "notification_id": notification.pk,
            "body": notification.message,
        }
        fcm = FCMNotification(api_key=settings.FIREBASE_API_KEY)

        return fcm.notify_single_device(
            registration_id=str(recipient.device.token),
            badge=recipient.unread_notifications_count(),
            data_message=data_payload,
            message_body=content)

    elif recipient.has_ios_device():
        apns = APNs(use_sandbox=settings.APNS_USE_SANDBOX, 
                    cert_file=settings.APNS_CERT_PATH, 
                    enhanced=True)
        aps = {
            "badge": recipient.unread_notifications_count(),
            "alert": notification.message,
            "sound": "default"
        }
        data_payload = {
            "notification_id": notification.pk,
        }
        custom_payload = {
            "aps": aps,
            "payload": data_payload
        }
        payload = Payload(custom=custom_payload)
        return apns.gateway_server.send_notification(recipient.device.token, 
                                                     payload, 
                                                     identifier=notification.pk)