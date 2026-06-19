from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.db.db import Base

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False) # Название категории

    # Связь с книгами: одна категория может содержать много книг
    books = relationship("Book", back_populates="category")

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)       # Название книги
    description = Column(String)                 # Описание
    price = Column(Float, nullable=False)        # Цена
    url = Column(String, default="")             # Ссылка на товар (пока пустая)
    category_id = Column(Integer, ForeignKey("categories.id")) # Ссылка на категорию

    # Обратная связь с категорией
    category = relationship("Category", back_populates="books")
