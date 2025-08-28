from django.views.generic import TemplateView
from django.shortcuts import render


# Create your views here.
class HomePage(TemplateView):
    """Home page view."""
    template_name = 'index.html'


def index(request):
    colors = [
        'white', 'pink', 'red', 'blue',
        'purple', 'yellow', 'brown', 'green'
    ]
    return render(request, 'selector.html', {'colors': colors})
