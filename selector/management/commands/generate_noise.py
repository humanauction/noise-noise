from django.core.management.base import BaseCommand, CommandError
from selector.utils import save_noise


class Command(BaseCommand):
    help = 'Generate a colored noise .wav file'

    def add_arguments(self, parser):
        parser.add_argument(
            'color',
            type=str,
            help=(
                'Noise color (white, pink, red, blue, purple, yellow, '
                'brown, green)'
            )
        )
        parser.add_argument('filename', type=str, help='Output .wav file path')
        parser.add_argument(
            '--duration',
            type=float,
            default=10.0,
            help='Duration in seconds'
        )
        parser.add_argument(
            '--samplerate',
            type=int,
            default=44100,
            help='Sample rate'
        )

    def handle(self, *args, **options):
        color = options['color']
        filename = options['filename']
        duration = options['duration']
        samplerate = options['samplerate']
        try:
            save_noise(color, filename, duration, samplerate)
            self.stdout.write(
                self.style.SUCCESS(
                    f'Successfully generated {color} noise: {filename}'
                )
            )
        except Exception as e:
            raise CommandError(str(e))
