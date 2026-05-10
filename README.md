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
cd Biblioteca-Virtual
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

*(Endpoints en desarrollo - se actualizará en versiones posteriores)*

### Estado Actual del Proyecto

✅ **Parte 1:** Configuración inicial de Django + DRF  
✅ **Parte 2:** Modelos de datos (Author y Book) y Serializers  
✅ **Parte 3:** Views y ViewSets de la API REST  
✅ **Parte 4:** Configuración completa de la API y datos de prueba  
✅ **Parte 5:** Funcionalidades CRUD completas  
✅ **Parte 6:** Búsqueda y filtros completas  
✅ **Parte 7:** Testing y validación final

### Partes Completadas

- **Parte 5**: CRUD completo para Autor y Libro mediante endpoints DRF.
- **Parte 6**: Búsqueda por título, género y autor; filtros por autor, género y año.  
- **Parte 7**: Cobertura de pruebas con `APITestCase` para crear, listar, actualizar, eliminar y filtrar registros.

### Modelos de Datos

#### Author (Autor)
- `name`: CharField (255 caracteres) - Nombre completo del autor
- `nationality`: CharField (100 caracteres) - Nacionalidad del autor
- `created_at`: DateTimeField - Fecha de creación (automática)
- `updated_at`: DateTimeField - Fecha de actualización (automática)

#### Book (Libro)
- `title`: CharField (255 caracteres) - Título del libro
- `publication_year`: IntegerField - Año de publicación
- `genre`: CharField (100 caracteres) - Género literario
- `author`: ForeignKey - Relación con Author (uno a muchos)
- `created_at`: DateTimeField - Fecha de creación (automática)
- `updated_at`: DateTimeField - Fecha de actualización (automática)

**Relación:** Un autor puede tener múltiples libros, pero cada libro pertenece a un solo autor.

### Serializers Implementados

- `AuthorSerializer`: Serializa todos los campos del modelo Author
- `BookSerializer`: Serializa Book con campo adicional `author_name`
- `BookDetailSerializer`: Serializa Book con información completa del autor relacionado

### ViewSets y Endpoints Implementados

#### AuthorViewSet
- **GET** `/api/authors/` - Listar todos los autores
- **POST** `/api/authors/` - Crear nuevo autor
- **GET** `/api/authors/{id}/` - Obtener autor específico
- **PUT/PATCH** `/api/authors/{id}/` - Actualizar autor
- **DELETE** `/api/authors/{id}/` - Eliminar autor
- **Búsqueda:** Por nombre y nacionalidad
- **Ordenamiento:** Por nombre, nacionalidad, fecha de creación

#### BookViewSet
- **GET** `/api/books/` - Listar todos los libros
- **POST** `/api/books/` - Crear nuevo libro
- **GET** `/api/books/{id}/` - Obtener libro específico
- **PUT/PATCH** `/api/books/{id}/` - Actualizar libro
- **DELETE** `/api/books/{id}/` - Eliminar libro
- **Búsqueda:** Por título, género y nombre del autor
- **Filtros:** Por autor, género, año de publicación
- **Ordenamiento:** Por título, año, género, fecha de creación

### Tecnologías Adicionales

- **django-filter==25.2** - Para filtros avanzados en la API

## Ejemplos de Uso de la API

### Datos de Prueba Incluidos

La API incluye datos de prueba para facilitar las pruebas:

**Autores:**
- Gabriel García Márquez (Colombia)
- Miguel de Cervantes (España)

**Libros:**
- "Cien Años de Soledad" (1967, Realismo Mágico) - Gabriel García Márquez
- "El Amor en los Tiempos del Cólera" (1985, Novela) - Gabriel García Márquez
- "Don Quijote de la Mancha" (1605, Novela) - Miguel de Cervantes

### Ejemplos de Endpoints

#### 1. Listar todos los libros
```bash
GET /api/books/
```

### Pruebas Automatizadas

El proyecto incluye un conjunto de pruebas en `books/tests.py` que verifica:
- creación, listado, actualización y eliminación de autores
- creación, listado, actualización y eliminación de libros
- búsqueda de libros por título
- filtrado de libros por género y autor

Ejecutar pruebas:
```bash
python manage.py test
```

#### 2. Buscar libros por título
```bash
GET /api/books/?search=Quijote
```

**Respuesta:**
```json
{
  "count": 3,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "title": "Cien Años de Soledad",
      "publication_year": 1967,
      "genre": "Realismo Mágico",
      "author": 1,
      "author_name": "Gabriel García Márquez",
      "created_at": "2026-05-09T18:40:00Z",
      "updated_at": "2026-05-09T18:40:00Z"
    },
    {
      "id": 2,
      "title": "El Amor en los Tiempos del Cólera",
      "publication_year": 1985,
      "genre": "Novela",
      "author": 1,
      "author_name": "Gabriel García Márquez",
      "created_at": "2026-05-09T18:40:00Z",
      "updated_at": "2026-05-09T18:40:00Z"
    },
    {
      "id": 3,
      "title": "Don Quijote de la Mancha",
      "publication_year": 1605,
      "genre": "Novela",
      "author": 2,
      "author_name": "Miguel de Cervantes",
      "created_at": "2026-05-09T18:40:00Z",
      "updated_at": "2026-05-09T18:40:00Z"
    }
  ]
}
```

#### 2. Buscar libros por título
```bash
GET /api/books/?search=Quijote
```

#### 3. Filtrar libros por género
```bash
GET /api/books/?genre=Novela
```

#### 4. Filtrar libros por autor
```bash
GET /api/books/?author=1
```

#### 5. Ordenar libros por año de publicación
```bash
GET /api/books/?ordering=publication_year
```

#### 6. Crear un nuevo libro
```bash
POST /api/books/
Content-Type: application/json

{
  "title": "Nueva Novela",
  "publication_year": 2024,
  "genre": "Ficción",
  "author": 1
}
```

#### 7. Listar todos los autores
```bash
GET /api/authors/
```

**Respuesta:**
```json
{
  "count": 2,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "name": "Gabriel García Márquez",
      "nationality": "Colombia",
      "created_at": "2026-05-09T18:40:00Z",
      "updated_at": "2026-05-09T18:40:00Z"
    },
    {
      "id": 2,
      "name": "Miguel de Cervantes",
      "nationality": "España",
      "created_at": "2026-05-09T18:40:00Z",
      "updated_at": "2026-05-09T18:40:00Z"
    }
  ]
}
```

#### 8. Buscar autores por nombre
```bash
GET /api/authors/?search=Gabriel
```

### Configuración de la API

- **Paginación:** 10 elementos por página
- **Rate Limiting:** 100 requests/hora (anónimos), 1000 requests/hora (autenticados)
- **Filtros:** Búsqueda, ordenamiento y filtrado avanzado
- **Renderers:** JSON y Browsable API (interfaz web para desarrollo)

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
---

**Última actualización:** 9 de Mayo de 2026
