from django.urls import path

from  .views import home_view, article_view

app_name = "homepage"

urlpatterns = [
    path('', home_view, name="index"),
    path('articles/', article_view, name="articles")
]