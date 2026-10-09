from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail


@shared_task
def send_otp_mail(email, code):
    send_mail(
        subject="Registration code",
        message=f"your code {code}",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email],
    )


# @shared_task
# def send_report_mail():
#     send_mail(
#         subject="Report daily",
#         message="..................................",
#         from_email=settings.EMAIL_HOST_USER,
#         recipient_list=["riszav.01@gmail.com"],
#     )