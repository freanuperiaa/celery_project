from django.urls import path

from .views import *


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('success/', SuccessQueueTaskView.as_view(), name='success'),
]
