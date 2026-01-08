from book import book_details

def test_book_details():
    result =book_details(
        101,
        " the sanjav story",
        "sanjav",
        2020
    )

    expected_output = (
        "Book ID: 101\n"
        "Book Title: the sanjav story\n"
        "Author Name:sanjav \n"
        "Year of Publication: 2020"
    )

    assert result == expected_output
