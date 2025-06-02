# Variables
PYTHON=python
MANAGE=manage.py

# Cibles par défaut
.PHONY: \
	run \
	migrate \
	makemigrations \
	shell \
	createsuperuser \
	test \
	collectstatic \
	lint \
	format \
	app \
	clean


# Commandes
run:
	$(PYTHON) $(MANAGE) runserver

migrate:
	$(PYTHON) $(MANAGE) migrate

makemigrations:
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