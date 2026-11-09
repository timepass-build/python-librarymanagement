class Book:
    def __init__(self, name):
        self.name = name

    def get_bookname(self):
        return self.name

    def set_bookname(self):
        if "[Marked]" not in self.name:
            self.name = f"{self.name}  [Marked]"