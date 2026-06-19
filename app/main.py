from app.db.db import SessionLocal
from app.db import crud

def main():
    print("--- ПОДКЛЮЧЕНИЕ К БАЗЕ ДАННЫХ ---")
    db = SessionLocal()
    try:
        categories = crud.get_categories(db)
        books = crud.get_books(db)

        print(f"\nНайдено категорий: {len(categories)}")
        for cat in categories:
            print(f" ID: {cat.id} | Название: {cat.title}")

        print(f"\nНайдено книг: {len(books)}")
        for book in books:
            print(f" Книга: \"{book.title}\" | Цена: {book.price} руб. | ID категории: {book.category_id}")
            print("-" * 40)
    finally:
        db.close()

if __name__ == "__main__":
    main()