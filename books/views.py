from rest_framework import viewsets, filters
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer, BookDetailSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gestionar autores.
    Proporciona operaciones CRUD completas para el modelo Author.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [AllowAny]  # Para desarrollo - en producción usar autenticación

    # Configuración de filtros y búsqueda
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'nationality']
    ordering_fields = ['name', 'nationality', 'created_at']
    ordering = ['name']  # Orden por defecto


class BookViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gestionar libros.
    Proporciona operaciones CRUD completas para el modelo Book.
    Incluye búsqueda por título y género, y filtros por autor.
    """
    queryset = Book.objects.select_related('author').all()  # Optimización con select_related
    permission_classes = [AllowAny]  # Para desarrollo - en producción usar autenticación

    # Configuración de filtros y búsqueda
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['author', 'genre', 'publication_year']
    search_fields = ['title', 'genre', 'author__name']  # Búsqueda en título, género y nombre del autor
    ordering_fields = ['title', 'publication_year', 'genre', 'created_at']
    ordering = ['title']  # Orden por defecto

    def get_serializer_class(self):
        """
        Retorna el serializer apropiado según la acción.
        Para list y retrieve usa BookSerializer (con author_name),
        para create/update usa BookSerializer básico.
        """
        if self.action in ['list', 'retrieve']:
            return BookSerializer
        return BookSerializer  # Para create, update, partial_update

    def perform_create(self, serializer):
        """Método personalizado para creación de libros"""
        serializer.save()

    def perform_update(self, serializer):
        """Método personalizado para actualización de libros"""
        serializer.save()
