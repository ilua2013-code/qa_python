import pytest
from main import BooksCollector


class TestBooksCollector:


    # Первый метод 
    length_val = ['A', 'AA', 'A' * 25, 'A' * 39, 'A' * 40]
    @pytest.mark.parametrize('book', length_val)
    def test_add_new_book_valid_length_and_borders(self, bookscollection, book):
        bookscollection.add_new_book(book)
        assert book in bookscollection.books_genre and bookscollection.books_genre[book] == ''

    length_inval = ['', 'A' * 41, 'A' * 60]
    @pytest.mark.parametrize('book', length_inval)
    def test_add_new_book_invalid_length_and_borders(self, bookscollection, book):
        bookscollection.add_new_book(book)
        assert book not in bookscollection.books_genre 

    def test_add_new_book_add_two_books(self, bookscollection):
        bookscollection.add_new_book('Гордость и предубеждение и зомби')
        bookscollection.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(bookscollection.books_genre) == 2
    
    
    # Второй метод 
    def test_set_book_valid_book_and_genre_from_list_successful_addition_of_genre(self, bookscollection):
        book = 'Война-56'
        genre = 'Ужасы'
        bookscollection.add_new_book(book)
        bookscollection.set_book_genre(book, genre)
        assert bookscollection.books_genre.get('Война-56') == 'Ужасы'

    def test_set_book_valid_book_and_genre_not_on_the_list_no_genre_added(self, bookscollection):
        book = 'Война'
        genre = 'Роман'
        bookscollection.add_new_book(book)
        bookscollection.set_book_genre(book, genre)
        assert bookscollection.books_genre.get('Война') == ''

    def test_set_book_booknot_in_list_and_genre_from_list_genre_not_update_if_not_book(self, bookscollection):
        book = 'ФФ'
        genre = 'Ужасы'
        bookscollection.set_book_genre(book, genre)
        assert bookscollection.books_genre.get('ФФ') != 'Ужасы'

    # Третий метод
    def test_get_book_genre_book_and_genre_from_list_return_value_book_from_dict(self, bookscollection):
        book = 'Идиот'
        genre = 'Комедии'
        bookscollection.add_new_book(book)
        bookscollection.set_book_genre(book, genre)
        assert bookscollection.get_book_genre('Идиот') == 'Комедии'

    def test_get_book_genre_genre_from_list_book_not_from_list_return_None(self, bookscollection):
        book = 'Капитан'
        assert bookscollection.get_book_genre(book) is None
    
    # Четвертый метод
    def test_get_books_with_specific_genre_3_books_return_list_book_with_one_genre(self, bookscollection):
        book =  ['Ужасающий', 'Ужасающий2', 'Ужасающий3']
        genre = 'Ужасы'
        genre1 = 'Детективы'
        for i in range(len(book)):
            bookscollection.add_new_book(book[i])
            if i < 2:
                bookscollection.set_book_genre(book[i], genre)
            else:
                bookscollection.set_book_genre(book[i], genre1)
        assert bookscollection.get_books_with_specific_genre(genre) == ['Ужасающий', 'Ужасающий2']
    # Пятый метод 
    def test_get_books_genre_book_and_genre_return_dict(self, bookscollection):
        bookscollection.add_new_book('Война-56')
        bookscollection.set_book_genre('Война-56', 'Ужасы')
        assert bookscollection.get_books_genre() == {'Война-56': 'Ужасы'}
    
    
    # Шестой метод 
    def test_get_books_for_children_add_4_book_return_book_for_children(self, bookscollection):
        book = ['Лолита','Американский психопат', 'Заводной апельсин', 'Ну, погоди!']
        genre = 'Детективы'
        genre1 = 'Комедии'
        for i in range(len(book)):
            bookscollection.add_new_book(book[i])
            if i < 3:
                bookscollection.set_book_genre(book[i], genre)
            else:
                bookscollection.set_book_genre(book[i], genre1)
        assert bookscollection.get_books_for_children() == [book[-1]]

    def test_get_books_for_children_add_3_book_return_empty_list(self, bookscollection):
        book = ['Лолита','Американский психопат', 'Заводной апельсин']
        genre = 'Детективы'
        for i in range(len(book)):
            bookscollection.add_new_book(book[i])
            bookscollection.set_book_genre(book[i], genre)
        assert bookscollection.get_books_for_children() == []

    # Седьмой метод 
    def test_add_book_in_favorites_book_from_list_add_in_favorites(self, bookscollection):
        book = 'Заводной апельсин'
        bookscollection.add_new_book(book)
        bookscollection.add_book_in_favorites(book)
        assert book in bookscollection.favorites

    def test_add_book_in_favorites_book_from_list_book_not_add_again(self, bookscollection):
        book = 'Заводной апельсин'
        bookscollection.add_new_book(book)
        bookscollection.add_book_in_favorites(book)
        bookscollection.add_book_in_favorites(book)
        assert len(bookscollection.favorites) == 1

    # Восьмой метод
    def test_delete_book_from_favorites_successful_delete_book(self, bookscollection):
        book = 'Лолита'
        bookscollection.add_new_book(book)
        bookscollection.add_book_in_favorites(book)
        bookscollection.delete_book_from_favorites(book)
        assert book not in bookscollection.favorites

    def test_delete_book_from_favorites_deletion_did_not_cause_an_error(self, bookscollection):
        book = 'Лолита'
        bookscollection.add_new_book(book)
        bookscollection.delete_book_from_favorites(book)
        assert book not in bookscollection.favorites
    # Девятый метод
    def test_get_list_of_favorites_books_book_from_list_return_list_book(self, bookscollection):
        book = 'Лолита'
        bookscollection.add_new_book(book)
        bookscollection.add_book_in_favorites(book)
        assert bookscollection.get_list_of_favorites_books() == [book]