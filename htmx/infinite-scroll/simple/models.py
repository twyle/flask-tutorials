class User:
    id = 0
    def __init__(self, fname, lname, email):
        User.id  += 1
        self.id = User.id 
        self.fname = fname
        self.lname = lname 
        self.email = email

    def search(self, word):
        if (word is None):
            return False
        all = self.fname + self.lname + self.email
        return word.lower() in all.lower()