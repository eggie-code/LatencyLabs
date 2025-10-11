import os
from celery import Celery
from django.core.mail import send_mail
from .models import Device
# device monitoring task
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'network_monitor.settings')

app = Celery('network_monitor')
app.config_from_object('django.conf:settings', namespace='CELERY')


@app.task
def ping_devices():
    devices = Device.objects.all()
    for device in devices:
        # Ping device and check status
        # Trigger alert if device is down
        pass
