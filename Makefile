# Variables
PYTHON=python
MANAGE=manage.py


.PHONY: \
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
	@read -p "Did you activate your virtual environment named ".venv" ? (y/n) " answer; \
	if [ "$$answer" != "y" ]; then \
		echo "Aborted."; \
		exit 1; \
	fi
	@echo "Installation de Django..."
	uv pip install django
	@echo "Création des migrations..."
	make migrations
	@echo "Exécution des migrations..."
	make migrate
	@echo "Démarrage du serveur de développement..."
	make run

run:
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
	flake8 .

format:
	black .

# Commande personnalisée avec un argument
app:
	$(PYTHON) $(MANAGE) startapp $(name)

# Pour supprimer les fichiers compilés Python
clean:
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete