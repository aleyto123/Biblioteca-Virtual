from django.db import models


class Author(models.Model):
    """Modelo para representar autores en la biblioteca"""
    name = models.CharField(max_length=255, help_text="Nombre completo del autor")
    nationality = models.CharField(max_length=100, help_text="Nacionalidad del autor")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"
        ordering = ['name']

    def __str__(self):
        return f"{self.name} ({self.nationality})"


class Book(models.Model):
    """Modelo para representar libros en la biblioteca"""
    title = models.CharField(max_length=255, help_text="Título del libro")
    publication_year = models.IntegerField(help_text="Año de publicación")
    genre = models.CharField(max_length=100, help_text="Género literario del libro")
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='books',
        help_text="Autor del libro"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Libro"
        verbose_name_plural = "Libros"
        ordering = ['title']
        unique_together = ['title', 'author']  # No permitir libros duplicados del mismo autor

    def __str__(self):
        return f"{self.title} - {self.author.name}"
