#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import subprocess

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
VENV_PYTHON = os.path.join(ROOT_DIR, 'venv', 'Scripts', 'python.exe')

if os.path.exists(VENV_PYTHON):
    current_python = os.path.normcase(os.path.abspath(sys.executable))
    venv_python = os.path.normcase(os.path.abspath(VENV_PYTHON))
    if current_python != venv_python:
        script_path = os.path.join(ROOT_DIR, 'manage.py')
        args = [VENV_PYTHON, script_path] + sys.argv[1:]
        sys.exit(subprocess.check_call(args))


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
