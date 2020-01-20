from django.urls import path

from . import views

app_name = 'authors'

urlpatterns = [
    path('', views.IndexPage.as_view(), name='authors')
]