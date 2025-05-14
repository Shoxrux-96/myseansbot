from fastapi import FastAPI, Request, Query
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from admin.database import SessionLocal, User, Message
import math

app = FastAPI()
templates = Jinja2Templates(directory="admin/templates")


# Sahifani olish yordamchi funksiyasi
def get_paginated_data(query, page: int, page_size: int = 20):
    total = query.count()
    total_pages = math.ceil(total / page_size)
    data = query.offset((page - 1) * page_size).limit(page_size).all()
    return data, total_pages


# Foydalanuvchilar sahifasi
@app.get("/users", response_class=HTMLResponse)
def users(request: Request, page: int = Query(1, ge=1)):
    db: Session = SessionLocal()
    query = db.query(User)
    users_data, total_pages = get_paginated_data(query, page)
    db.close()
    return templates.TemplateResponse("users.html", {
        "request": request,
        "users": users_data,
        "page": page,
        "total_pages": total_pages
    })


# Xabarlar sahifasi
@app.get("/messages", response_class=HTMLResponse)
def messages(request: Request, page: int = Query(1, ge=1)):
    db: Session = SessionLocal()
    query = db.query(Message).order_by(Message.timestamp.desc())
    messages_data, total_pages = get_paginated_data(query, page)
    db.close()
    return templates.TemplateResponse("messages.html", {
        "request": request,
        "messages": messages_data,
        "page": page,
        "total_pages": total_pages
    })
