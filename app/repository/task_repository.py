from pydantic.v1 import UUID4
from sqlalchemy.ext.asyncio import AsyncSession
from app.domain.tasks import TaskCreate, Task
from app.models.task import Task as TaskModel
from typing import Optional


class TaskRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, task_data: TaskCreate) -> Task:
        task = TaskModel(**task_data.dict())
        self.session.add(task)
        await self.session.commit()
        await self.session.refresh(task)
        return Task.from_orm(task)

    async def get_by_id(self, task_id: UUID4) -> Optional[Task]:
        result = await self.session.get(TaskModel, task_id)
        return Task.from_orm(result) if result else None

   # TODO: Сделать другие методы: update, delete, filter_by_status