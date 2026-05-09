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

*(Endpoints en desarrollo - se actualizará en versiones posteriores)*

### Estado Actual del Proyecto

✅ **Parte 1:** Configuración inicial de Django + DRF  
✅ **Parte 2:** Modelos de datos (Author y Book) y Serializers  
🔄 **Parte 3:** Views y ViewSets (en progreso)  
⏳ **Parte 4:** URLs y configuración de rutas  
⏳ **Parte 5:** Funcionalidades CRUD completas  
⏳ **Parte 6:** Búsqueda y filtros  
⏳ **Parte 7:** Testing y validación final

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
