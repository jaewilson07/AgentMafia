import shelve
from datetime import datetime
import uuid
from typing import List, Optional
from models import Note

class Storage:
    def __init__(self, db_name: str = "streamlit_db"):
        self.db_name = db_name

    def add_note(self, title: str, content: str) -> Note:
        """Add a new note to storage"""
        with shelve.open(self.db_name) as db:
            note_id = str(uuid.uuid4())
            note = Note(
                id=note_id,
                title=title,
                content=content,
                created_at=datetime.now()
            )
            if 'notes' not in db:
                db['notes'] = {}
            db['notes'][note_id] = note
            return note

    def get_notes(self) -> List[Note]:
        """Retrieve all notes from storage"""
        with shelve.open(self.db_name) as db:
            notes = db.get('notes', {})
            return list(notes.values())

    def get_note(self, note_id: str) -> Optional[Note]:
        """Retrieve a specific note by ID"""
        with shelve.open(self.db_name) as db:
            notes = db.get('notes', {})
            return notes.get(note_id)

    def update_note(self, note_id: str, title: str, content: str) -> Optional[Note]:
        """Update an existing note"""
        with shelve.open(self.db_name) as db:
            notes = db.get('notes', {})
            if note_id in notes:
                note = notes[note_id]
                note.title = title
                note.content = content
                note.updated_at = datetime.now()
                notes[note_id] = note
                db['notes'] = notes
                return note
            return None

    def delete_note(self, note_id: str) -> bool:
        """Delete a note by ID"""
        with shelve.open(self.db_name) as db:
            notes = db.get('notes', {})
            if note_id in notes:
                del notes[note_id]
                db['notes'] = notes
                return True
            return False
