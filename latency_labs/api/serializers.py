from .serializers import DeviceSerializer, MetricSerializer, AlertSerializer, UserDeviceSerializer
from rest_framework import generics, serializers
from .models import Device, Metric, Alert, UserDevice


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ['id', 'name', 'ip_address']


class MetricSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metric
        fields = ['id', 'device', 'metric_name', 'value']


class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alert
        fields = ['id', 'device', 'alert_name', 'message']


class UserDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDevice
        fields = ['id', 'user', 'device']
