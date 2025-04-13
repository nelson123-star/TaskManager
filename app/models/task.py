from sqlalchemy import Column, String, DateTime, Enum, Integer
from app.database.database import Base
from sqlalchemy.sql import func

class Task(Base):
    __tablename__ = "tasks"
    # id = Column(UUID, primary_key=True, server_default=func.uuid_generate_v4())
    # title = Column(String, nullable=False)
    # description = Column(String)
    # status = Column(Enum("todo", "in_progress", "done", name="task_status"))
    # created_at = Column(DateTime, server_default=func.now())
    # updated_at = Column(DateTime, onupdate=func.now())

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    status = Column(Enum("todo", "in_progress", "done", name="task_status"))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)