from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('polttopallo/', views.polttopallo, name='polttopallo'),
]
