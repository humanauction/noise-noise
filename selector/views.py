from django.views.generic import TemplateView

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
