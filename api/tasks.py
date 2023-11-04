from celery import shared_task

from django.core.mail import send_mail


@shared_task
def send_email(email, blog):
    send_mail(
        subject=blog.title,
        from_email='from 127.0.0.1',
        recipient_list=[email],
        message=blog.description,
        fail_silently=True
    )
    return 'Done'
