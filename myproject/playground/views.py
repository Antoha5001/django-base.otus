from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Articles, Publisher

class PlaygroundView(TemplateView):
    template_name = 'playground/home.html'
    #
    # def get(self, request, *args, **kwargs):
    #     articles = Articles.objects.all()
    #     for article in articles:
    #         print(article.publisher)
    #     args = {
    #         'articles': articles
    #     }
    #     return render(request, self.template_name, args)

    def get_context_data(self, **kwargs):
        request = super().get_context_data(**kwargs)
        request['articles'] = Articles.objects.all()
        return request


# Create your views here.
