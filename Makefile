MANAGE = python src/manage.py

run:
	$(MANAGE) runserver


make_migrations:
	$(MANAGE) makemigrations


migrate:
	$(MANAGE) migrate

shell_plus:
	$(MANAGE) shell_plus --print-sql


createsuperuser:
	$(MANAGE) createsuperuser


collect-static:
	$(MANAGE) collectstatic