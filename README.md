# BookVerse API 📚

**AUTOR:** Bellido Chambi Rony Widmer

## Descripción del Proyecto

BookVerse es una API REST para gestionar una Biblioteca Virtual utilizando Django y Django REST Framework. La aplicación permite administrar libros y autores en una biblioteca digital, con capacidad de crear, leer, actualizar y eliminar registros a través de endpoints RESTful.

### Entidades

- **Libros**: Información sobre libros (título, año de publicación, género)
- **Autores**: Información sobre autores (nombre, nacionalidad)

Cada libro está asociado con un autor, estableciendo una relación de uno a muchos.

## Tecnologías Utilizadas

- **Python 3.11**
- **Django 5.2.14** - Framework web
- **Django REST Framework 3.17.1** - Toolkit para construir APIs REST
- **SQLite** - Base de datos
- **Git** - Control de versiones

## Instalación y Configuración

### Requisitos Previos
- Python 3.11 o superior
- pip (gestor de paquetes de Python)

### Pasos de Instalación

1. **Clonar el repositorio:**
```bash
git clone https://github.com/aleyto123/Biblioteca-Virtual.git
cd bookverse_api
```

2. **Crear entorno virtual:**
```bash
# Windows
python -m venv venv

# Linux/Mac
python3 -m venv venv
```

3. **Activar entorno virtual:**
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

4. **Instalar dependencias:**
```bash
pip install -r requirements.txt
```

5. **Realizar migraciones de base de datos:**
```bash
python manage.py migrate
```

6. **Ejecutar el servidor de desarrollo:**
```bash
python manage.py runserver
```

El servidor estará disponible en: `http://127.0.0.1:8000/`

## Endpoints Disponibles

### Libros (Books)

#### Listar todos los libros
```bash
GET /api/books/
curl -X GET http://127.0.0.1:8000/api/books/
```

**Respuesta esperada:**
```json
[
  {
    "id": 1,
    "title": "El Quijote",
    "publication_year": 1605,
    "genre": "Novela",
    "author": 1
  }
]
```

#### Crear un nuevo libro
```bash
POST /api/books/
curl -X POST http://127.0.0.1:8000/api/books/ \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Cien Años de Soledad",
    "publication_year": 1967,
    "genre": "Realismo Mágico",
    "author": 1
  }'
```

#### Obtener un libro específico
```bash
GET /api/books/{id}/
curl -X GET http://127.0.0.1:8000/api/books/1/
```

#### Actualizar un libro
```bash
PUT /api/books/{id}/
curl -X PUT http://127.0.0.1:8000/api/books/1/ \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Cien Años de Soledad",
    "publication_year": 1967,
    "genre": "Ficción",
    "author": 1
  }'
```

#### Eliminar un libro
```bash
DELETE /api/books/{id}/
curl -X DELETE http://127.0.0.1:8000/api/books/1/
```

#### Buscar libros por título o género
```bash
GET /api/books/?search=Quijote
curl -X GET http://127.0.0.1:8000/api/books/?search=Quijote
```

### Autores (Authors)

#### Listar todos los autores
```bash
GET /api/authors/
curl -X GET http://127.0.0.1:8000/api/authors/
```

**Respuesta esperada:**
```json
[
  {
    "id": 1,
    "name": "Miguel de Cervantes",
    "nationality": "España"
  }
]
```

#### Crear un nuevo autor
```bash
POST /api/authors/
curl -X POST http://127.0.0.1:8000/api/authors/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Gabriel García Márquez",
    "nationality": "Colombia"
  }'
```

#### Obtener un autor específico
```bash
GET /api/authors/{id}/
curl -X GET http://127.0.0.1:8000/api/authors/1/
```

#### Actualizar un autor
```bash
PUT /api/authors/{id}/
curl -X PUT http://127.0.0.1:8000/api/authors/1/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Miguel de Cervantes",
    "nationality": "España"
  }'
```

#### Eliminar un autor
```bash
DELETE /api/authors/{id}/
curl -X DELETE http://127.0.0.1:8000/api/authors/1/
```

## Estructura del Proyecto

```
bookverse_api/
├── config/              # Configuración del proyecto
│   ├── settings.py     # Configuración de Django
│   ├── urls.py         # URLs principales
│   └── wsgi.py         # Configuración WSGI
├── books/              # Aplicación de libros y autores
│   ├── models.py       # Modelos de datos
│   ├── serializers.py  # Serializadores DRF
│   ├── views.py        # Vistas de la API
│   ├── urls.py         # URLs de la app
│   └── migrations/     # Migraciones de BD
├── manage.py           # Script de gestión de Django
├── requirements.txt    # Dependencias del proyecto
└── README.md          # Este archivo
```

## Notas Adicionales

- El proyecto utiliza SQLite como base de datos por defecto.
- No se utiliza el Django Admin para la gestión de datos.
- Toda la gestión se realiza mediante endpoints REST.
- Los commits del repositorio son progresivos y descriptivos para rastrear el desarrollo del proyecto.

---

**Última actualización:** 9 de Mayo de 2026
