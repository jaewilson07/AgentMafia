from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Note:
    """Data model for notes"""
    id: str
    title: str
    content: str
    created_at: datetime
    updated_at: Optional[datetime] = None
