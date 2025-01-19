from django.urls import path
from .views import image_compression

urlpatterns = [
    path("",image_compression,name="image_compressions")
    # path('',fronted_look,name='fronted_looks'),
]