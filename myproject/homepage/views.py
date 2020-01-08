from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse

require_http_methods(['POST', 'GET'])
def home_view(request):
    # response = HttpResponse("Hello")
    # response['My-Custom-Header'] = 'meat-and-eggs'
    if request.method == 'GET':
        print('This is GET')
    response = render(request, 'homepage/index.html')
    return response
# Create your views here.
def article_view(request):

    args = {
        'articles': list(range(1, 4)),
        'title0': '',
        'title1': '<h3>title h3 1</h3>',
        'title2': '<h4>title h4 2</h4>'
    }

    response = render(request, 'homepage/articles.html', args)
    return response