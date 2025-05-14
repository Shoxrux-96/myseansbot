from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# Baza bilan ulanish
engine = create_engine("sqlite:///data.db", connect_args={"check_same_thread": False})
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)

# Jadval: Foydalanuvchilar
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, unique=True)
    name = Column(String)
    username = Column(String)

# Jadval: Xabarlar
class Message(Base):
    __tablename__ = "messages"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    name = Column(String)
    username = Column(String, nullable=True)
    user_message = Column(Text)
    ai_reply = Column(Text, nullable=True)
    file_name = Column(String, nullable=True)
    timestamp = Column(DateTime, default=datetime.utcnow)

# Barcha jadvallarni yaratish
Base.metadata.create_all(bind=engine)

# Funksiya: Xabar qo‘shish
def insert_message(user_id, name, username, user_message, ai_reply, file_name=None):
    session = SessionLocal()
    msg = Message(
        user_id=user_id,
        name=name,
        username=username,
        user_message=user_message,
        ai_reply=ai_reply,
        file_name=file_name
    )
    session.add(msg)
    session.commit()
    session.close()

# Funksiya: Foydalanuvchini qo‘shish yoki yangilash
def upsert_user(user_id, name, username):
    session = SessionLocal()
    user = session.query(User).filter_by(user_id=user_id).first()
    if user:
        user.name = name
        user.username = username
    else:
        user = User(user_id=user_id, name=name, username=username)
        session.add(user)
    session.commit()
    session.close()
