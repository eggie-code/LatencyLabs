from django.urls import path
from . import views

urlpatterns = [
    path('devices/', views.DeviceList.as_view()),
    path('devices/<int:pk>/', views.DeviceDetail.as_view()),
    path('metrics/', views.MetricList.as_view()),
    path('metrics/<int:pk>/', views.MetricDetail.as_view()),
    path('alerts/', views.AlertList.as_view()),
    path('alerts/<int:pk>/', views.AlertDetail.as_view()),
    path('users/<int:user_id>/devices/', views.UserDeviceList.as_view()),
    path('login/', views.LoginView.as_view()),

]
