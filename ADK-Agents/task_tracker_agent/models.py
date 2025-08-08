from typing import Literal, Optional, List, TypedDict
from dataclasses import dataclass

PriorityLevel = Literal["High", "Medium", "Low"]
TaskStatus = Literal["Complete", "Incomplete"]


@dataclass
class Task:
    id: str
    description: str
    priority: PriorityLevel
    status: TaskStatus


class AddTaskResponse(TypedDict):
    status: Literal["success"]
    task: Task


class ReadTaskResponse(TypedDict):
    status: Literal["success"]
    tasks: List[Task]


class UpdateDeleteResponse(TypedDict):
    status: Literal["success", "error"]
    updated: Optional[bool]
    deleted: Optional[bool]
    message: Optional[str]
