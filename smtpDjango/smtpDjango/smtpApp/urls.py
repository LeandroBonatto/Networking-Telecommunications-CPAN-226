from django.urls import path, include
from .views import send_email_view

urlpatterns = [
    path('', send_email_view, name='home'),
    path('send-email/', send_email_view, name='send-email'),
]

