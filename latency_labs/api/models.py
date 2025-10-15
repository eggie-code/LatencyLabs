from django.db import models
from django.contrib.auth.models import AbstractUser
from latency_labs import models

# user model definition


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

# alerting system


class Alert(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    metric_name = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    alert_name = models.CharField(max_length=100)
    message = models.TextField()
    triggered_at = models.DateTimeField(auto_now_add=True)


class UserDevice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)

# device grouping


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


class DeviceGroup(models.Model):
    name = models.CharFiels(max_length=100)
    devices = models.ManyToManyField(Device)
