from django.shortcuts import render, reverse, redirect
from django.views.generic import TemplateView, ListView

from .models import Author
from .forms import AuthorForms

class IndexPage(ListView):
    model = Author
    template_name = 'authors/index.html'
    context_object_name = 'authors'

class CreatePage(TemplateView):
    template_name = 'authors/create-page.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['form'] = AuthorForms()
        return data

    def post(self, request):
        form = AuthorForms(request.POST)
        if form.is_valid():
            new_author = form.save(commit=False)
            new_author.email = 'default@email.ru'
            new_author.save()
            return redirect(reverse('authors:authors'))
        return render(request, self.template_name, {'form' : form})



# Create your views here.
