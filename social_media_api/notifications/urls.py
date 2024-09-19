from django.urls import path
from .views import NotificationListView

urlpatterns = [
    path('notifications/', NotificationListView.as_view(), name='notification-list'),
]

from django.urls import include, path

urlpatterns = [
    ...
    path('notifications/', include('notifications.urls')),
    ...
]
