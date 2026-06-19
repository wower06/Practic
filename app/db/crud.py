from sqlalchemy.orm import Session
from app.db import models

# --- ФУНКЦИИ ДЛЯ КАТЕГОРИЙ ---

def create_category(db: Session, title: str):
    db_category = models.Category(title=title)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def get_categories(db: Session):
    return db.query(models.Category).all()

# --- ФУНКЦИИ ДЛЯ КНИГ ---

def create_book(db: Session, title: str, description: str, price: float, category_id: int):
    db_book = models.Book(
        title=title, 
        description=description, 
        price=price, 
        category_id=category_id
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def get_books(db: Session):
    return db.query(models.Book).all()