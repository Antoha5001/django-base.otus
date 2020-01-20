from django.urls import path, register_converter
from django.views.generic.base import TemplateView

from .views import article_view, article_view_year, HomeView, ArticleView

app_name = "homepage"

class YearConverter():
    regex = r'[0-9]{4}'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return '%04d' % value

register_converter(YearConverter, 'year')

urlpatterns = [
    path('', TemplateView.as_view(template_name='homepage/index.html'), name="index"),
    path('articles/', ArticleView.as_view(), name="articles"),
    path('articles/<year:year>/', article_view_year, name='articles_year')
    # re_path(r'^articles/(?P<year>[0-9]{4})/$', article_view_year, name='articles_year')
]