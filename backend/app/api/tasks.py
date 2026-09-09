from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.core.database import get_db
from app.core.auth import AuthUser, get_current_user, require_view, require_create, require_edit, require_delete
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate, TaskResponse, TaskStatusUpdate

router = APIRouter(
    prefix="/api/tasks",
    tags=["tasks"],
)

@router.get("", response_model=List[TaskResponse])
def list_tasks(user: AuthUser = Depends(require_view), db: Session = Depends(get_db)):
    tasks = db.query(Task).filter(Task.org_id == user.org_id).all()
    return tasks

@router.post("", response_model=TaskResponse)
def create_task(
    task_data: TaskCreate,
    user: AuthUser = Depends(require_create), 
    db: Session = Depends(get_db)
    ):
    task = Task(
        title=task_data.title,
        description=task_data.description,
        status=task_data.status,
        org_id=user.org_id,
        created_by=user.user_id
    )
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

@router.get("/{task_id}", response_model=TaskResponse)
def get_task(
    task_id: str, 
    user: AuthUser = Depends(require_view), 
    db: Session = Depends(get_db)
    ):
    task = db.query(Task).filter(
        Task.id == task_id, 
        Task.org_id == user.org_id).first()
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Task not found")
    return task