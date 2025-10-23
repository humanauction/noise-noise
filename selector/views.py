from django.views.generic import TemplateView
from django.shortcuts import render

# Create your views here.


class HomePage(TemplateView):
    """Home page view."""
    template_name = 'selector/index.html'


class SelectorView(TemplateView):
    """Selector page view."""
    template_name = 'selector/selector.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['colors'] = [
            'white', 'pink', 'red', 'blue',
            'purple', 'yellow', 'brown', 'green'
        ]
        return context


def mixer_view(request):
    """Mixer page view."""
    tracks = [
        {'id': 'white', 'name': 'White Noise'},
        {'id': 'pink', 'name': 'Pink Noise'},
        {'id': 'brown', 'name': 'Brown Noise'},
        {'id': 'blue', 'name': 'Blue Noise'},
        {'id': 'purple', 'name': 'Purple Noise'},
    ]
    return render(request, 'selector/mixer.html', {'tracks': tracks})
