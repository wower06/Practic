from app.db.db import SessionLocal, engine, Base
from app.db import crud

def init_database():
    print("Создаем таблицы в базе данных...")
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()
    try:
        existing_categories = crud.get_categories(db)
        if not existing_categories:
            print("Заполняем базу начальными данными...")
            
            # Создаем категории
            cat_fiction = crud.create_category(db, title="Фантастика")
            cat_science = crud.create_category(db, title="Наука и IT")

            # Добавляем книги
            crud.create_book(db, title="Дюна", description="Культовый научно-фантастический роман Фрэнка Герберта.", price=850.0, category_id=cat_fiction.id)
            crud.create_book(db, title="Основание", description="Фантастика Айзека Азимова.", price=720.0, category_id=cat_fiction.id)
            crud.create_book(db, title="Чистый код", description="Руководство по созданию хорошего кода.", price=1200.0, category_id=cat_science.id)
            
            print("База данных успешно заполнена!")
        else:
            print("База данных уже содержит данные.")
    finally:
        db.close()

if __name__ == "__main__":
    init_database()
