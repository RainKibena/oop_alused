class Andmed():
    def __init__(self, *info):
        self.info = list(info)
    def __getitem__(self, i):
        return self.info[i]