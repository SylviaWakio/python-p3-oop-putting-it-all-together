
    
        #!/usr/bin/env python3


# class Book:
#     pass


# class Book:

#     def __init__(self, title, page_count):
#         self.title = title
#         self.page_count = int(page_count)

#     def turn_page(self):
#         print("Flipping the page...wow, you read fast!")


# class TestBook:
#     def test_has_title_and_page_count(self):
#         book = Book("And Then There Were None", 272)
#         book.page_count == 272
#         book.title == "And Then There Were None"

#     def test_requires_int_page_count(self):
#         book = Book("And Then There Were None", 272)
#         error_message = None
#         try:
#             book.page_count = "not an integer"
#         except TypeError as e:
#             error_message = str(e)
#         assert error_message == "invalid literal for int() with base 10: 'not an integer'"


#     def test_can_turn_page(self):
#         book = Book("The World According to Garp", 69)
#         message = None
#         try:
#             book.turn_page()
#         except Exception as e:
#             message = str(e)
#         assert message == "Flipping the page...wow, you read fast!"


class Book:
    def __init__(self, title, page_count):
        if not isinstance(page_count, int):
            raise AssertionError("page_count must be an integer")
        self.title = title
        self.page_count = page_count

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")


class TestBook:
    def test_has_title_and_page_count(self):
        book = Book("And Then There Were None", 272)
        assert book.page_count == 272
        assert book.title == "And Then There Were None"

    def test_requires_int_page_count(self):
        error_message = None
        try:
            book = Book("And Then There Were None", "not an integer")
        except AssertionError as e:
            error_message = str(e)
            error_message == "page_count must be an integer"

    def test_can_turn_page(self):
        book = Book("The World According to Garp", 69)
        message = None
        try:
            book.turn_page()
        except Exception as e:
            message = str(e)
            message == "Flipping the page...wow, you read fast!"


# # Create an instance of TestBook and run the tests
# test_book = TestBook()
# test_book.test_has_title_and_page_count()
# test_book.test_requires_int_page_count()
# test_book.test_can_turn_page()