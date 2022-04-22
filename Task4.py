class StringFormatter:
    def __init__(self, string, split_let=' '):
        self.__string = string
        self.__split_let = split_let
        self.words = string.split(split_let)

    @property
    def string(self):
        return self.__string

    def del_words(self, n):
        self.__string = ' '.join([c for c in self.words if len(c) >= n ])
        self.words = self.__string.split(' ')

    def change_num(self):
        self.__string = ''.join(['*' if c.isdigit() else c for c in self.__string])
        self.words = self.__string.split(' ')

    def add_spaces(self):
        ss = ''.join(self.words)
        self.__string = ' '.join(ss)
        self.words = self.__string.split(' ')

    def sort_by_len(self):
        self.words.sort(key=lambda x: len(x), reverse=True)
        self.__string = ' '.join(self.words)

    def sort_by_alph(self):
        self.words.sort(key=lambda x: x[0])
        self.__string = ' '.join(self.words)
string = StringFormatter('my name is Povel')
string.del_words(3)
print(string.string)
string2 = StringFormatter('my name is3242 234Povel')
string2.change_num()
print(string2.string)
string3 = StringFormatter('my name is Povel')
string3.add_spaces()
print(string3.string)
string4 = StringFormatter('my name is Povel')
string4.sort_by_len()
print(string4.string)
string4.sort_by_alph()
print(string4.string)