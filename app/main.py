from fastapi import FastAPI
from app.api.categories import router as categories_router
from app.api.books import router as books_router

app = FastAPI(title="Library API")

app.include_router(categories_router)
app.include_router(books_router)

@app.get("/health")
def health_check():
    return {"status": "working"}
