from datetime import date

last_id = 0

class Note:
    '''Represent a note in the notebook. Match against aObjects in Python
       string in searches and store tags for each note.'''
    
    def __init__(self, memo, tags=''):
        self.memo = memo
        self.tags = tags
        self.creation_date = date.today()
        global last_id
        last_id += 1
        self.id = last_id
    
    def match(self, search_filter):
        '''Determine if this note matches the filter
           text. Return True if it matches, False otherwise.
           Search is case sensitive and matches both text and
           tags.'''
        return (search_filter in str(self.memo)) or (search_filter in self.tags)

class Notebook:
    def __init__(self):
        self.notes = []
    
    def new_note(self, memo, tags = ''):
        '''Create a new note and add it to the list.'''
        self.notes.append(Note(memo, tags))
    
    def _find_note(self, note_id):
        '''Locate the note with the given id.'''
        for note in self.notes:
            if note.id == note_id:
                return note
        return None

    def modify_memo(self, note_id, memo):
        '''Find the note with the given id and change its
        memo to the given value.'''
        note = self._find_note(note_id)
        if note:
            note.memo = memo
            return True
        return False
    
    def modify_tags(self, note_id, tags):
        '''Find the note with the given id and change its
        memo to the given value.'''
        note = self._find_note(note_id)
        if note:
            note.tags = tags
            return True
        return False
    
    def search(self, search_filter):
        '''Find all notes that match the given filter
           string.'''
        return [note for note in self.notes if note.match(search_filter)]
