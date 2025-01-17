from . import views
from django.urls import path
urlpatterns = [
    path('send-email',views.send_emails,name='send_email'),
    path('track/dashboard',views.tracking_dash,name='tracking_dash'),
    path('track/stats/<int:pk>/',views.email_statics,name='email_statics'),
    path('track/click/<unique_id>/',views.track_click,name='track_click'),
    path('track/open/<unique_id>/',views.track_open,name='track_open'),
]
