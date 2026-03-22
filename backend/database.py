from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# 🔥 DATABASE URL (update if needed)
DATABASE_URL = "postgresql://postgres:password@localhost:5432/accessibility_db"

# 🔌 Engine
engine = create_engine(DATABASE_URL)

# 🧠 Session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 🏗️ Base
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()