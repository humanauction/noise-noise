from django.views.generic import TemplateView
from django.shortcuts import render
import os
from django.conf import settings


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
    # Get all .wav files from static/audio/
    audio_dir = os.path.join(settings.BASE_DIR, 'static', 'audio')
    audio_files = []
    if os.path.exists(audio_dir):
        audio_files = [f for f in os.listdir(audio_dir) if f.endswith('.wav')]
    # Create 6 tracks
    tracks = [
        {'id': i, 'name': f'track: {i}'} for i in range(1, 7)]

    return render(request, 'selector/mixer.html', {
        'tracks': tracks,
        'audio_files': audio_files
    })
