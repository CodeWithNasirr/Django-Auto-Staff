from . import views
from django.urls import path
urlpatterns = [
    path('send-email',views.send_emails,name='send_email'),
]