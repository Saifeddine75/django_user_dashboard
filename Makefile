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

shell:
	$(PYTHON) $(MANAGE) shell

createsuperuser:
	$(PYTHON) $(MANAGE) createsuperuser

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