from django.views.generic import TemplateView


# Create your views here.
class HomePage(TemplateView):
    """Home page view."""
    template_name = 'index.html'
