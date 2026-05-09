from rest_framework import serializers
from .models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):
    """Serializador para el modelo Author"""
    
    class Meta:
        model = Author
        fields = ['id', 'name', 'nationality', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


class BookSerializer(serializers.ModelSerializer):
    """Serializador para el modelo Book con información del autor"""
    author_name = serializers.CharField(source='author.name', read_only=True)
    
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'genre', 'author', 'author_name', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


class BookDetailSerializer(serializers.ModelSerializer):
    """Serializador detallado para el modelo Book con información completa del autor"""
    author = AuthorSerializer(read_only=True)
    
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'genre', 'author', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at', 'author']
