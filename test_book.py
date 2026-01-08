def book_details(title, author, book_id, year):
    result = {
        "title": title,
        "author": author,
        "book_id": book_id,
        "year": year
    }
    return result
if __name__ == "__main__":
    title = "the sanjav story"
    author = "sanjav"
    book_id = 12345
    year = 2020
    print(book_details(title, author, book_id, year))
