from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet, BookViewSet

# Crear el router
router = DefaultRouter()

# Registrar los ViewSets
router.register(r'authors', AuthorViewSet, basename='author')
router.register(r'books', BookViewSet, basename='book')

# Las URLs generadas automáticamente serán:
# - /authors/ (GET, POST)
# - /authors/{id}/ (GET, PUT, PATCH, DELETE)
# - /books/ (GET, POST)
# - /books/{id}/ (GET, PUT, PATCH, DELETE)

urlpatterns = [
    path('', include(router.urls)),
]