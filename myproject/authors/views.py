from django.views.generic import TemplateView, ListView

from .models import Author

class IndexPage(ListView):
    model = Author
    template_name = 'authors/index.html'
    context_object_name = 'authors'

# Create your views here.
