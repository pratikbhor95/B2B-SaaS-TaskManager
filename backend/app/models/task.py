import uuid
from datetime import datetime, timezone
from sqlalchemy import Column, String, Text, DateTime, Enum
import enum
from app.core.database import Base


class TaskStatus(str, enum.Enum):
    PENDING = "pending"
    STARTED = "started"
    COMPLETED = "completed"

class Task(Base):
    __tablename__ = "tasks"

    id = Column(String, primary_key=True, default=lambda:str(uuid.uuid4))
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    status = Column(Enum(TaskStatus), default=TaskStatus.PENDING, nullable=False)
    org_id = Column(String, nullable=False, index=True)  # Assuming org_id is a string, adjust as necessary
    created_by = Column(String, nullable=False)  # Assuming created_by is a string, adjust as necessary
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc), nullable=False)