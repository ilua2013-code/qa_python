import pytest 
from main import BooksCollector


@pytest.fixture
def bookscollection():
    return BooksCollector()

