from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone


@shared_task
def add(x, y):
    from time import sleep

    sleep(15)
    print(f"args {x} and {y}")
    return x + y


# 1. Задача для запуска через .delay()
@shared_task
def generate_number():
    import random

    number = random.randint(1, 1000)
    print(f"Сгенерировано число: {number}")
    return number


# 2. Задача для запуска по расписанию через crontab
@shared_task
def daily_task():
    print(f"Ежедневная задача выполнена: {timezone.now()}")
    return "Ежедневная задача выполнена"


# 3. Задача отправки письма через SMTP
@shared_task
def send_example_email(email):
    send_mail(
        subject="Письмо от Celery",
        message="Привет! Это тестовое письмо, отправленное через Celery.",
        from_email=None,
        recipient_list=[email],
        fail_silently=False,
    )
    return "Письмо отправлено"