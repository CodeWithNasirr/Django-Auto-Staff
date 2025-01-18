from django.urls import path
from .views import fronted_look

urlpatterns = [
    path('',fronted_look,name='fronted_looks'),
]