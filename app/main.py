from app.db.db import SessionLocal
from app.db import crud

def show_db_data():
    session = SessionLocal()
    
    print("--- Проверка данных в БД ---")
    
    # достаем категории и выводим списком
    cats = crud.get_categories(session)
    print(f"\nВсего категорий в базе: {len(cats)}")
    for c in cats:
        print(f"ID: {c.id} | Название: {c.title}")

    # теперь выводим книги
    all_books = crud.get_books(session)
    print(f"\nСписок книг ({len(all_books)} шт.):")
    
    for b in all_books:
        print(f"- Книга: {b.title}")
        print(f"  Цена: {b.price} руб.")
        print(f"  Категория (ID): {b.category_id}")
        print("*" * 30)

    session.close()

if __name__ == "__main__":
    show_db_data()