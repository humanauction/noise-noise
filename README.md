# Noise Machine 🎵

A Django-based web application for generating and mixing colored noise sounds designed to aid concentration and provide calming ambient audio.

![Django](https://img.shields.io/badge/django-4.2.23-green.svg)
![Python](https://img.shields.io/badge/python-3.13-blue.svg)
![Tailwind CSS](https://img.shields.io/badge/tailwindcss-4.1.13-38bdf8.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## Features

### 🎨 Color Noise Generator

- **8 Types of Noise**: White, Pink, Red, Blue, Purple, Yellow, Brown, and Green noise
- **Interactive Flip Cards**: Click cards to reveal playback controls
- **Individual Audio Controls**: Play, pause, loop, and volume adjustment for each noise type
- **Responsive Grid Layout**: Optimized card layout for all screen sizes
- **Seamless Looping**: For continuous ambient sound
- **Audio Controls**: Play, pause, loop and volume adjustment
- **Responsive Design**: Works on desktop and mobile devices

### 🎚️ Multi-Track Mixer

- **Multi-Track Mixing Console**: Professional-grade audio mixing interface
- **3-Band EQ**: High, Mid, and Low frequency control per track using rotary sliders
- **Dynamic Controls**: Solo, Mute and individual volume faders
- **Master Output**: Global volume control with peak metering
- **Dynamic Audio Source Selection**: Load any generated noise type into any track
- **Web Audio API**: Real-time audio processing in the browser

### 👤 User Authentication

- **Django Allauth Integration**: Secure user registration and login
- **Guest Access**: Try the app without creating an account
- **Session Management**: Persistent guest sessions with UUID tokens
- **Custom User Model**: Extended user profiles with timestamps

### 🎨 Modern UI/UX

- **DaisyUI Components**: UI components
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
- **honcho**: Process manager for local development

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

#### 1. Clone the repository

```bash
git clone https://github.com/humanauction/noise-noise.git
cd noise-noise
```

#### 2. Create and activate virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

#### 2.5. Create environment file

```bash
# Create .env file with your credentials
echo 'SECRET_KEY="your-secret-key-here"' > .env
echo 'DATABASE_URL=your-database-url' >> .env
```

#### 3. Install dependencies and setup project

```bash
make setup
```

This will:

- Install Python dependencies
- Install npm dependencies
- Run security checks
- Apply database migrations
- **Build Tailwind CSS**
- Collect static files

#### 4. Creating a superuser

```bash
make createsuperuser
```

#### 5. Audio Files

The project includes pre-generated noise files in `static/audio/`. However, if you need to regenerate or add custom durations:

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

**Available noise types:** white, pink, red, blue, purple, yellow, brown, green

**Note:** The repository includes additional ambient sounds:

- `bathroom-fan.wav`
- `outskirts-city.wav`
- `trainstation.wav`

#### 5.5 Git and Static Files

The `.gitignore` excludes `/static/*` to prevent committing generated files. However, audio files are an exception:

```gitignore
/static/*
!/static/audio/
!/static/audio/**
```

To commit audio files:

```bash
git add -f static/audio/*.wav
```

For Tailwind CSS (if rebuilding):

```bash
cd theme/static_src && npm run build && cd ../..
git add -f theme/static/css/dist/styles.css
```

#### 6. Run the development server

```bash
make dev
```

This starts both Django and Tailwind in watch mode.

Visit `http://127.0.0.1:8000` in your browser.

---

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
2. Click on any colored noise card to reveal controls
3. Use play/pause/loop buttons
4. Adjust volume with the range slider

**Audio files are loaded from:** `/static/audio/{color}.wav`

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

```bash
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

For production, configure bespoke email backend in `settings.py`:

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-password'
```

## Deployment

### Heroku Deployment

#### Prerequisites

- Heroku CLI installed: `brew install heroku/brew/heroku` (macOS)
- Heroku account created

#### Steps

1. **Login and create app**

```bash
heroku login
heroku create your-app-name
```

2. **Add PostgreSQL**

```bash
heroku addons:create heroku-postgresql:essential-0
```

3. **Set environment variables**

```bash
heroku config:set SECRET_KEY="$(python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())')"
heroku config:set DEBUG=False
heroku config:set DJANGO_SETTINGS_MODULE=noise_machine.settings
```

4. **Deploy**

```bash
git push heroku main
```

5. **Run migrations and collect static**

```bash
heroku run python manage.py migrate
heroku run python manage.py collectstatic --noinput
```

6. **Create superuser**

```bash
heroku run python manage.py createsuperuser
```

7. **Open app**

```bash
heroku open
```

#### Troubleshooting

**CSS/JS not loading:**

```bash
# Rebuild Tailwind locally
cd theme/static_src && npm run build && cd ../..

# Force add built CSS
git add -f theme/static/css/dist/styles.css

# Commit and redeploy
git commit -m "Add built CSS"
git push heroku main
heroku run python manage.py collectstatic --noinput
```

**Audio files missing:**

```bash
# Force add audio files
git add -f static/audio/*.wav
git commit -m "Add audio files"
git push heroku main
heroku run python manage.py collectstatic --noinput
```

**Check logs:**

```bash
heroku logs --tail
```

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

### Completed ✅

- [x] 8 colored noise types (white, pink, red, blue, purple, yellow, brown, green)
- [x] Multi-track mixer with EQ
- [x] Guest session support
- [x] Dark/light mode

### In Progress 🚧

- [ ] Audio visualization (waveforms, spectrograms)
- [ ] Preset saving/loading

### Planned 📋

- [ ] Add more noise types (nature, industrial, etc.)
- [ ] Implement preset saving/loading
- [ ] Mobile app (React Native, maybe Flutter)
- [ ] Export mixed audio to file
- [ ] Spotify/Apple Music integration
- [ ] Routine timer integration
- [ ] Sleep timer functionality

---

## Made by

Me. For... better focus and relaxation? Yeah, lets go with that.

<!-- TODO: ## 🌐 Live Demo

**[View Live App →](https://noise-machine-74f044719326.herokuapp.com/)**

Try it now without installing anything!

TODO:## 📸 Screenshots

### Noise Selector
*[Add screenshot of selector page with colored cards]*

### Multi-Track Mixer
*[Add screenshot of mixer interface with EQ knobs]*

### Dark Mode
*[Add screenshot showing theme toggle]* -->

## ⚡ Performance

- **Audio files:** Pre-generated 10-second loops (441KB each)
- **Web Audio API:** Client-side processing for zero latency
- **Caching:** WhiteNoise serves static files with aggressive caching
- **Database:** PostgreSQL on Neon (serverless)

**Tips for best performance:**

- Use headphones for better audio quality
- Chrome/Edge recommended (best Web Audio API support)
- Close unused tabs to free memory

### Custom Management Commands

#### Generate Noise

Creates colored noise audio files using FFT and signal processing.

```bash
python manage.py generate_noise <color> <output_path> --duration <seconds>
```

**Example:**

```bash
python manage.py generate_noise pink static/audio/pink.wav --duration 30
```

**Available colors:**

- `white` - Equal power across all frequencies
- `pink` - -3dB per octave (1/f noise)
- `red` / `brown` - -6dB per octave (Brownian noise)
- `blue` - +3dB per octave
- `purple` - +6dB per octave
- `yellow` - Pink + white blend
- `green` - Bandpass filtered (300-700Hz)

**Implementation:** See `selector/management/commands/generate_noise.py`

## 🙏 Acknowledgments

Special thanks to:

- The Django and Tailwind CSS communities
- Contributors to NumPy, SciPy, and Web Audio API
- Early testers and feedback providers

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details
