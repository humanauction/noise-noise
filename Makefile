#	Makefile for Django project with Tailwind CSS integration
#	Usage example from root, type:
#	make help - To show this help message

.PHONY: help setup dev server tailwind install migrate makemigrations createsuperuser shell test clean collectstatic build check-venv

help:
	@echo	"Available commands:"
	@echo	"	make dev				-	Run Django server and Tailwind watch in parallel"
	@echo	"	make server				-	Run Django development server"
	@echo	"	make tailwind			-	Run Tailwind watch mode"
	@echo	"	make install			-	Install Python and npm dependencies"
	@echo	"	make migrate			-	Run database migrations"
	@echo	"	make makemigrations		-	Create new migrations"
	@echo	"	make createsuperuser	-	Create Django superuser"
	@echo	"	make shell				-	Open Django shell"
	@echo	"	make test				-	Run tests"
	@echo	"	make collectstatic		-	Collect static files"
	@echo	"	make build				-	Build Tailwind CSS for production"
	@echo	"	make clean				-	Remove generated files"
# What 'make setup' does:
	@echo	"	make setup				-	Complete project setup (venv, deps, migrations)"
# FIRST TIME SETUP ONLY!!
# Checks venv is activated (exits if not)
# Upgrades pip to latest version
# Installs requirements.txt dependencies
# Runs pip check for broken dependencies
# Installs safety and checks for known vulnerabilities
# Installs npm dependencies for Tailwind
# Runs migrations
# Collects static files
# FIRST TIME SETUP ONLY!!
# To use:
# 1. Create virtual environment (if not already created):
	python3 -m venv .venv
# 2. Activate virtual environment:
	source .venv/bin/activate

	make setup
# Daily development
# make dev

# List of commands below
setup: check-venv
	@echo "🔧 Setting up project..."
	@echo "📦 Installing Python dependencies..."
	pip install --upgrade pip
	pip install -r requirements.txt
	@echo "🔒 Checking for security vulnerabilities..."
	pip check
	pip install safety
	safety check --json || echo "⚠️	Security issues found - review above"
	@echo "📦 Installing npm dependencies..."
	cd theme/static_src && npm install
	@echo "🗄️	Running migrations..."
	python manage.py migrate
	@echo "📁 Collecting static files..."
	python manage.py collectstatic --noinput
	@echo "✅ Setup complete! Run 'make dev' to start."

check-venv:
	@if [ -z "$$VIRTUAL_ENV" ]; then \
		echo "❌ Virtual environment not activated!"; \
		echo "Run: source .venv/bin/activate"; \
		exit 1; \
	else \
		echo "✅ Virtual environment active: $$VIRTUAL_ENV"; \
	fi


dev: check-venv
	honcho start -f Procfile.tailwind

server: check-venv
	python manage.py runserver

tailwind:
	cd theme/static_src && npm run dev

install: check-venv
	pip install -r requirements.txt
	cd theme/static_src && npm install

migrate: check-venv
	python manage.py migrate

makemigrations: check-venv
	python manage.py makemigrations

createsuperuser: check-venv
	python manage.py createsuperuser

shell: check-venv
	python manage.py shell

test: check-venv
	python manage.py test

collectstatic: check-venv
	python manage.py collectstatic --noinput

build: check-venv
	cd theme/static_src && npm run build
	python manage.py collectstatic --noinput

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	rm -rf staticfiles/
	rm -rf theme/static/css/dist/