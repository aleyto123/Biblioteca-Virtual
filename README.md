# BookVerse API 📚

Una API REST para gestionar una Biblioteca Virtual utilizando Django y Django REST Framework.

## Descripción

BookVerse es una aplicación que permite administrar libros y autores en una biblioteca digital. 

### Entidades

- **Libros**: Información sobre libros (título, año de publicación, género)
- **Autores**: Información sobre autores (nombre, nacionalidad)

Cada libro está asociado con un autor.

## Tecnologías

- Django 5.2
- Django REST Framework 3.17
- SQLite

## Instalación

1. Crear entorno virtual:
```bash
python -m venv venv
```

2. Activar entorno virtual:
```bash
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

4. Realizar migraciones:
```bash
python manage.py migrate
```

5. Ejecutar servidor:
```bash
python manage.py runserver
```

## Endpoints

(Por completar en siguientes versiones)

## Autor

Desarrollado como proyecto de la Biblioteca Virtual
