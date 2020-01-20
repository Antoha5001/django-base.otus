from random import randint
from datetime import date, datetime, timedelta
from django.views.generic import TemplateView

from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from datetime import datetime
from django.http import HttpResponse

def today(count=20):
    days = []
    today = datetime.today() - timedelta(days=8)
    for i in range(count):
        print(i)
        day = today - timedelta(days=i)
        # print(day)
        for j in range(randint(2, 5)):
            print(str(i) + '-' + str(j))
            days.append(day.replace(hour=randint(0, 23)))
    return days
    # print(len(days))

class HomeView(TemplateView):
    template_name = 'homepage/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, template_name=self.template_name)

class ArticleView(TemplateView):
    template_name = 'homepage/articles.html'

    def get(self, request, *args, **kwargs):
        myclass = MyClass()
        myclass.data = {
            'datakey': 'datavalue'
        }
        myclass.list = list(range(4, 8))
        args = {
            'articles': list(range(1, 4)),
            'title0': '',
            'title1': '<h3>title h3 1</h3>',
            'title2': '<h4>title h4 2</h4>',
            'myclass': myclass,
            'dates_my': today()
        }
        today()
        response = render(request, self.template_name, args)
        return response


def article_view_year(request, year):
    return HttpResponse(f'<h1>{year}</h1>')


class MyClass():
    foo = "foooooo"
    barr = 'baaaarr'
    def __repr__(self):
        return self.foo