from django.views.generic import TemplateView, ListView

from .models import Author

class IndexPage(ListView):
    model = Author
    template_name = 'authors/index.html'
    context_object_name = 'authors'

class CreatePage(TemplateView):
    template_name = 'authors/create-page.html'
    def get_context_data(self, **kwargs):
        data = super().get_context_data()
        return data

# Create your views here.
