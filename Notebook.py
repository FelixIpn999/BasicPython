import datetime
last_id = 0


class Note:


    def __init__(self, memo, tags =''):
        '''
        A Note is contained in a Notebook
        :param memo:
        :param tags:
        '''

        self.memo = memo
        self.tags = tags
        self.date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id

    def match(self, filter):
        '''
        Does the Note match with the filter?
        :param filter: A word or a string to be placed
        :return:
        '''
        return filter in self.memo or filter in self.tags


class Notebook:
    '''
    Represent a collection of Notes that can be tagged or searched
    '''
    def __init__(self):
        ''' Initialize a list of Nodes'''
        self.notes = []

    def new_Note(self, memo, tags = ''):
        self.notes.append(Note(memo, tags))

    def modify_Note(self, note_id, memo):
        note = self._find_note(note_id)
        if note:
            note.memo = memo
            return True
        return False

    def _find_note(self, note_id):
        for note in self.notes:
            if str(note.id) == str(note_id):
                return note
            return None

    def modify_tags(self, note_id, tags):
        note = self._find_note(note_id)
        if note:
            note.tags = tags
            return True
        return False

    def search(self, filter):
        return [note for note in self.notes if note.match(filter)]