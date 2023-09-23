from sqlalchemy import inspect

from database import Session, engine
from models import Base, Author, Book, AuthorBook
from sqlalchemy.orm import joinedload


def ensure_tables_created():
    inspector = inspect(engine)
    existing_tables = set(inspector.get_table_names())

    required_tables = set(Base.metadata.tables.keys())

    if not required_tables.issubset(existing_tables):
        print("Creating tables...")
        Base.metadata.create_all(bind=engine)
        print("Tables created successfully!")
    else:
        print("Tables already exist. Skipping creation.")


def add_book(title, number_of_pages, author_first_name, author_last_name):
    session = Session()
    try:
        # Check if the author already exists
        author = session.query(Author).filter_by(firstName=author_first_name, lastName=author_last_name).first()

        # If the author doesn't exist, add them
        if not author:
            author = Author(firstName=author_first_name, lastName=author_last_name)
            session.add(author)

        # Add the book
        book = Book(title=title, numberOfPages=number_of_pages)
        session.add(book)

        # Update the association table
        association = AuthorBook(author=author, book=book)
        session.add(association)

        session.commit()
    except Exception as e:
        session.rollback()
        print(f"Error: {e}")
    finally:
        session.close()


def get_book_and_authors(title):
    session = Session()
    try:
        book = session.query(Book).options(joinedload(Book.authors)).filter_by(title=title).first()
        if book:
            print(f"Book: {book.title}, Pages: {book.numberOfPages}")
            for author_book in book.authors:
                author = author_book.author
                print(f"Author: {author.firstName} {author.lastName}")
        else:
            print(f"No book found with title '{title}'")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        session.close()


if __name__ == "__main__":
    ensure_tables_created()
    add_book("A Great Book", 300, "Or", "Hasson")
    get_book_and_authors("A Great Book")
