-include django_commands.mk

# Variables
PYTHON=python
MANAGE=manage.py
UV=TRUE # Set to TRUE if you want to use uv pip, otherwise set to FALSE
ifeq ($(UV), TRUE)
	PIP=uv pip
else
	PIP=pip
endif


.PHONY: \
	check-venv \
	install-dev \
	run \
	migrate \
	migrations \
	shell \
	createsuperuser \
	list_commands \
	update_commands \
	test \
	collectstatic \
	lint \
	format \
	app \
	clean



install-dev:
	@echo "Vérification de l'environnement virtuel..."
	make check-venv
	@read -p "Did you activate your virtual environment named \".venv\" ? (y/n) " answer; \
	if [ "$$answer" != "y" ]; then \
		echo "Aborted."; \
		echo "Virtual env not found."; \
		exit 1; \
	fi
	@echo "Installation de Django..."
	$(PIP) install django
	@echo "Création des migrations..."
	make migrations
	@echo "Exécution des migrations..."
	make migrate
	@echo "Démarrage du serveur de développement..."
	make run


# Check if the virtual environment is active and its name is ".venv"
check-venv:
	@if [ -z "$$VIRTUAL_ENV" ]; then \
		echo "❌ No virtual environment is activated."; \
		exit 1; \
	elif [ "$$(basename $$VIRTUAL_ENV)" != ".venv" ]; then \
		echo "❌ Wrong virtual environment. Expected '.venv', got '$$(basename $$VIRTUAL_ENV)'."; \
		exit 1; \
	else \
		echo "✅ Virtual environment '.venv' is active."; \
	fi

run:
	@echo "Starting the Django development server..."
	$(PYTHON) $(MANAGE) runserver

migrate:
	$(PYTHON) $(MANAGE) migrate

migrations:
	$(PYTHON) $(MANAGE) makemigrations

delete-migrations:
	python clean_migrations.py
	rm db.sqlite3
	# find . -path "*/migrations/*.py" ! -name "__init__.py" -delete
	# find . -path "*/migrations/*.pyc" -delete

# Delete and recreate migrations
remake-migrations: delete-migrations
	python manage.py makemigrations
	python manage.py migrate

reset-db:
	python manage.py flush --no-input
	python manage.py migrate
	python manage.py createsuperuser

save-db:
	python manage.py dumpdata > db.json

load-db:
	python manage.py loaddata db.json

shell:
	$(PYTHON) $(MANAGE) shell

createsuperuser:
	$(PYTHON) $(MANAGE) createsuperuser

list-commands:
	@echo "Available Django commands:"
	$(PYTHON) $(MANAGE) help | grep -E '^[ ]+[a-zA-Z]' | awk '{print $$1}'

update-commands:
	export DJANGO_SETTINGS_MODULE=../myproject.settings
	python Scripts/update_commands.py > django_commands.mk
	@echo "Commands from django_commands.mk:"
	@grep '^\.[Pp][Hh][Oo][Nn][Yy]: ' django_commands.mk | sed 's/\.PHONY: //' | sort



test:
	$(PYTHON) $(MANAGE) test

collectstatic:
	$(PYTHON) $(MANAGE) collectstatic --noinput

lint:
	ruff check .

format:
	black .

# Commande personnalisée avec un argument
app:
	$(PYTHON) $(MANAGE) startapp $(name)

# Pour supprimer les fichiers compilés Python
clean:
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete
