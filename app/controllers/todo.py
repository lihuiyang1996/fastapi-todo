from typing import List
from fastapi import HTTPException

from app.core.crud import CRUDBase
from app.models.todo import Todo
from app.schemas.todo import TodoCreate, TodoUpdate


class TodoController(CRUDBase[Todo, TodoCreate, TodoUpdate]):
    def __init__(self):
        super().__init__(model=Todo)

    async def create_for_user(self, user_id: int, todo_in: TodoCreate) -> Todo:
        return await self.model.create(user_id=user_id, **todo_in.model_dump())

    async def get_user_todos(self, user_id: int) -> List[Todo]:
        return await self.model.filter(user_id=user_id).all()

    async def get_user_todo(self, todo_id: int, user_id: int) -> Todo:
        todo = await self.model.get_or_none(id=todo_id, user_id=user_id)
        if not todo:
            raise HTTPException(status_code=404, detail="Todo not found")
        return todo

    async def update_user_todo(self, todo_id: int, user_id: int, todo_in: TodoUpdate) -> Todo:
        todo = await self.get_user_todo(todo_id, user_id)
        await todo.update_from_dict(todo_in.model_dump(exclude_unset=True)).save()
        return todo

    async def delete_user_todo(self, todo_id: int, user_id: int) -> None:
        todo = await self.get_user_todo(todo_id, user_id)
        await todo.delete()


todo_controller = TodoController()