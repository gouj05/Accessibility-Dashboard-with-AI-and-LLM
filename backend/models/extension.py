from sqlalchemy import Column, Integer, String
from database import Base

class Extension(Base):
    __tablename__ = "extensions"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    image = Column(String)
    download = Column(String)