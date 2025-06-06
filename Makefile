-include django_commands.mk

# Variables
VENV=.venv
ACTIVATE_VENV=FALSE
PYTHON=$(VENV)/Scripts/python.exe
USE_UV=TRUE # Set to TRUE if you want to use uv pip, otherwise set to FALSE
SERVER_HOST=LOCALHOST
SERVER_PORT=8000

ifeq ($(USE_UV), TRUE)
	PIP=uv pip
else
	PIP=pip
endif


.PHONY: \
	activate-env \
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
	ifeq ($(ACTIVATE_VENV), TRUE)
		activate_env
	else
		@read -p "Did you activate your virtual environment named \".venv\" ? (y/n) " answer; \
		if [ "$$answer" != "y" ]; then \
			echo "Aborted."; \
			echo "Virtual env not found."; \
			exit 1; \
		fi
	endif
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
	$(PYTHON) manage.py runserver $(SERVER_HOST):$(SERVER_PORT)

migrate:
	$(PYTHON) manage.py migrate

migrations:
	$(PYTHON) manage.py makemigrations

delete-migrations:
	$(PYTHON) clean_migrations.py
	rm db.sqlite3
	# find . -path "*/migrations/*.py" ! -name "__init__.py" -delete
	# find . -path "*/migrations/*.pyc" -delete

# Delete and recreate migrations
remake-migrations: delete-migrations
	$(PYTHON) manage.py makemigrations
	$(PYTHON) manage.py migrate

reset-db:
	$(PYTHON) manage.py flush --no-input
	$(PYTHON) manage.py migrate
	$(PYTHON) manage.py createsuperuser

save-db:
	$(PYTHON) manage.py dumpdata > db.json

load-db:
	$(PYTHON) manage.py loaddata db.json

shell:
	$(PYTHON) manage.py shell

createsuperuser:
	$(PYTHON) manage.py createsuperuser

list-cmd:
	@echo "Available Django commands:"
	$(PYTHON) manage.py help | grep -E '^[ ]+[a-zA-Z]' | awk '{print $$1}'

update-cmd:activate-env
	export DJANGO_SETTINGS_MODULE=myproject.settings
	cd scripts
	$(PYTHON) update_commands.py > django_commands.mk
	@echo "Commands from django_commands.mk:"
	@grep '^\.[Pp][Hh][Oo][Nn][Yy]: ' django_commands.mk | sed 's/\.PHONY: //' | sort


test:
	$(PYTHON) manage.py test

collectstatic:
	$(PYTHON) manage.py collectstatic --noinput

lint:
	ruff check .

format:
	black .

# Commande personnalisée avec un argument
app:
	$(PYTHON) manage.py startapp $(name)

# Pour supprimer les fichiers compilés Python
clean:
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete
