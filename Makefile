#	Makefile for Django project with Tailwind CSS integration
#	Usage example from root, type:
#	make help	-	To show this help message

.PHONY: help dev server tailwind install migrate makemigrations createsuperuser shell test clean collectstatic build

help:
	@echo	"Available commands:"
	@echo	"	make development		-	Run Django server and Tailwind watch in parallel"
	@echo	"	make server				-	Run Django development server"
	@echo	"	make tailwind			-	Run Tailwind watch mode"
	@echo	"	make install			-	Install Python and npm dependencies"
	@echo	"	make migrate			-	Run database migrations"
	@echo	"	make makemigrations		-	Create new migrations"
	@echo	"	make createsuperuser	-	Create Django superuser"
	@echo	"	make shell				-	Open Django shell"
	@echo	"	make tests				-	Run tests"
	@echo	"	make collectstatic		-	Collect static files"
	@echo	"	make Build				-	Build Tailwind CSS for production"
	@echo	"	make clean				-	Remove generated files"

dev:
	honcho start -f Procfile.tailwind

server:
	python manage.py runserver

tailwind:
	cd theme/static_src && npm run dev

install:
	pip install -r requirements.txt
	cd theme/static_src && npm install

migrate:
	python manage.py migrate

makemigrations:
	python manage.py makemigrations

createsuperuser:
	python manage.py createsuperuser

shell:
	python manage.py shell

test:
	python manage.py test

collectstatic:
	python manage.py collectstatic --noinput

build:
	cd theme/static_src && npm run build
	python manage.py collectstatic --noinput

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	rm -rf staticfiles/
	rm -rf theme/static/css/dist/