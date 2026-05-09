from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Author, Book


class BooksAuthorsAPITest(APITestCase):
    def setUp(self):
        self.author1 = Author.objects.create(name="Gabriel García Márquez", nationality="Colombia")
        self.author2 = Author.objects.create(name="Miguel de Cervantes", nationality="España")

        self.book1 = Book.objects.create(
            title="Cien Años de Soledad",
            publication_year=1967,
            genre="Realismo Mágico",
            author=self.author1,
        )
        self.book2 = Book.objects.create(
            title="El Amor en los Tiempos del Cólera",
            publication_year=1985,
            genre="Novela",
            author=self.author1,
        )
        self.book3 = Book.objects.create(
            title="Don Quijote de la Mancha",
            publication_year=1605,
            genre="Novela",
            author=self.author2,
        )

    def test_list_authors(self):
        url = reverse('author-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 2)

    def test_create_author(self):
        url = reverse('author-list')
        data = {'name': 'Isabel Allende', 'nationality': 'Chile'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Author.objects.count(), 3)
        self.assertEqual(Author.objects.last().name, 'Isabel Allende')

    def test_update_author(self):
        url = reverse('author-detail', kwargs={'pk': self.author1.pk})
        data = {'name': 'Gabriel García Márquez', 'nationality': 'México'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.author1.refresh_from_db()
        self.assertEqual(self.author1.nationality, 'México')

    def test_delete_author(self):
        url = reverse('author-detail', kwargs={'pk': self.author2.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Author.objects.count(), 1)

    def test_list_books(self):
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 3)

    def test_create_book(self):
        url = reverse('book-list')
        data = {
            'title': 'La Casa de los Espíritus',
            'publication_year': 1982,
            'genre': 'Realismo Mágico',
            'author': self.author1.pk,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 4)
        self.assertEqual(Book.objects.last().title, 'La Casa de los Espíritus')

    def test_update_book(self):
        url = reverse('book-detail', kwargs={'pk': self.book1.pk})
        data = {
            'title': self.book1.title,
            'publication_year': 1968,
            'genre': self.book1.genre,
            'author': self.author1.pk,
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.publication_year, 1968)

    def test_delete_book(self):
        url = reverse('book-detail', kwargs={'pk': self.book2.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 2)

    def test_search_books_by_title(self):
        url = reverse('book-list')
        response = self.client.get(url, {'search': 'Quijote'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)
        self.assertEqual(response.data['results'][0]['title'], 'Don Quijote de la Mancha')

    def test_filter_books_by_genre(self):
        url = reverse('book-list')
        response = self.client.get(url, {'genre': 'Novela'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 2)

    def test_filter_books_by_author(self):
        url = reverse('book-list')
        response = self.client.get(url, {'author': self.author1.pk})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 2)
