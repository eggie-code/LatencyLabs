from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Device(models.Model):
    name = models.CharField(max_length=100)
    ip_address = models.GenericIPAddressField()
    location = models.CharField(max_length=100)


class Metric(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    metric_name = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=10, decimal_places=2)


class Alert(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    metric_name = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=10, decimal_places=2)


class UserDevice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
