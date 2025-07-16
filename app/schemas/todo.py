from datetime import datetime, date
from typing import Optional
from pydantic import BaseModel, Field


class BaseTodo(BaseModel):
    id: int
    title: str
    description: Optional[str] = ""
    is_completed: bool = False
    due_date: Optional[date] = None
    user_id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class TodoCreate(BaseModel):
    title: str = Field(..., example="完成项目文档")
    description: Optional[str] = Field("", example="补充接口文档说明")
    due_date: Optional[date] = Field(None, example="2025-07-20")
    user_id: int = Field(..., example=123) 


class TodoUpdate(BaseModel):
    id: int = Field(..., example=1)
    title: Optional[str] = Field(None, example="更新任务标题")
    description: Optional[str] = Field(None, example="更新描述")
    is_completed: Optional[bool] = Field(None, example=True)
    due_date: Optional[date] = Field(None, example="2025-07-30")