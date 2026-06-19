from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.db import get_db
from app.schemas import BookCreate, BookResponse, BookUpdate
from app.db.models import Book, Category

router = APIRouter(prefix="/books", tags=["Books"])

@router.get("/", response_model=list[BookResponse])
def read_books(category_id: int = None, db: Session = Depends(get_db)):
    query = db.query(Book)
    if category_id:
        query = query.filter(Book.category_id == category_id)
    return query.all()

@router.post("/", response_model=BookResponse, status_code=201)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    cat_exists = db.query(Category).filter(Category.id == book.category_id).first()
    if not cat_exists:
        raise HTTPException(status_code=400, detail="Такой категории не существует")
    db_book = Book(
        title=book.title,
        description=book.description,
        price=book.price,
        url=book.url,
        category_id=book.category_id
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

@router.get("/{book_id}", response_model=BookResponse)
def read_book(book_id: int, db: Session = Depends(get_db)):
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if not db_book:
        raise HTTPException(status_code=404, detail="Книга не найдена")
    return db_book

@router.put("/{book_id}", response_model=BookResponse)
def update_book(book_id: int, book_data: BookUpdate, db: Session = Depends(get_db)):
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if not db_book:
        raise HTTPException(status_code=404, detail="Книга не найдена")
    if book_data.category_id is not None:
        cat_exists = db.query(Category).filter(Category.id == book_data.category_id).first()
        if not cat_exists:
            raise HTTPException(status_code=400, detail="Указанная категория не существует")
    for key, value in book_data.model_dump(exclude_unset=True).items():
        setattr(db_book, key, value)
    db.commit()
    db.refresh(db_book)
    return db_book

@router.delete("/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if not db_book:
        raise HTTPException(status_code=404, detail="Книга не найдена")
    db.delete(db_book)
    db.commit()
    return {"message": "Книга удалена успешно"}
