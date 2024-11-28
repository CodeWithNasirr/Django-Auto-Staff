from . import views
from django.urls import path
urlpatterns = [
    path('',views.Dashboard,name='Dash'),
    path('imports',views.imports,name='Import'),
    path('export',views.export,name='Export')
]
