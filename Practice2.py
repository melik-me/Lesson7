import unittest
import requests

class CreateBookTests(unittest.TestCase):
    def setUp(self):
        self.base_url = "http://pulse-rest-testing.herokuapp.com/"

    def test_create_book_posititve(self):
        books = [
            {'title': "blabla", 'author': 'blabla'},
            {'title': "adsddf", 'author': 'blabla'},
            {'title': "blabla", 'author': 'asdfsd'},
        ]

        for book in books:
            response = requests.post(self.base_url + 'books/', data=book)
            self.assertEqual(response.status_code, 201)

if __name__ == "__main__":
    unittest.main()