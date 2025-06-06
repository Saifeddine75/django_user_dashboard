# generate_makefile_commands.py
import sys
import django
from django.core.management import get_commands

def main():
    django.setup()
    commands = get_commands()
    for cmd in sorted(commands.keys()):
        print(f".PHONY: {cmd}")
        print(f"{cmd}:")
        print(f"\tpython manage.py {cmd} $(ARGS)")
        print()

if __name__ == "__main__":
    # Make sure DJANGO_SETTINGS_MODULE is set before running this
    main()
