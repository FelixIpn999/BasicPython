import sys

from Notebook import Note , Notebook

class menu:
    ''' Display a menu with options to be chosen'''
    def __init__(self):
        self.notebook = Notebook()
        self.choices = {
            "1": self.show_notes,
            "2": self.search,
            "3": self.add_note,
            "4": self.modify_Note,
            "5": self.quit
        }

    def display_menu(self):
        print("""
        Notebook menu
        1. Show all Notes
        2. Search Notes
        3. Add Note
        4. Modify Note
        5. Quit
        """)
    def run(self):
        ''' Display the menu and respond to choices'''
        while True:
            self.display_menu()
            choice = input("Enter an option\n")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not valid".format(choice))

    def show_notes(self, notes=None):
        if not notes:
            notes = self.notebook.notes
        for note in notes:
            print("{0}: {1}\n{2}".format(
                note.id, note.tags, note.memo))

    def search(self):
        filter = input("Search for:")
        notes = self.notebook.search(filter)
        self.show_notes()

    def add_note(self):
        memo = input("Add Info to your note :")
        self.notebook.new_Note(memo)
        print("Your note's been added")

    def modify_Note(self):
        id = input("Enter your id to modify your Note")
        memo = input("Enter your note")
        tags = input("Enter tags")
        if memo:
            self.notebook.modify_Note(id,memo)
        if tags:
            self.notebook.modify_tags(id,tags)

    def quit(self):
        print("Exiting the program")


if __name__ == "__main__":
    menu().run()
