# Noise Machine 🎵

A Django-based web application for generating and mixing colored noise sounds designed to aid concentration and provide calming ambient audio.

![Django](https://img.shields.io/badge/django-4.2.23-green.svg)
![Python](https://img.shields.io/badge/python-3.13-blue.svg)
![Tailwind CSS](https://img.shields.io/badge/tailwindcss-4.1.13-38bdf8.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## Features

### 🎨 Color Noise Generator
- **8 Types of Noise**: White, Pink, Red, Blue, Purple, Yellow, Brown, and Green noise
- **Interactive Cards**: Click to reveal playback controls
- **Audio Controls**: Play, pause, loop, and volume adjustment for each noise type
- **Responsive Design**: Works seamlessly on desktop and mobile devices

### 🎚️ Multi-Track Mixer
- **6-Track Mixing Console**: Professional-grade audio mixing interface
- **3-Band EQ**: High, Mid, and Low frequency control per track using rotary sliders
- **Dynamic Controls**: Solo, Mute, and individual volume faders
- **Master Output**: Global volume control with peak metering
- **Audio Source Selection**: Load different noise types per track
- **Web Audio API**: Real-time audio processing in the browser

### 👤 User Authentication
- **Django Allauth Integration**: Secure user registration and login
- **Guest Access**: Try the app without creating an account
- **Session Management**: Persistent guest sessions with UUID tokens
- **Custom User Model**: Extended user profiles with timestamps

### 🎨 Modern UI/UX
- **DaisyUI Components**: Beautiful, accessible UI components
- **Dark/Light Mode**: Theme switcher for user preference
- **Responsive Grid Layout**: Optimized for all screen sizes
- **Smooth Animations**: Hover effects and transitions

## Tech Stack

### Backend
- **Django 4.2.23**: Web framework
- **PostgreSQL**: Database (via Neon)
- **Gunicorn**: WSGI server for production
- **WhiteNoise**: Static file serving
- **Django Allauth**: Authentication system

### Frontend
- **Tailwind CSS 4.1**: Utility-first CSS framework
- **DaisyUI 5.1**: Component library
- **Font Awesome**: Icon library
- **Round Slider**: Rotary EQ controls
- **Web Audio API**: Audio processing

### Audio Processing
- **NumPy**: Numerical operations
- **SciPy**: Signal processing
- **SoundFile**: Audio file I/O
- **FFT-based Noise Generation**: High-quality colored noise synthesis

## Installation

### Prerequisites
- Python 3.13+
- Node.js 16+
- PostgreSQL (or use the provided Neon database)

### Setup Steps

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd noise-noise
```

2. **Create and activate virtual environment**
```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. **Install dependencies and setup project**
```bash
make setup
```

This will:
- Install Python dependencies
- Install npm dependencies
- Run security checks
- Apply database migrations
- Collect static files

4. **Create a superuser (optional)**
```bash
make createsuperuser
```

5. **Generate audio files**
```bash
python manage.py generate_noise white static/audio/white.wav --duration 10
python manage.py generate_noise pink static/audio/pink.wav --duration 10
python manage.py generate_noise red static/audio/red.wav --duration 10
python manage.py generate_noise blue static/audio/blue.wav --duration 10
python manage.py generate_noise purple static/audio/purple.wav --duration 10
python manage.py generate_noise yellow static/audio/yellow.wav --duration 10
python manage.py generate_noise brown static/audio/brown.wav --duration 10
python manage.py generate_noise green static/audio/green.wav --duration 10
```

6. **Run the development server**
```bash
make dev
```

This starts both Django and Tailwind in watch mode.

Visit `http://127.0.0.1:8000` in your browser.

## Usage

### Makefile Commands

```bash
make help              # Show all available commands
make dev               # Run Django + Tailwind in parallel
make server            # Run Django server only
make tailwind          # Run Tailwind watch mode
make install           # Install dependencies
make migrate           # Apply database migrations
make makemigrations    # Create new migrations
make createsuperuser   # Create admin user
make shell             # Open Django shell
make test              # Run tests
make collectstatic     # Collect static files
make build             # Build for production
make clean             # Remove generated files
```

### Noise Selector Page
1. Navigate to `/selector/selector/`
2. Click on any colored noise card
3. Use play/pause/loop controls
4. Adjust volume with the slider

### Multi-Track Mixer
1. Navigate to `/selector/mixer/`
2. Select audio source for each track
3. Adjust EQ (High/Mid/Low) using rotary knobs
4. Use Solo (S) and Mute (M) buttons
5. Control individual track volumes with vertical faders
6. Adjust master output volume

### Authentication
- Click "Login" to access the login page
- New users can sign up for an account
- Guest users can access features without registration

## Project Structure

```
noise-noise/
├── accounts/              # User authentication app
│   ├── models.py         # CustomUser, GuestSession
│   ├── views.py          # Auth views
│   └── templates/        # Login/signup templates
├── noise_machine/        # Main project settings
│   ├── settings.py       # Django configuration
│   └── urls.py           # URL routing
├── selector/             # Core app
│   ├── models.py         # AudioFile model
│   ├── views.py          # Selector & mixer views
│   ├── utils.py          # Noise generation algorithms
│   ├── templates/        # HTML templates
│   └── static/           # JS, CSS, audio files
├── theme/                # Tailwind theme app
│   ├── static_src/       # Source CSS/JS
│   └── templates/        # Base template
├── static/               # Static assets
├── staticfiles/          # Collected static files
├── requirements.txt      # Python dependencies
├── Makefile             # Development commands
├── Procfile.tailwind    # Development processes
└── manage.py            # Django management
```

## Noise Types Explained

- **White Noise**: Equal energy across all frequencies - great for masking distractions
- **Pink Noise**: More energy at lower frequencies - natural, relaxing sound
- **Brown Noise**: Even more bass-heavy - deep, rumbling sound for deep focus
- **Blue Noise**: High-frequency emphasis - energizing sound
- **Purple Noise**: Very high frequencies - useful for tinnitus relief
- **Yellow Noise**: Combination of pink noise and white noise
- **Green Noise**: Mid-frequency band (300-700Hz) - nature-like ambience
- **Red Noise**: Similar to brown noise - deep, warm sound

## Configuration

### Environment Variables
Create a `.env` file:
```env
SECRET_KEY=your-secret-key-here
DATABASE_URL=postgresql://user:pass@host/db
DEBUG=True
```

### Email Settings
For production, configure email backend in `settings.py`:
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-password'
```

## Deployment

### Heroku
1. Install Heroku CLI
2. Create Heroku app: `heroku create your-app-name`
3. Add PostgreSQL addon: `heroku addons:create heroku-postgresql:mini`
4. Set environment variables: `heroku config:set SECRET_KEY=...`
5. Deploy: `git push heroku main`
6. Run migrations: `heroku run python manage.py migrate`
7. Create superuser: `heroku run python manage.py createsuperuser`

### Production Checklist
- [ ] Set `DEBUG = False`
- [ ] Configure `ALLOWED_HOSTS`
- [ ] Set strong `SECRET_KEY`
- [ ] Configure email backend
- [ ] Run `make build` for production assets
- [ ] Configure SSL/HTTPS
- [ ] Set `CSRF_COOKIE_SECURE = True`
- [ ] Set `SESSION_COOKIE_SECURE = True`

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit changes: `git commit -am 'Add feature'`
4. Push to branch: `git push origin feature-name`
5. Submit a pull request

## License

This project is licensed under the MIT License.

## Acknowledgments

- **Noise Generation Algorithms**: Based on FFT and bandpass filtering techniques
- **UI Components**: DaisyUI and Tailwind CSS
- **Audio Processing**: Web Audio API
- **Django Community**: For excellent documentation and packages

## Support

For issues, questions or contributions, please open an issue on GitHub.

## Roadmap

- [ ] Add more noise types (Grey, Velvet, etc.)
- [ ] Implement preset saving/loading
- [ ] Add audio visualization (waveforms, spectrograms)
- [ ] Mobile app (React Native/Flutter)
- [ ] Export mixed audio to file
- [ ] Spotify/Apple Music integration
- [ ] Productivity timer integration
- [ ] Sleep timer functionality

---

## Made by
Me. For... better focus and relaxation? Yeah, lets go with that.
