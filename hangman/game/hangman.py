class Hangman:
    def __init__(self):
        self._pole = ["_________", "|","|","|","|","|","|_____" ]
        self._person = [ "|", "0", "/ | \\", "/ \\" ]

    def display_pole(self):
        for i in self._pole:
            print(i)

    def display_person(self):
        for i in self._person:
            print(i)

    def cut_line(self):
        self._person.pop(0)



#hangman = ([ _________
      #  |       |
      #  |       0
      #  |     / | \
      #  |      / \
      #  |
      #  |_____ ])