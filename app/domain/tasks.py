from enum import Enum
from pydantic import BaseModel, UUID4
from datetime import datetime


class TaskStatus(Enum):
    TODO = "todo"
    IN_PROGRESS = "in_progress"
    DONE = "done"


class TaskBase(BaseModel):
    title: str
    description: str
    status: TaskStatus


class TaskCreate(TaskBase):
    pass


class Task(TaskBase):
    id: UUID4
    created_at: datetime
    updated_at: datetime
