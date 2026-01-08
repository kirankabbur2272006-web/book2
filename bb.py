def book_details(title, author, book_id, year):
    return (
        f"Book ID: {book_id}\n"
        f"Book Title: {title}\n"
        f"Author Name: {author}\n"
        f"Year of Publication: {year}"
    )

if __name__ == "__main__":
    title = "The Sanjav Story"
    author = "Sanjav"
    book_id = 12345
    year = 2020

    print(book_details(title, author, book_id, year))
