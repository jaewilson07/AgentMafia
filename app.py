import streamlit as st
from storage import Storage
from datetime import datetime

# Initialize storage
storage = Storage()

def main():
    st.title("Notes Application")
    
    # Sidebar for actions
    action = st.sidebar.selectbox(
        "Choose an action",
        ["View Notes", "Create Note"]
    )

    if action == "Create Note":
        create_note()
    else:
        view_notes()

def create_note():
    st.header("Create a New Note")
    
    with st.form("note_form"):
        title = st.text_input("Title")
        content = st.text_area("Content")
        submit = st.form_submit_button("Save Note")

        if submit:
            if title and content:
                try:
                    storage.add_note(title, content)
                    st.success("Note created successfully!")
                    st.rerun()
                except Exception as e:
                    st.error(f"Error creating note: {str(e)}")
            else:
                st.warning("Please fill in both title and content.")

def view_notes():
    st.header("Your Notes")
    
    try:
        notes = storage.get_notes()
        
        if not notes:
            st.info("No notes found. Create your first note!")
            return

        for note in notes:
            with st.expander(f"📝 {note.title}"):
                st.write(note.content)
                st.text(f"Created: {note.created_at.strftime('%Y-%m-%d %H:%M:%S')}")
                if note.updated_at:
                    st.text(f"Updated: {note.updated_at.strftime('%Y-%m-%d %H:%M:%S')}")
                
                col1, col2 = st.columns(2)
                with col1:
                    if st.button(f"Delete {note.title}", key=f"delete_{note.id}"):
                        try:
                            storage.delete_note(note.id)
                            st.success("Note deleted successfully!")
                            st.rerun()
                        except Exception as e:
                            st.error(f"Error deleting note: {str(e)}")
                
                with col2:
                    if st.button(f"Edit {note.title}", key=f"edit_{note.id}"):
                        st.session_state.editing_note = note
                        st.rerun()

        # Edit note form
        if hasattr(st.session_state, 'editing_note'):
            note = st.session_state.editing_note
            st.header(f"Edit Note: {note.title}")
            
            with st.form("edit_form"):
                new_title = st.text_input("Title", value=note.title)
                new_content = st.text_area("Content", value=note.content)
                save = st.form_submit_button("Save Changes")

                if save:
                    if new_title and new_content:
                        try:
                            storage.update_note(note.id, new_title, new_content)
                            del st.session_state.editing_note
                            st.success("Note updated successfully!")
                            st.rerun()
                        except Exception as e:
                            st.error(f"Error updating note: {str(e)}")
                    else:
                        st.warning("Please fill in both title and content.")

    except Exception as e:
        st.error(f"Error loading notes: {str(e)}")

if __name__ == "__main__":
    main()
