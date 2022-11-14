class User:
    def __init__(self, name, age, key):
        # string | Thor
        self.name = name
        # int | 23
        self.age = age
        # [1]
        self.userKey = key
    
    def get_name(self):
        return self.name
    def get_key(self):
        return self.userKey

    def clear(self):
        self.name = ''
        self.age = None
        self.userKey = []

    def __str__(self):
        return f'{self.name}'