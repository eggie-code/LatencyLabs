from django.shortcuts import render
from rest_framework import generics
from .models import Device, Metric, Alert, UserDevice
from .serializers import DeviceSerializer, MetricSerializer, AlertSerializer, UserDeviceSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
import matplotlib.pyplot as plt
from io import BytesIO
import base64


class DeviceList(generics.ListCreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


class DeviceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


class MetricList(generics.ListAPIView):
    queryset = Metric.objects.all()
    serializer_class = MetricSerializer


class MetricDetail(generics.RetrieveAPIView):
    queryset = Metric.objects.all()
    serializer_class = MetricSerializer

    def perform_create(self, serializer):
        metric = serializer.save()
        if metric.value > 80:  # Threshold
            Alert.objects.create(
                device=metric.device, alert_name='High CPU usage', message='CPU usage is high')


class AlertList(generics.ListAPIView):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer


class AlertDetail(generics.RetrieveAPIView):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer


class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(
            raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
        })


class MetricChartView(generics.RetrieveAPIView):
    queryset = Metric.objects.all()
    serializer_class = MetricSerializer

    def get(self, request, *args, **kwargs):
        metric = self.get_object()
        # Generate chart
        plt.plot(metric.values)
        plt.xlabel('Time')
        plt.ylabel('Value')
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_png = buffer.getvalue()
        buffer.close()
        return Response({'image': base64.b64encode(image_png).decode('utf-8')})
