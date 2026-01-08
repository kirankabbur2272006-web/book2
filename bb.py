def book_details(title, author, book_id, year):
    return (
        f"Book ID: {book_id}\n"
        f"Book Title: {title}\n"
        f"Author Name: {author}\n"
        f"Year of Publication: {year}"
    )

if __name__ == "__main__":
    title = " the sanjav story "
    author = "Sanjav"
    book_id = 101
    year = 2020

    print(book_details(title, author, book_id, year))
