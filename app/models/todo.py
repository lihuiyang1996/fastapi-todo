from tortoise import fields
from .base import BaseModel, TimestampMixin


class Todo(BaseModel, TimestampMixin):
    title = fields.CharField(max_length=100, description="标题")
    description = fields.TextField(null=True, description="描述")
    is_completed = fields.BooleanField(default=False, description="是否完成", index=True)
    due_date = fields.DatetimeField(null=True, description="截止时间", index=True)

    # 外键：关联到用户
    user = fields.ForeignKeyField("models.User", related_name="todos", description="所属用户")

    class Meta:
        table = "todo"