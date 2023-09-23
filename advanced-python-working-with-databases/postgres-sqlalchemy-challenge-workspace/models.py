from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import registry, relationship, declarative_base

mapper_registry = registry()
Base = mapper_registry.generate_base()


class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    firstName = Column(String)
    lastName = Column(String)

    books = relationship("AuthorBook", back_populates="author")

    def __repr__(self):
        return f"<Author(id={self.id}, firstName={self.firstName}, lastName={self.lastName})>"


class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    numberOfPages = Column(Integer)

    authors = relationship("AuthorBook", back_populates="book")

    def __repr__(self):
        return f"<Book(id={self.id}, title={self.title}, numberOfPages={self.numberOfPages})>"


class AuthorBook(Base):
    __tablename__ = 'author_books'
    id = Column(Integer, primary_key=True)
    authorID = Column(Integer, ForeignKey('authors.id'))
    bookID = Column(Integer, ForeignKey('books.id'))

    author = relationship("Author", back_populates="books")
    book = relationship("Book", back_populates="authors")

    def __repr__(self):
        return f"<AuthorBook(id={self.id}, authorID={self.authorID}, bookID={self.bookID})>"
